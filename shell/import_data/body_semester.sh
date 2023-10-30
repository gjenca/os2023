#!/bin/bash
cut -c 3- |
while read PRIEZVISKO MENO BODY
do
	echo "$BODY"
done | grep -v '^None$' |
(
NUM=0
SUM=0
while read BODY
do
	let NUM=NUM+1
	let SUM=SUM+BODY
done
echo "$SUM/$NUM" | bc -l
)	

