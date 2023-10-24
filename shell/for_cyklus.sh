#!/bin/bash
for VAR in a b 1 slon
do
	echo "VAR=$VAR"
done
echo '*************************'
for N in $(seq 10)
do
	echo "N=$N"
done
echo '*************************'
for FNM in *.sh
do
	echo 'skript:' "$FNM"
done

