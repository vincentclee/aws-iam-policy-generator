#!/usr/bin/env python3

"""
generator.py
============
python script to generate minified AWS IAM policies from a list of all known IAM actions
Intended to be run under Python >= 3.7
"""

import argparse
import json
import sys


# argparse
parser = argparse.ArgumentParser(description="NOFORN Presents: AWS IAM Policy Generator")
parser.add_argument("-s", "--services",
                    dest="services",
                    help="The command separated list of AWS Services by their service prefix.",
                    required=True)
args = parser.parse_args()

services = args.services.split(",")
actions = {}

# open file with all AWS IAM Statement Actions
for line in open("files/all-actions.txt", "r"):
    # action
    action = line.strip()
    
    # line check
    if not action:
        continue
    
    # service
    service = action.rpartition(":")[0]
    
    # add shortened action to set inside a dictionary
    if service not in actions:
        actions[service] = set()
    actions[service].add(action[0:action.find(":") + 2] + "*")

# open JSON file with blank policy
with open("files/template.json", "r") as file:
    policy = json.load(file)

# add all Actions from selected Services to the policy
services = sorted(services)
for service in services:
    try:
        _actions = sorted(actions[service])
    except KeyError:
        print("Error: IAM Actions are missing for the service: " + service)
        raise
    policy["Statement"][0]["Action"].extend(list(_actions))

# Serialize JSON
json_object = json.dumps(policy, indent=4)

# Write policy to policy.json
with open("policy.json", "w") as file:
    file.write(json_object)

print("Great Success")
print("AWS IAM policy generated: policy.json")
