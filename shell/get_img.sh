#!/bin/bash

if [ "$#" != 1 ]
then
	echo "Usage: $0 URL"
	exit 1
fi

curl -s "$1" | 
#    Stiahne obsah z URL, da na stdout
tr -d '\n' | 
#    Zmaze newline
tr '<' '\n' | 
#    Nahradi < newline
grep '^img ' |
#    Vyhlada img
sed 's/.*src="\([^"]*\)".*/\1/' |
# Vyfiltruje hodnotu src atributu z kazdeho riadku
sed "s#^#$1#"
# Da spravny prefix, aby sa dobre dalej spracovalo

