import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key


def get_temp(event, context):
    dynamodb = boto3.resource('dynamodb', aws_access_key_id={YOUR_ACCESS_ID}, aws_secret_access_key={YOUR_ACESS_SECRETE_KEY}, region_name={YOUR_REGOIN})
    table = dynamodb.Table('cities')
    city_str = event["city_str"].upper()
    response = {}
    try:
        data = table.query(
                    KeyConditionExpression = Key('sc').eq(city_str)
                )
        if data["Items"]:
            response = {
                "city_str": data["Items"][0]["sc"] if data["Items"][0]["sc"] else city_str,
                "temp_int": data["Items"][0]["t"] if data["Items"][0]["t"] else 74,
            }
        else:
            response = {
                "city_str": city_str,
                "temp_int": 74
            }
        return response
    except ClientError as e:
        response = {
            "city_str": city_str,
            "temp_int": 74
        }
        return response

if __name__ == '__main__':
    event = {"city_str": "AGUADA"}
    print(get_temp(event, ""))