#!/usr/bin/env python3
import os
import re
import argparse

def find_api_key_in_file(manifest_file):
    meta_data_pattern = re.compile(r'(?s)<meta-data\s+.*?>', re.IGNORECASE)
    name_pattern = re.compile(r'android:name\s*=\s*[\'"]([^\'"]*api_key[^\'"]*)[\'"]', re.IGNORECASE)
    value_pattern = re.compile(r'android:value\s*=\s*[\'"]([^\'"]+)[\'"]', re.IGNORECASE)
    if not os.path.isfile(manifest_file):
        return
    try:
        with open(manifest_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        for match_tag in meta_data_pattern.finditer(content):
            tag = match_tag.group(0)
            nm = name_pattern.search(tag)
            vm = value_pattern.search(tag)
            if nm and vm:
                key_name = nm.group(1)
                key_value = vm.group(1)
                start_pos = match_tag.start()
                line_number = content.count('\n', 0, start_pos) + 1
                print(f"[API-KEY] {manifest_file} - line {line_number} => Name: {key_name} | Value: {key_value}")
    except:
        pass

def find_api_key_in_manifest(folder):
    meta_data_pattern = re.compile(r'(?s)<meta-data\s+.*?>', re.IGNORECASE)
    name_pattern = re.compile(r'android:name\s*=\s*[\'"]([^\'"]*api_key[^\'"]*)[\'"]', re.IGNORECASE)
    value_pattern = re.compile(r'android:value\s*=\s*[\'"]([^\'"]+)[\'"]', re.IGNORECASE)
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.lower() == "androidmanifest.xml":
                path_file = os.path.join(root, filename)
                try:
                    with open(path_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    for match_tag in meta_data_pattern.finditer(content):
                        tag = match_tag.group(0)
                        nm = name_pattern.search(tag)
                        vm = value_pattern.search(tag)
                        if nm and vm:
                            key_name = nm.group(1)
                            key_value = vm.group(1)
                            start_pos = match_tag.start()
                            line_number = content.count('\n', 0, start_pos) + 1
                            print(f"[FOUND][API-KEY] {path_file} - line {line_number} => Name: {key_name} | Value: {key_value}")
                except:
                    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find API KEY in AndroidManifest.xml (case-insensitive for 'api_key')")
    parser.add_argument("-d", "--directory", help="Folder to scan")
    parser.add_argument("-f", "--file", help="Single AndroidManifest.xml file to check")
    args = parser.parse_args()

    if args.directory:
        find_api_key_in_manifest(args.directory)
    if args.file:
        find_api_key_in_file(args.file)
