#!/bin/env python

import os
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from collections import defaultdict

def calculate_hash(filepath, block_size=65536):
    """Berechnet den SHA256-Hash einer Datei."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                hasher.update(block)
    except (OSError, IOError):
        return None  # Datei kann nicht gelesen werden
    return hasher.hexdigest()

def scan_files(directory):
    """Findet alle Dateien im Verzeichnisbaum."""
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def process_file(file):
    """Berechnet die Dateigröße und den Hash."""
    try:
        size = os.path.getsize(file)
        file_hash = calculate_hash(file)
        return (size, file_hash, file)
    except Exception as e:
        return None  # Fehlerhafte Datei ignorieren

def main(directory, num_threads=4):
    """Hauptprogramm zur parallelen Verarbeitung."""
    hash_dict = defaultdict(list)
    total_size = 0
    duplicates = []

    # Dateien scannen
    files = list(scan_files(directory))
    print(f"Scanne {len(files)} Dateien im Verzeichnis {directory}...")

    # Multithreading zur Verarbeitung von Dateien
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_file = {executor.submit(process_file, file): file for file in files}
        for future in tqdm(as_completed(future_to_file), total=len(future_to_file)):
            result = future.result()
            if result:
                size, file_hash, file = result
                if file_hash in hash_dict:
                    duplicates.append((size, file_hash, hash_dict[file_hash][0], file))
                    total_size += size
                else:
                    hash_dict[file_hash].append(file)

    # Ergebnisse anzeigen
    print("\nDuplikate gefunden:")
    for dup in duplicates:
        size, file_hash, original, duplicate = dup
        print(f"Größe: {size} Bytes | Hash: {file_hash}")
        print(f"Original: {original}")
        print(f"Duplikat: {duplicate}\n")

    print(f"Gesamtgröße der Duplikate: {total_size} Bytes")
    return duplicates

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Find and list duplicate files.")
    parser.add_argument("directory", help="Directory to scan for duplicate files.")
    parser.add_argument("--threads", type=int, default=4, help="Number of threads to use.")
    args = parser.parse_args()

    main(args.directory, args.threads)

