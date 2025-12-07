# -*- coding: utf-8 -*-
import ast

with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Test line 22 (index 21)
print("Testing line 22...")
line = lines[21].strip()
print(f"Line length: {len(line)} characters")
print(f"First 200 chars: {line[:200]}")
print(f"Last 200 chars: {line[-200:]}")

# Find where bare commas are
bare_commas = []
i = 0
while i < len(line):
    if line[i:i+2] == ',,':
        bare_commas.append(i)
        i += 2
    else:
        i += 1

if bare_commas:
    print(f"\nFound {len(bare_commas)} instances of bare commas (,,) at positions: {bare_commas[:10]}")
else:
    print("\nNo bare commas found")

# Try to parse it
try:
    ast.literal_eval(line)
    print("\n✓ Line 22 parses successfully!")
except SyntaxError as e:
    print(f"\n✗ Syntax error: {e}")
    print(f"Error at position: {e.offset}")
    if e.offset:
        start = max(0, e.offset - 50)
        end = min(len(line), e.offset + 50)
        print(f"Context: ...{line[start:end]}...")
