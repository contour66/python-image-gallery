import logging
import boto3
import json
from botocore.exceptions import ClientError
import requests


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# def get_object(bucket_name, key):
#     try:
#         s3_client = boto3.client('s3')
#         result = s3_client.get_object(Bucket=bucket_name, Key=key)
#     except ClientError as e:
#         logging.error(e)
#         return None
#     return resultdef

def get_object(bucket_name, key):
    try:
        s3_client = boto3.client('s3')
        result = s3_client.get_object(Bucket=bucket_name, Key=key)
    except ClientError as e:
        logging.error(e)
        return None
    return result


def put_object(bucket_name, key, value):
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=value)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_file(bucket_name, directory, filename, user):
    try:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=bucket_name, Key=directory, Body=filename, ACL='authenticated-read', Metadata={user: user})

    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_objects(bucket_name, name):
    try:
        s3_client = boto3.client('s3')
        result = s3_client.list_objects(Bucket=bucket_name, Prefix=name)
        # list = list_objects('au.zt.image-gallery', 'dog')['Contents']
        list = result['Contents']
        endpoint = "https://s3-us-west-1.amazonaws.com/au.zt.image-gallery/"
        images = []
        for i in list:
            images.append(endpoint + i['Key'])
    except ClientError as e:
        logging.error(e)
        return None
    return images


def create_presigned_url(bucket_name, object_name, expiration=3600):
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name,
                                                                          'Key': object_name}, ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def get_url(bucket_name, object_name):
    url = create_presigned_url(bucket_name, object_name)
    if url is not None:
        response = requests.get(url)


def main():
    #	create_bucket('au.zt.image-gallery', 'us-west-1')
    put_object('au.zt.image-gallery', 'banana', 'red')
    print(get_object('au.zt.image-gallery', 'dog/IMG_0041.JPG'))
    print(create_presigned_url('au.zt.image-gallery', 'dog/IMG_0041.JPG'))
    upload_file('au.zt.image-gallery', 'dog/', 'CindyP.png', 'dog')
    # print(get_url('au.zt.image-gallery.s3.amazonaws.com', 'dog/IMG_0041.JPG'))
    # list_objects('au.zt.image-gallery', 'dog')pip
    # for e in list_objects('au.zt.image-gallery', 'dog'):
    #     print(e)


if __name__ == '__main__':
    main()
