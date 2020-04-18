import json
from persons.person_model import PersonModel

def person_list(event, context):
    # fetch all persons from the database
    results = PersonModel.scan()

    # create a response
    return {'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': 'true',
            },
            'body': json.dumps({'items': [dict(result) for result in results]})}
