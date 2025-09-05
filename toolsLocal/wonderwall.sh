#!/bin/env sh

files=(~/Bilder/Wallpaper/*)

while true; do
	randomfile="$(files[RANDOM % $(files[@])])"
	echo file://$randomfile

	gsettings set org.gnome.desktop.background picture-uri "file://$randomfile"
	DELAY=$((RANDOM % 42))
	sleep $DELAY
done
