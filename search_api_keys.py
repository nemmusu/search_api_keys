#!/usr/bin/env python3
import os
import re
import argparse

def extract_api_keys(content):
    meta_data_pattern = re.compile(r'(?s)<meta-data\s+.*?>', re.IGNORECASE)
    name_pattern = re.compile(r'android:name\s*=\s*[\'"]([^\'"]*api_key[^\'"]*)[\'"]', re.IGNORECASE)
    value_pattern = re.compile(r'android:value\s*=\s*[\'"]([^\'"]+)[\'"]', re.IGNORECASE)
    results = []
    
    for match_tag in meta_data_pattern.finditer(content):
        tag = match_tag.group(0)
        nm = name_pattern.search(tag)
        vm = value_pattern.search(tag)
        if nm and vm:
            key_name = nm.group(1)
            key_value = vm.group(1)
            start_pos = match_tag.start()
            line_number = content.count('\n', 0, start_pos) + 1
            results.append((line_number, key_name, key_value))
    return results

def process_file(manifest_file):
    if not os.path.isfile(manifest_file):
        print(f"File not found: {manifest_file}")
        return
    try:
        with open(manifest_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        api_keys = extract_api_keys(content)
        for line_number, key_name, key_value in api_keys:
            print(f"[API-KEY] {manifest_file} - line {line_number} => Name: {key_name} | Value: {key_value}")
    except Exception as e:
        print(f"Error processing file {manifest_file}: {e}")

def scan_directory(folder):
    for root, _, files in os.walk(folder):
        for filename in files:
            if filename.lower() == "androidmanifest.xml":
                path_file = os.path.join(root, filename)
                process_file(path_file)

def main():
    parser = argparse.ArgumentParser(description="Search for API keys in AndroidManifest.xml files (case-insensitive for 'api_key').")
    parser.add_argument("-d", "--directory", help="Folder to scan")
    parser.add_argument("-f", "--file", help="Single AndroidManifest.xml file to check")
    args = parser.parse_args()

    if args.directory:
        scan_directory(args.directory)
    if args.file:
        process_file(args.file)

if __name__ == "__main__":
    main()
