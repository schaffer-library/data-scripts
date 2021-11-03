 #!/bin/bash

# To run this: 'sh fileqc.sh path/to/input-directory'
# Prints .csv output to the directory you run the script from 
c=1
IPATH=$1
PATHNAME="$(basename -- $IPATH)"
NUMFILES="$(ls $IPATH | wc -l | xargs echo -n)"
echo "filename", "mimetype", "size", "dimensions", "bits", "color", "dpi" > "$PATHNAME.csv"
for i in $(find $IPATH \( -name "*.tiff" -o -name "*.tif" -o -name "*.jpg" \));
do
	echo "Processing $c of $NUMFILES files"
	f="$(basename -- $i)"
	mime="$(exiftool -p '$MimeType' $i)" 
	size="$(exiftool -p '$FileSize' $i)"
	dimensions="$(exiftool -p '$ImageSize' $i)"
	bits="$(exiftool -p '$BitsPerSample' $i)"
	dpi="$(exiftool -p '$XResolution;$YResolution' $i)"
	color="$(exiftool -p '$ColorSpaceData' $i)"
	echo "$f," "$mime", "$size", "$dimensions", "$bits", "$color", "$dpi"  >> "$PATHNAME.csv"
	let c=c+1
done;

