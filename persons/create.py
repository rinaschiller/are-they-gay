import json
import logging
import uuid

from persons.person_model import PersonModel


def create(event, context):
    if 'body' in event:
        data = json.loads(event['body'])
    else:
        data = event
    print(event)
    if 'first_name' not in data and 'last_name' not in data and 'is_gay' not in data:
        logging.info(event)
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the person item because required fields not in JSON payload.'})}

   # TODO: handle if someone with that name already exists

    a_person = PersonModel(person_id=str(uuid.uuid1()),
                           first_name=data.get('first_name'),
                           last_name=data.get('last_name'),
                           gender=data.get('gender'),
                           is_gay=data.get('is_gay'),
                           zodiac_sign=data.get('zodiac'),
                           sexuality=data.get('sexuality'),
                           pronouns=data.get('pronouns'),
                           image_url=data.get('image_url'),
                           twitter_handle=data.get('twitter_handle'))

    # write the person to the database
    a_person.save()

    logging.info('Person {} {} successfully created'.format(a_person.first_name, a_person.last_name))
    # create a response
    return {'statusCode': 201,
            'message': 'Person successfully created',
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
            },
            'body': json.dumps(dict(a_person))}
