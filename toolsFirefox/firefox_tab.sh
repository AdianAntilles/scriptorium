#!/bin/zsh

# Variablen
PROFILE_DIR=~/.mozilla/firefox/87syjf8o.default-release # Hier ein Catchall finden.
SESSION_FILE="$PROFILE_DIR/sessionstore-backups/recovery.jsonlz4"
TLD="scryfall"
OUTPUT_FILE="$HOME/Programme/firefox_tabs_de.txt"

# Session-Daten dekodieren und URLs extrahieren
~/Programme/firefox_tab.py "$SESSION_FILE" | jq -r '.windows[].tabs[].entries[-1].url' | grep -E "$TLD" > "$OUTPUT_FILE"

echo "Alle URLs mit $TLD wurden in $OUTPUT_FILE geschrieben."

