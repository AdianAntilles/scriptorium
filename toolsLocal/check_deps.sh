#!/usr/bin/env zsh

# Farben laden
autoload -U colors && colors
GREEN=$colors[green]
BLUE=$colors[blue]
RED=$colors[red]
RESET=$colors[reset]

# Pakete mit Updates holen
updates=( ${(f)"$(checkupdates)"} )

# Ausgabe vorbereiten
for update in $updates; do
    pkg=${update%% *}  # Paketname extrahieren
    depends_count=$(pactree -u "$pkg" 2>/dev/null | wc -l)
    
    # Farblogik
    if (( depends_count <= 3 )); then
        color=$GREEN
    elif (( depends_count <= 10 )); then
        color=$BLUE
    else
        color=$RED
    fi

    echo -e "${color}${pkg} - ${depends_count} Abhängigkeiten${RESET}"
done
