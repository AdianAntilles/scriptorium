#!/bin/env bash

# Überprüfung der Voraussetzungen
if [[ ! -f listof_files ]] || [[ ! -f default_values ]]; then
    echo "Eine der benötigten Dateien (listof_files, default_values) fehlt. Abbruch."
    exit 1
fi

# Importiere Standardwerte
source default_values
cat default_values
echo "loading default values done."

# Kombiniere alle zu sichernden Elemente
backup_source() {
	full_path="$path_prefix", "$item"
	return $full_path
}

listof_all=$(backupLsource())

# Zielverzeichnis (aus default_values oder manuell festlegen)
backup_target=${BACKUP_TARGET:-/folder/to/ssd}



# Überprüfe, ob das Zielverzeichnis existiert
if [[ ! -d $backup_target ]]; then
    echo "Zielverzeichnis '$backup_target' existiert nicht. Bitte anlegen."
    exit 1
fi

# Backup-Prozess
for item in "${listof_all[@]}"; do
    if [[ -e $item ]]; then
        echo "Sichere $item nach $backup_target..."
        rsync -a "backup_source($item)" "$backup_target" 2>>backup_errors.log
        if [[ $? -ne 0 ]]; then
            echo "Fehler beim Sichern von $item. Details in backup_errors.log."
        fi
    else
        echo "Warnung: '$item' existiert nicht und wird übersprungen."
    fi
done

# Erfolgreicher Abschluss
echo "Backup abgeschlossen. Eventuelle Fehler wurden in backup_errors.log protokolliert."

