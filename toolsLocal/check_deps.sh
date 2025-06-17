#!/usr/bin/env zsh

### Farben definieren
GREEN='\033[32m'
BLUE='\033[34m'
RED='\033[31m'
RESET='\033[0m'

### Funktion für das Einfärben von Counts
counttocol() {
    local count=$1
    if (( count <= 3 )); then
        echo -n "$GREEN"
    elif (( count <= 40 )); then
        echo -n "$BLUE"
    else
        echo -n "$RED"
    fi
}

### Funktion zur Paketinfo
pckInfo() {
    local pkg=$1
    local depends_count=$(pactree -u "$pkg" 2>/dev/null | wc -l)
    local depending_count=$(pactree -r "$pkg" 2>/dev/null | wc -l)
    local depends_color=$(counttocol "$depends_count")
    local depending_color=$(counttocol "$depending_count")
    return "$pkg ${depends_color}$depends_count ${depending_color}$depending_count${RESET}"
}

### Main: Pakete mit Updates prüfen
updates=( ${(f)"$(checkupdates 2>/dev/null)"} )
echo -e "$updates"

for update in $updates; do
    pkg=${update%% *}  # Paketname extrahieren
    
    list="$list $pckInfo $pkg"
done
echo -e "$list"
