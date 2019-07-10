#Zakkai_Goldman_301165759
#Itzik_Reuven_200856409

from botocore.vendored import requests
import json


def lambda_handler(event, context):
    number = event["number"];

    status = 'off'
    if (number > 25):
        status = 'on'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    req = requests.post("https://iot.fernbach.ml",
                        data=json.dumps({'device_id': 'zakkai_itzik_final', 'status': status}), headers=headers)

    return {
        'status': status,
        'statusCode': req.status_code,
        'body': json.dumps('Hello from Itzik & Zakkai!')
    }