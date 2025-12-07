# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import ast
import random
import os

app = Flask(__name__)

# Global variable to store vocabulary data
vocabulary_data = []
last_indices = []
MAX_HISTORY = 20

def parse_data_file():
    """Parse the data.txt file and create vocabulary entries."""
    global vocabulary_data
    vocabulary_data = []

    data_file = 'data.txt'
    if not os.path.exists(data_file):
        print(f"Warning: {data_file} not found. Creating template file.")
        create_template_file()
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    if not content:
        print("data.txt is empty. Please add your vocabulary data.")
        return

    try:
        # Split by lines and get non-empty, non-comment lines
        lines = [line.strip() for line in content.split('\n')
                if line.strip() and not line.strip().startswith('#')]

        if len(lines) == 0:
            print("data.txt contains only comments. Please add your vocabulary data.")
            return

        if len(lines) < 11:
            print(f"Error: Expected 11 lists, but found {len(lines)}")
            return

        # Parse each line as a Python list
        articles = ast.literal_eval(lines[0])
        reflexivity = ast.literal_eval(lines[1])
        words = ast.literal_eval(lines[2])
        plural_endings = ast.literal_eval(lines[3])
        noun_declination = ast.literal_eval(lines[4])
        present_conjugation = ast.literal_eval(lines[5])
        verb_type = ast.literal_eval(lines[6])
        simple_past = ast.literal_eval(lines[7])
        helping_verb = ast.literal_eval(lines[8])
        past_participle = ast.literal_eval(lines[9])
        definitions = ast.literal_eval(lines[10])

        # Verify all lists have the same length
        list_lengths = [len(articles), len(reflexivity), len(words), len(plural_endings),
                       len(noun_declination), len(present_conjugation), len(verb_type),
                       len(simple_past), len(helping_verb), len(past_participle), len(definitions)]

        if len(set(list_lengths)) != 1:
            print(f"Error: Lists have different lengths: {list_lengths}")
            return

        # Combine into vocabulary entries
        for i in range(len(words)):
            entry = {
                'article': articles[i],
                'reflexivity': reflexivity[i],
                'word': words[i],
                'plural_ending': plural_endings[i],
                'noun_declination': noun_declination[i],
                'present_conjugation': present_conjugation[i],
                'verb_type': verb_type[i],
                'simple_past': simple_past[i],
                'helping_verb': helping_verb[i],
                'past_participle': past_participle[i],
                'definition': definitions[i]
            }
            vocabulary_data.append(entry)

        print(f"Successfully loaded {len(vocabulary_data)} vocabulary entries.")

    except Exception as e:
        print(f"Error parsing data.txt: {e}")
        return

def create_template_file():
    """Create a template data.txt file with instructions."""
    template = """# INSTRUCTIONS FOR data.txt
#
# Paste your 11 comma-separated lists below (one per line).
# Each list should be in Python list format: ["item1", "item2", "item3", ...]
# Include empty entries as "" where needed.
# All 11 lists must have the same number of entries (e.g., 400 items each).
#
# The 11 lists in order are:
# 1. Articles (der/die/das)
# 2. Reflexivity
# 3. Words (German vocabulary)
# 4. Plural endings
# 5. Noun declination
# 6. Present conjugation
# 7. Verb type
# 8. Simple past
# 9. Helping verb
# 10. Past participle
# 11. Definition (English)
#
# Example format (remove these example lines and paste your actual data):
# ["der", "die", "das", ...]
# ["", "sich", "", ...]
# ["Hund", "waschen", "Katze", ...]
# ["e", "", "n", ...]
# ["", "", "", ...]
# ["", "waescht", "", ...]
# ["", "strong", "", ...]
# ["", "wusch", "", ...]
# ["", "haben", "", ...]
# ["", "gewaschen", "", ...]
# ["dog", "to wash", "cat", ...]
"""
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write(template)
    print("Created template data.txt file.")

def get_random_entry():
    """Get a random vocabulary entry, avoiding recent repeats."""
    global last_indices

    if not vocabulary_data:
        return None

    if len(vocabulary_data) <= MAX_HISTORY:
        # If we have fewer entries than history, just pick random
        index = random.randint(0, len(vocabulary_data) - 1)
    else:
        # Pick an index not in recent history
        available_indices = [i for i in range(len(vocabulary_data)) if i not in last_indices]
        if not available_indices:
            # Reset history if we've exhausted all options
            last_indices = []
            available_indices = list(range(len(vocabulary_data)))

        index = random.choice(available_indices)

    # Update history
    last_indices.append(index)
    if len(last_indices) > MAX_HISTORY:
        last_indices.pop(0)

    return vocabulary_data[index]

@app.route('/')
def index():
    """Render the main quiz page."""
    return render_template('index.html')

@app.route('/api/random-entry')
def random_entry():
    """Get a random vocabulary entry."""
    entry = get_random_entry()
    if entry:
        return jsonify(entry)
    else:
        return jsonify({'error': 'No vocabulary data loaded'}), 404

@app.route('/api/stats')
def stats():
    """Get statistics about loaded vocabulary."""
    return jsonify({
        'total_entries': len(vocabulary_data),
        'loaded': len(vocabulary_data) > 0
    })

if __name__ == '__main__':
    parse_data_file()
    app.run(debug=True, port=5001)
