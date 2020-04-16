import json
import logging

from pynamodb.exceptions import DoesNotExist
from persons.person_model import PersonModel


def update(event, context):
    # TODO: Figure out why this is behaving differently to the other endpoints
    print("Event is---")
    print(event)
    data = json.loads(event.get('body'))

    if 'person_id' not in data and 'last_name' not in data:
        logging.error('Validation Failed %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t update the person item.'})}

    try:
        found_person = PersonModel.get(hash_key=event['path']['person_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'Person was not found'})}

    person_changed = False
    # TODO: Need to perform this check for all attributes so that they are updated
    if 'last_name' in data and data.get('last_name') != found_person.last_name:
        found_person.last_name = data['last_name']
        person_changed = True
    if 'first_name' in data and data.get('first_name') != found_person.checked:
        found_person.first_name = data['first_name']
        person_changed = True

    if person_changed:
        found_person.save()
    else:
        logging.info('Nothing changed, did not update')

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_person))}

