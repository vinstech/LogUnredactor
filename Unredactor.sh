#!/bin/bash

read -p "Enter the log file path: " log_file
read -p "Enter the redaction mapping file path: " json_file

python3 -c "import json;
def unredact(log_file, json_file):
    with open(json_file) as f:
        mapping = json.load(f)
    with open(log_file) as f:
        logs = f.readlines()
    unredacted_logs = []
    for log in logs:
        for key, value in mapping.items():
            log = log.replace(key, value)
        unredacted_logs.append(log)
    return unredacted_logs;

logs = unredact('$log_file', '$json_file');
print(''.join(logs))"
