import json
import logging
import uuid

from persons.person_model import PersonModel


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the person item.'})}

    if not data['text']:
        logging.error('Validation Failed - text was empty. %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the person item. As text was empty.'})}

    a_person = PersonModel(person_id=str(uuid.uuid1()),
                           first_name=data['first_name'],
                           last_name=data['last_name'],
                           gender=data['gender'],
                           is_gay=data['is_gay'],
                           sexuality=data['sexuality'],
                           pronouns=data['pronouns'],
                           image_url=data['image_url'],
                           twitter_handle=data['twitter_handle']
                           )

    # write the person to the database
    a_person.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_person))}
