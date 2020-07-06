import logging
import boto3
import json
from PIL import Image
from io import BytesIO
import numpy as np
from botocore.exceptions import ClientError


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
        file_stream = result['Body']
        im = Image.open(file_stream)
    except ClientError as e:
        logging.error(e)
        return None
    return im


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
        s3_client.put_object(Bucket=bucket_name, Key=directory, Body=filename, Metadata={user: user})

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


def main():
    #	create_bucket('au.zt.image-gallery', 'us-west-1')
    put_object('au.zt.image-gallery', 'banana', 'red')
    print(get_object('au.zt.image-gallery', 'dog/IMG_0041.JPG'))


    # list_objects('au.zt.image-gallery', 'dog')
    for e in list_objects('au.zt.image-gallery', 'dog'):
        print(e)


if __name__ == '__main__':
    main()
