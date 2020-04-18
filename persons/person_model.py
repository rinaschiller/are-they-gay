import os
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class PersonModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        if 'ENV' in os.environ:
            host = 'http://localhost:8000'
        else:
            region = 'us-east-1'
            host = 'https://dynamodb.us-east-1.amazonaws.com'

    person_id = UnicodeAttribute(hash_key=True, null=False)
    first_name = UnicodeAttribute(null=False)
    last_name = UnicodeAttribute(null=False)
    is_gay = UnicodeAttribute(null=False, default='no')
    gender = UnicodeAttribute(null=True)
    zodiac_sign = UnicodeAttribute(null=True)
    sexuality = UnicodeAttribute(null=True)
    pronouns = UnicodeAttribute(null=True)
    image_url = UnicodeAttribute(null=True)
    twitter_handle = UnicodeAttribute(null=True)
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.now())
    updatedAt = UTCDateTimeAttribute(null=False)

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        super(PersonModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
