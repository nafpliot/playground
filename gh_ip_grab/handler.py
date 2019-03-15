from __future__ import print_function
import urllib
import json
import datetime
import boto3
from botocore.exceptions import ClientError

bucket_name = 'my-ip-bucket-16522'
filename = 'ips.json'
gh_meta_url = "https://api.github.com/meta"

def fetch_data():
    response = urllib.urlopen(gh_meta_url)
    data = json.loads(response.read())
    data.pop('verifiable_password_authentication', None)
    # getting unique ips
    ips = list(set(sum(data.values(), [])))
    timestamp = str(datetime.datetime.utcnow())
    data = [{'timestamp':timestamp, 'ips':ips}]
    return data

def main(event, context):
    s3 = boto3.resource('s3')
    try:
        s3_ips = json.loads(s3.Object(bucket_name, filename).get()["Body"].read())
    except ClientError as e:
        # file does not exist. For others errors raise exception
        if e.response['Error']['Code'] == 'NoSuchKey':
            ips = fetch_data()
            s3.Object(bucket_name, filename).put(Body=json.dumps(ips, indent=4, separators=(',', ': ')))
        else:
            raise e
    else:
        new_ips = fetch_data()
        ips = s3_ips + new_ips
        s3.Object(bucket_name, filename).put(Body=json.dumps(ips, indent=4, separators=(',', ': ')))
