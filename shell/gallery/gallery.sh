#!/bin/bash
HEADER=Gallery
PERC=10
while true
do
	if [ "$1" == -t ]
	then
		HEADER="$2"
		shift 2
		continue
	
	elif [ "$1" == -p ]
	then
		PERC="$2"
		shift 2
		continue
	
	else
		break
	fi
done
mkdir mini 2>/dev/null 
cat <<THE_END
<html>
<body>
<h1>$HEADER</h1>
<ul>
THE_END
for IMG in "$@"
do
	PNG=$(echo "$IMG" | sed 's/jpg$/png/' )
	convert -resize "$PERC%" "$IMG" "mini/$PNG"
	echo '<li>'
	echo '<a href="'"$IMG"'">'
	echo '<img src="mini/'"$PNG"'">'
	echo '</a>'
	echo '</li>'
done
cat <<THE_END
</ul>
</body>
</html>
THE_END
