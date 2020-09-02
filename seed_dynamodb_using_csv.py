import boto3
from csv import reader


def lambda_handler(event, context):
    try:                       
        dyndb = boto3.client('dynamodb', aws_access_key_id={YOUR_ACCESS_ID}, aws_secret_access_key={YOUR_ACCESS_SECRETE_ID}, region_name={YOUR_REGION})
        # open file in read mode
        with open('employee.csv', 'r', errors='ignore') as read_obj:
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                empid = row[1]
                name = row[0]
                response = dyndb.put_item(
                    TableName='emplist',
                    Item={
                        'empid' : {'N': str(empid)},
                        'name': {'S': name},
                    }
                )
        print('Put succeeded:')
    except Exception as e:
        print (str(e))

lambda_handler("","")