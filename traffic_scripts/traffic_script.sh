#!/bin/bash

start=$(date +%s)
echo Started at $(date +%H)

#Start at 6 am

echo "First Interval"

while [ $(date "+%H") -lt 8 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 300))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  

#Start at 8 am (continue)

echo "Second Interval"

while [ $(date "+%H") -lt 10 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 240))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  

#Start at 10 am (continue)

echo "Third Interval"

while [ $(date "+%H") -lt 14 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 180))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  

#Start at 2 pm (continue)

echo "Fourth Interval"

while [ $(date "+%H") -lt 18 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 120))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  

#Start at 6 pm (continue)

echo "Fifth Interval"

while [ $(date "+%H") -lt 22 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 60))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  

#Start at 10 pm (continue)

echo "Sixth Interval"

while [ $(date "+%H") -lt 24 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 600))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  

#Start at 0 am

while [ $(date "+%H") -lt 6 ]; do
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload &
   time curl --request POST -H "Content-Type: application/txt" --data-binary "c2FtcGxlIHRleHQ=" https://d8uc7y7gc4.execute-api.us-east-1.amazonaws.com/v1/upload 
   wait $(jobs -p)
   pause=$((1 + RANDOM % 600))
   echo "Sleep for $pause sec" 
   sleep $pause
   done  


echo Ended at $(date +%H)

