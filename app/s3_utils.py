import boto3
import os

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

BUCKET = os.getenv("S3_BUCKET")

def upload_to_s3(file_obj, filename):
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))

    content_type = 'image/jpeg'  # or detect using mimetypes module

    s3.upload_fileobj(
        Fileobj=file_obj,
        Bucket=os.getenv("S3_BUCKET"),
        Key=filename,
        ExtraArgs={
         
            "ContentType": content_type
        }
    )

    s3_url = f"https://{os.getenv('S3_BUCKET')}.s3.amazonaws.com/{filename}"
    return s3_url

