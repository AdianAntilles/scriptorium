#!/usr/bin/env python3
import lz4.block
import json
import sys

def walk_files(path_list):
	with open(list_path, 'rb') as list:
		

def decode_lz4(file_path):
    with open(file_path, 'rb') as file:
        # Überspringe die ersten 8 Bytes (Header)
        file.read(8)
        compressed_data = file.read()
        return lz4.block.decompress(compressed_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lz4_reader.py <path_to_lz4_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        data = decode_lz4(file_path)
        # Lade als JSON für bessere Lesbarkeit
        json_data = json.loads(data)
        print(json.dumps(json_data, indent=2))
    except Exception as e:
        print(f"Error: {e}")
        
