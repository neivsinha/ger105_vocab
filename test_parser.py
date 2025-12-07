# -*- coding: utf-8 -*-
"""
Test script to debug data parsing
"""

with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read().strip()

print("=== CHECKING FILE CONTENT ===")
print(f"File starts with: {content[:100]}")
print(f"\nFile starts with '# INSTRUCTIONS': {content.startswith('# INSTRUCTIONS')}")

# Split by lines and get non-empty, non-comment lines
lines = [line.strip() for line in content.split('\n')
        if line.strip() and not line.strip().startswith('#')]

print(f"\n=== NON-COMMENT LINES FOUND ===")
print(f"Number of non-comment lines: {len(lines)}")

if len(lines) > 0:
    print(f"\nFirst line preview (first 100 chars):")
    print(lines[0][:100])
    print(f"\nSecond line preview (first 100 chars):")
    if len(lines) > 1:
        print(lines[1][:100])
    print(f"\nThird line preview (first 100 chars):")
    if len(lines) > 2:
        print(lines[2][:100])
else:
    print("ERROR: No data lines found!")
    print("\nShowing first 40 lines of file:")
    for i, line in enumerate(content.split('\n')[:40], 1):
        print(f"{i:3}: {line[:80]}")
