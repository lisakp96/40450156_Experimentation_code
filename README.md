# MASTER PROJECT

This project contains code for the investigation of traffic on AWS Lambda.

The Master Branch contains the raw github repositories of both the faas_measure-master and traffic scripts.

The sam-app Folder contains the hello-world lamdba function. The SAM CLI integrates a seperate README containing information on how to deploy the code. The function has been build and deployed accordingly, adding the --region eu-west-2 flag to deploy in the AWS London Region. 

###########################################################################

```bash
cd faas_measure-master
python *_test.py
```

Add Credentals in config.py to give permission to access AWS. 

Variable settings such as sleep_tm, thread_no, runtime language and memory can be taken from the test files directly. 
In code/python/index.py, adjustments to integrate the fileupload stream are in L. 15, and L. 73-88, with the public IP and Region environment variables set to be able those settings in the Logs and better track experimentation. 

###########################################################################

```bash
cd traffic scripts
./*traffic*.sh
```
The Code to add the S3 payload is intgrated in L.46-53
Variable Settings are as follows:

The Json Payload to test the fileupload Lambda Handler 

```bash
{
    "content": "c2FtcGxlIHRleHQ="
}
```

The Command to access the API Gatway with an example .txt file as payload:  

```bash
curl --request POST -H "Content-Type: application/txt" --data-binary "@/Users/lisamuller/Desktop/analysis_R/tmp_1.txt" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload
```


The Lambda Handler for the fileupload stream as deployed on AWS (see: lamdba_function.py and the fileUploadApi.yaml file): 

```bash
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

    ```

###########################################################################

```bash
cd ip_locations
node index.js
```

Add Access Key in index.js to start code. 

###########################################################################
>>>>>>> origin/fileupload_measurement
