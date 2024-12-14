#!/bin/env sh

temp_list=./file_hashes_with_size.txt
sort_list=./sorted_files.txt
dupe_list=./duplicate_files.txt

#make list of files, md5sum path 
find $1 -type f | xargs -P 8 -I {} md5sum "{}" >> $temp_list

# sort the list
sort $temp_list >> $sort_list
 
# find duped entries
awk '{if (seen[$1]++) print $2}' $sorted_list >> $dupe_list

echo "done"
