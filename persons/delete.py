import json

from pynamodb.exceptions import DoesNotExist, DeleteError
from persons.person_model import PersonModel


def delete(event, context):
    try:
        found_person = PersonModel.get(hash_key=event['path']['person_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'Person was not found'})}
    try:
        found_person.delete()
    except DeleteError:
        return {'statusCode': 400,
                'body': json.dumps({'error_message': 'Unable to delete the Person'})}

    # create a response
    return {'statusCode': 204}
