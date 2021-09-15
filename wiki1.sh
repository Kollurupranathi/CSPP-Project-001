for i in {1992..2014}
do
url=https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_$i
curl $url | grep '<td><a' | sed 's|> featuring <|>\n<|g' | sed 's|>, <|>\n<|g' | sed 's|> and <|>\n<|g' | sed 's|a>.*<a|a>\n<a|g' | sed 's|<\/a>.*|<\/a>|' | sed 's| class\=\"mw\-redirect\" | |' | sed 's|<td><a|<a|' | sed 's|<a href\=\"|https://en.wikipedia.org|' | sed 's|\" title\=\"|\t|' | sed 's|">.*</a>||' >> allUrls.tsv
done
