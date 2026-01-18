#!/usr/bin/env python3
import os
import re

# Read the topic list
with open('topics/topic_list.txt', 'r') as f:
    topics = f.readlines()

# Parse topics into a dictionary
topic_dict = {}
for line in topics:
    line = line.strip()
    if line:
        match = re.match(r'^(\d+)\.\s+(.+)$', line)
        if match:
            num = int(match.group(1))
            name = match.group(2)
            topic_dict[num] = name

# Get existing test folders
existing = set()
for folder in os.listdir('tests'):
    match = re.match(r'^(\d+)_', folder)
    if match:
        existing.add(int(match.group(1)))

# Find missing topics
missing = []
for num in sorted(topic_dict.keys()):
    if num not in existing:
        missing.append((num, topic_dict[num]))

print(f"Total topics: {len(topic_dict)}")
print(f"Existing tests: {len(existing)}")
print(f"Missing tests: {len(missing)}")
print("\nMissing topics:")
for num, name in missing:
    print(f"{num}. {name}")
