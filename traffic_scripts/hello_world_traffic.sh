#!/bin/bash

start=$(date +%s)
echo Started at $(date +%H)


#Start at 2 pm
#2am - 6am

echo "First Interval"

while [ $(date "+%H") -lt 10 ]; do
   time curl https://n2tp6ri95a.execute-api.eu-west-2.amazonaws.com/Prod/hello/ 
   wait $(jobs -p)
   echo "Sleep for 1 min" 
   sleep 60
   done  

#Start at 5 pm
#5pm - 9pm

echo "Second Interval"

while [ $(date "+%H") -lt 23 ]; do
   time curl https://n2tp6ri95a.execute-api.eu-west-2.amazonaws.com/Prod/hello/ 
   wait $(jobs -p)
   echo "Sleep for 10 min" 
   sleep 600
   done  


echo Ended at $(date +%H)

end=$(date +%s)
seconds=$(echo "$end - $start" | bc)
echo $seconds' sec'