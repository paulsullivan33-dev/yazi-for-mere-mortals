#!/bin/sh
rm -rf ops
mkdir -p ops/archive
printf 'Dear Sam,\n\nThank you for the seedlings.\n' > ops/draft-letter.txt
printf 'row,length\n1,12\n2,9\n' > ops/measurements.csv
printf 'Old notes, kept just in case.\n' > ops/old-notes.txt
