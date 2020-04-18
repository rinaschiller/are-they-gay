import json

from pynamodb.exceptions import DoesNotExist
from persons.person_model import PersonModel

def get(event, context):
    try:
        found_person = PersonModel.get(hash_key=event['path']['person_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'Person was not found'})}

    # create a response
    return {'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
            },
            'body': json.dumps(dict(found_person))}
