import json

def hello(event, context):
    body = {
        "message": "Hello World",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this if you don't use the http event 
    """
    return {
        "message": "Hello World",
        "event": event
    }
    """
