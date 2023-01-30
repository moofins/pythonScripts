#!/bin/bash

num=0
check='Incorrect Try Harder'

for i in {0..1000000}
do
	response="$(printf $i | ./try-harder)"
	if [[ "$response" == *"$check"* ]]	#this line isnt working for whatever reason. need some flavor of response.find
	then
		if [ $(expr $i % 1000) == "0" ]
		then
			echo "progress: $i"
		else
			continue
		fi
		continue
	else
		echo "$i"
	fi
done