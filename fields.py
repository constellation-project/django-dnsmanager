from django.core.validators import RegexValidator
from django.db import models


class RecordNameField(models.CharField):

    record_name_validator = RegexValidator(
        regex=r'(?:[a-zA-Z0-9_][a-zA-Z0-9_-]{0,62}(?<!-)\.)*(?:[a-zA-Z0-9_][a-zA-Z0-9_-]{0,62}(?<!-))',
        message='Not a valid domain name',
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 253
        if 'editable' not in kwargs:
            kwargs['editable'] = True
        if 'validators' in kwargs:
            kwargs['validators'].append(RecordNameField.record_name_validator)
        else:
            kwargs['validators'] = [RecordNameField.record_name_validator]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        if 'validators' in kwargs:
            if RecordNameField.record_name_validator in kwargs['validators']:
                kwargs['validators'].remove(
                    RecordNameField.record_name_validator)
            if not kwargs['validators']:
                del kwargs['validators']
        return name, path, args, kwargs


class DomainNameField(models.CharField):

    domain_name_validator = RegexValidator(
        regex=r'(?:[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(?<!-)\.)*(?:[a-zA-Z0-9][a-zA-Z0-9-]{0,62}(?<!-))',
        message='Not a valid domain name',
    )

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 253
        if 'editable' not in kwargs:
            kwargs['editable'] = True
        if 'validators' in kwargs:
            kwargs['validators'].append(DomainNameField.domain_name_validator)
        else:
            kwargs['validators'] = [DomainNameField.domain_name_validator]
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['max_length']
        if 'validators' in kwargs:
            if DomainNameField.domain_name_validator in kwargs['validators']:
                kwargs['validators'].remove(
                    DomainNameField.domain_name_validator)
            if not kwargs['validators']:
                del kwargs['validators']
        return name, path, args, kwargs
