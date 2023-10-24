#!/bin/bash
mkdir mini 2>/dev/null 
cat <<THE_END
<html>
<body>
<h1>galeria</h1>
<ul>
THE_END
for IMG in "$@"
do
	PNG=$(echo "$IMG" | sed 's/jpg$/png/' )
	convert -resize '10%' "$IMG" "mini/$PNG"
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
