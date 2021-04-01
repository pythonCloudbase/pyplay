sanitise.sh dowsnot work

## Possible methods

1. use pyPDF to remove all the links after extracting the text.
2. use some shell script to run and do manually
3. use pypdftk
4. sed '/Link/d' < file.pdf > file-without-links.pdf - works