#!/bin/bash
for A in $(seq 10)
do
	for B in $(seq 10)
	do
		echo "$A*$B=" $(echo "$A*$B" | bc)
	done
done

