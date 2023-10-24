#!/bin/bash
for N in $(seq 2 100)
do
	MAX=$(echo "sqrt($N)" | bc)
	PRIME=1
	for D in $(seq 2 "$MAX")
	do
		if test $(echo "$N%$D" | bc) = 0
		then
			PRIME=0
			break
		fi
	done
	if [ "$PRIME" = 1 ] ; then
		echo $N
	fi
done

