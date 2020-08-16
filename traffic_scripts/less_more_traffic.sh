#!/bin/bash

start=$(date +%s)
echo Started at $(date +%H)

echo "First Interval"

# true though ?
while [ $(date "+%H") -lt 24 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   echo "Sleep for 5 min" 
   sleep 5m
   done  


echo "Second Interval"

while [ $(date "+%H") -lt 24 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   echo "Sleep for 12 min" 
   sleep 12m
   done  

echo Ended at $(date +%H)
