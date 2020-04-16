import json
import logging
import uuid

from persons.person_model import PersonModel


def create(event, context):
    data = json.loads(event['body'])
    print(data)
    if 'first_name' not in data and 'last_name' not in data and 'is_gay' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the person item.'})}

    if not data.get('first_name') and not data.get('is_gay') and not data.get('last_name'):
        logging.error('Validation Failed - text was empty. %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the person item. As text was empty.'})}

    a_person = PersonModel(person_id=str(uuid.uuid1()),
                           first_name=data.get('first_name'),
                           last_name=data.get('last_name'),
                           gender=data.get('gender'),
                           is_gay=data.get('is_gay'),
                           sexuality=data.get('sexuality'),
                           pronouns=data.get('pronouns'),
                           image_url=data.get('image_url'),
                           twitter_handle=data.get('twitter_handle'))

    # write the person to the database
    a_person.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_person))}
