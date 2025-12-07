# German Vocabulary Quiz Application

A modern, responsive Flask web application for studying German vocabulary with interactive quiz modes.

## Features

- **Two Quiz Modes:**
  - **Definition Mode:** Shows an English definition, reveals all German data on click
  - **Word Mode:** Shows a German word, reveals all related information on click

- **Smart Randomization:** Avoids showing the same word repeatedly with a 20-item history buffer
- **Responsive Design:** Works beautifully on desktop, tablet, and mobile devices
- **Clean UI:** Modern interface with smooth animations and clear visual hierarchy
- **Easy Data Management:** Simple text file format for adding your vocabulary

## Setup Instructions

### 1. Install Dependencies

Make sure you have Python 3.7+ installed, then install the required packages:

```bash
pip install -r requirements.txt
```

Or if you're using a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add Your Vocabulary Data

Open the `data.txt` file and paste your 11 comma-separated lists. The file already contains detailed instructions, but here's the format:

```python
["der", "die", "das", ...]  # 1. Articles
["", "sich", "", ...]       # 2. Reflexivity
["Hund", "waschen", ...]    # 3. German words
["e", "", "n", ...]         # 4. Plural endings
["", "", "", ...]           # 5. Noun declination
["", "wäscht", "", ...]     # 6. Present conjugation
["", "strong", "", ...]     # 7. Verb type
["", "wusch", "", ...]      # 8. Simple past
["", "haben", "", ...]      # 9. Helping verb
["", "gewaschen", "", ...]  # 10. Past participle
["dog", "to wash", ...]     # 11. English definitions
```

**Important:**
- Each list must have the same number of entries (e.g., 400 items)
- Use `""` for empty entries
- Each list should be on its own line
- Remove the example/instruction lines before adding your data

### 3. Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

### 4. Using the Quiz

1. **Choose a Mode:** Click either "Definition Mode" or "Word Mode"
2. **Start Quiz:** Click "Next" to load a random vocabulary entry
3. **Study:** Read the prompt and try to recall the information
4. **Reveal:** Click "Reveal Answer" to see all related data
5. **Continue:** Click "Next" to get a new random word

## File Structure

```
german_quiz_program/
├── app.py                  # Flask application and backend logic
├── data.txt               # Your vocabulary data file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Styling and responsive design
    └── js/
        └── app.js        # Frontend quiz functionality
```

## Data Format Details

The application expects 11 lists with the following data:

1. **Articles:** German articles (der/die/das)
2. **Reflexivity:** Reflexive pronouns (sich, etc.)
3. **Words:** The main German vocabulary words
4. **Plural Endings:** Plural forms or endings
5. **Noun Declination:** Declination information
6. **Present Conjugation:** Present tense conjugations
7. **Verb Type:** Verb classification (strong, weak, etc.)
8. **Simple Past:** Past tense forms
9. **Helping Verb:** Auxiliary verbs (haben/sein)
10. **Past Participle:** Past participle forms
11. **Definition:** English translations/definitions

## Troubleshooting

### No vocabulary data loaded
- Make sure you've added your data to `data.txt`
- Verify that all 11 lists have the same number of entries
- Check that the Python list format is correct (with quotes and brackets)
- Restart the Flask server after updating `data.txt`

### Import errors
- Ensure you've installed dependencies: `pip install -r requirements.txt`
- Check that you're using Python 3.7 or higher

### Port already in use
- Change the port in `app.py` by modifying: `app.run(debug=True, port=5000)`
- Or kill the process using port 5000

## Customization

### Adjusting History Buffer
Edit the `MAX_HISTORY` variable in [app.py](app.py:11) to change how many words are remembered before allowing repeats.

### Styling
Modify [static/css/style.css](static/css/style.css) to customize colors, fonts, and layout.

### Quiz Behavior
Edit [static/js/app.js](static/js/app.js) to add new features or modify quiz behavior.

## License

This is a personal study tool. Feel free to modify and use as needed.

## Tips for Effective Study

1. Try to recall as much information as possible before revealing
2. Switch between modes to test different aspects of recall
3. Use regularly for best results with spaced repetition
4. Focus on words you find challenging by noting patterns in the data

Happy learning!
