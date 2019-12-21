from collections.abc import Mapping

from django.db import models
from rest_framework import serializers

"""
This is an adaptation of https://github.com/apirobot/django-rest-polymorphic/
by Denis Orehovsky, MIT licenced.

It integrates django-polymorphic with restframework.
"""


class PolymorphicSerializer(serializers.Serializer):
    model_serializer_mapping = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_serializer_mapping = self.model_serializer_mapping
        self.model_serializer_mapping = {}
        self.resource_type_model_mapping = {}

        for model, serializer in model_serializer_mapping.items():
            resource_type = self.to_resource_type(model)
            if callable(serializer):
                serializer = serializer(*args, **kwargs)
                serializer.parent = self

            self.resource_type_model_mapping[resource_type] = model
            self.model_serializer_mapping[model] = serializer

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name

    def to_representation(self, instance):
        if isinstance(instance, Mapping):
            resource_type = self._get_resource_type_from_mapping(instance)
            serializer = self._get_serializer_from_resource_type(resource_type)
        else:
            resource_type = self.to_resource_type(instance)
            serializer = self._get_serializer_from_model_or_instance(instance)

        ret = serializer.to_representation(instance)
        ret['resourcetype'] = resource_type
        return ret

    def to_internal_value(self, data):
        resource_type = self._get_resource_type_from_mapping(data)
        serializer = self._get_serializer_from_resource_type(resource_type)

        ret = serializer.to_internal_value(data)
        ret['resourcetype'] = resource_type
        return ret

    def create(self, validated_data):
        resource_type = validated_data.pop('resourcetype')
        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.create(validated_data)

    def update(self, instance, validated_data):
        resource_type = validated_data.pop('resourcetype')
        serializer = self._get_serializer_from_resource_type(resource_type)
        return serializer.update(instance, validated_data)

    def is_valid(self, *args, **kwargs):
        valid = super().is_valid(*args, **kwargs)
        try:
            resource_type = self._get_resource_type_from_mapping(
                self.validated_data)
            serializer = self._get_serializer_from_resource_type(resource_type)
        except serializers.ValidationError:
            child_valid = False
        else:
            child_valid = serializer.is_valid(*args, **kwargs)
            self._errors.update(serializer.errors)
        return valid and child_valid

    def _to_model(self, model_or_instance):
        return (model_or_instance.__class__
                if isinstance(model_or_instance, models.Model)
                else model_or_instance)

    def _get_resource_type_from_mapping(self, mapping):
        try:
            return mapping['resourcetype']
        except KeyError:
            raise serializers.ValidationError({
                'resourcetype': 'This field is required',
            })

    def _get_serializer_from_model_or_instance(self, model_or_instance):
        model = self._to_model(model_or_instance)

        for klass in model.mro():
            if klass in self.model_serializer_mapping:
                return self.model_serializer_mapping[klass]

        raise KeyError(
            '`{cls}.model_serializer_mapping` is missing '
            'a corresponding serializer for `{model}` model'.format(
                cls=self.__class__.__name__,
                model=model.__name__
            )
        )

    def _get_serializer_from_resource_type(self, resource_type):
        model = self.resource_type_model_mapping[resource_type]
        return self._get_serializer_from_model_or_instance(model)
