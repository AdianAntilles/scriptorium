#!/bin/bash

# Arbeitsverzeichnis (ändern nach Bedarf)
WORKDIR='/run/media/mo/TOSHIBA EXT'

# Temporäre Datei für Hashes und Ergebnisse
HASHFILE="/home/mo/Programme/file_hashes_with_size.txt"
DUPLICATES="/home/mo/Programme/duplicate_files.txt"

# Schritt 1: Alle Dateien mit Hash und Größe sammeln
find "$WORKDIR" -type f -exec sh -c 'printf "\047%s\047,\047%s\047,\047%s\047\n" "$(stat --printf="%s" "{}")" "$(md5sum "{}" | awk "{print \$1}")" "{}"' \; > "$HASHFILE"


# Schritt 2: Duplikate finden und in eine Liste schreiben
awk -F"," '{
    gsub(/\047/, "", $1); size=$1;
    gsub(/\047/, "", $2); hash=$2;
    gsub(/\047/, "", $3); file=$3;
    if (seen[hash]) {
        print size, hash, seen[hash], file;
        total += size;
    } else {
        seen[hash]=file;
    }
} END { print "Gesamtgröße der Duplikate: " total " Bytes" }' "$HASHFILE" > "$DUPLICATES"

echo "Operationen fertig."
