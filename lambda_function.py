import json
import base64
import boto3
import os
import urllib3

#######

import time
import socket
import sys
import uuid
import subprocess

try:
    import urllib2
    from urllib2 import urlopen
except BaseException:
    from urllib.request import urlopen

import decimal

INST_PRIV_IP_DST = "8.8.8.8"

########

BUCKET_NAME = 's3fileuploadmuellerl'


def lambda_handler(event, context):
    
    buf = open('/proc/meminfo').read()
    buf = ','.join([v.replace(' ', '') for v in
                    buf.split('\n') if v])
    print(buf)
    
    buf = "".join(open("/proc/cpuinfo").readlines())
    cpuinfo = buf.replace("\n", ";").replace("\t", "")
    print (cpuinfo)
    
    uptime = ','.join(open('/proc/uptime').read().strip('\n').split(' '))
    print(uptime)
    
    vm_private_ip = socket.gethostbyname(socket.getfqdn())
    print(vm_private_ip)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((INST_PRIV_IP_DST, 80))
    instance_private_ip = s.getsockname()[0]
    s.close()
    print(instance_private_ip)
    
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://checkip.amazonaws.com')
    print(r.data) 

    region = os.environ['AWS_REGION']
    print(region)  
    
    file_content = base64.b64decode(event['content'])
    file_path = 'sample.txt'
    s3 = boto3.client('s3')
    
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        raise IOError(e)
    return {
        'statusCode': 200,
        'body': {
            'file_path': file_path
        }
    }