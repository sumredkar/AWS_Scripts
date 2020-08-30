import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):

	bucket_name = event["bucket_name"]
	s3 = boto3.client('s3')
	bucket_objects = list_bucket_objects(s3, bucket_name)
	if bucket_objects is None:
		return dict(status_code=200,message="Empty bucket")
	
	for object in bucket_objects:
		try:
			s3.delete_object(Bucket=bucket_name, Key=object["Key"])
		except ClientError as e:
			print("Unable to delete Object.")
	
	return dict(status_code=200,message="Bucket Clear Successfully")
	

def list_bucket_objects(s3, bucket_name):
    # Retrieve the list of bucket objects
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Contents']