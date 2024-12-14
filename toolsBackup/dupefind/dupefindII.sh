#!/bin/env sh

temp_list=./file_hashes_with_size.txt
sort_list=./sorted_files.txt
dupe_list=./duplicate_files.txt

# Liste der Dateien mit MD5-Hash und Nullbyte-getrennten Pfaden erstellen
find "$1" -type f -print0 | xargs -0 -P 8 -I {} md5sum -z "{}" | echo "{} " >> "$temp_list"

# Sortierte Liste der Dateien erstellen und anhängen
sort -z "$temp_list" > "$sort_list"

# Doppelte Einträge finden und anhängen
awk -v RS='\0' '{if (seen[$1]++) print $2}' "$sort_list" > "$dupe_list"

echo "done"

