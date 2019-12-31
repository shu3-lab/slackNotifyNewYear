import json
import urllib.request
import os

def lambda_handler(event, context):
    result = post_slack()
    if 'ok' in json.dumps(result):
        body = json.dumps(result)
    else:
        body = 'NG!Watch logs of execution!'
        
    return {
        'statusCode': 200,
        'body': "slack result is " + body
    }
    
def post_slack():
    message = "<!channel> *Happy new year 2020!*"

    send_data = {
        "username": "SUZUKIKE_BOT",
        "icon_emoji": ":laughing:",
        "text": message
    }
    
    send_text = "payload=" + json.dumps(send_data)
    headers = {"Content-Type" : "application/json"}
    request = urllib.request.Request(
        os.environ["slack_url"], 
        data=send_text.encode('utf-8'),
        method="POST"
    )
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode('utf-8')
    except urllib.error.HTTPError as error:
        print(str(error.code) + error.reason)
    else:
        return response_body
