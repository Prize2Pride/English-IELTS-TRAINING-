#!/usr/bin/env python3
import os
import re
import json

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
        missing.append({"num": num, "name": topic_dict[num]})

# Save to JSON file
with open('missing_topics.json', 'w') as f:
    json.dump(missing, f, indent=2)

print(f"Saved {len(missing)} missing topics to missing_topics.json")

# Also print first 50 for reference
print("\nFirst 50 missing topics:")
for item in missing[:50]:
    print(f"{item['num']}. {item['name']}")
