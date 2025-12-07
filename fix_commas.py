# -*- coding: utf-8 -*-
"""
Fix bare commas in data.txt
"""
import re

with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix bare commas - replace sequences of commas with properly formatted empty strings
# Pattern: ,, becomes ,"",
def fix_line(line):
    # Keep replacing ,, with ,"", until no more ,, exist
    while ',,' in line:
        line = line.replace(',,', ',"",')
    return line

lines = content.split('\n')
fixed_lines = []

for i, line in enumerate(lines, 1):
    if 22 <= i <= 32:  # Data lines
        fixed = fix_line(line)
        if fixed != line:
            print(f"Fixed line {i}")
        fixed_lines.append(fixed)
    else:
        fixed_lines.append(line)

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(fixed_lines))

print("\nDone! All bare commas have been fixed.")
print("Now restart your Flask app: source venv/bin/activate && python app.py")
