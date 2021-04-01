mkdir temp
cd temp
pdftk ../demo.pdf burst
pdftk *.pdf cat output ../filewithlinksRemoved.pdf