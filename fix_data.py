# -*- coding: utf-8 -*-
"""
Script to remove # from data lines in data.txt
"""

with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

fixed_lines = []
for i, line in enumerate(lines, 1):
    # Lines 22-32 should have the # removed if they start with "# ["
    if 22 <= i <= 32 and line.startswith('# ['):
        # Remove the "# " from the beginning
        fixed_lines.append(line[2:])
        print(f"Fixed line {i}")
    else:
        fixed_lines.append(line)

with open('data.txt', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("\nDone! data.txt has been fixed.")
print("Now restart your Flask app: python app.py")
