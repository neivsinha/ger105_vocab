// Quiz application state
let currentMode = 'definition';
let currentEntry = null;
let isAnswerRevealed = false;

// DOM elements
const modeButtons = document.querySelectorAll('.mode-btn');
const promptLabel = document.getElementById('prompt-label');
const promptContent = document.getElementById('prompt-content');
const promptSection = document.querySelector('.quiz-prompt');
const answerSection = document.getElementById('answer-section');
const answerGrid = document.getElementById('answer-grid');
const actionBtn = document.getElementById('action-btn');
const statsElement = document.getElementById('vocab-count');
const errorMessage = document.getElementById('error-message');

// Field labels for display
const fieldLabels = {
    article: 'Article',
    reflexivity: 'Reflexivity',
    word: 'German Word',
    plural_ending: 'Plural Ending',
    noun_declination: 'Noun Declination',
    present_conjugation: 'Present Conjugation',
    verb_type: 'Verb Type',
    simple_past: 'Simple Past',
    helping_verb: 'Helping Verb',
    past_participle: 'Past Participle',
    definition: 'English Definition'
};

// Initialize the app
async function init() {
    await loadStats();
    setupEventListeners();
    // Enable the initial Next button
    actionBtn.disabled = false;
    actionBtn.textContent = 'Next';
    isAnswerRevealed = true; // Set to true so first click loads an entry
}

// Load vocabulary statistics
async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();

        if (data.loaded && data.total_entries > 0) {
            statsElement.textContent = `${data.total_entries} vocabulary entries loaded`;
            errorMessage.classList.add('hidden');
        } else {
            statsElement.textContent = 'No vocabulary data loaded';
            errorMessage.classList.remove('hidden');
        }
    } catch (error) {
        console.error('Error loading stats:', error);
        statsElement.textContent = 'Error loading data';
        errorMessage.classList.remove('hidden');
    }
}

// Setup event listeners
function setupEventListeners() {
    // Mode buttons
    modeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const mode = btn.dataset.mode;
            switchMode(mode);
        });
    });

    // Action button (toggles between Next and Reveal)
    actionBtn.addEventListener('click', handleAction);
}

// Handle action button click
function handleAction() {
    if (isAnswerRevealed) {
        loadNextEntry();
    } else {
        revealAnswer();
    }
}

// Switch between quiz modes
function switchMode(mode) {
    currentMode = mode;

    // Update button states
    modeButtons.forEach(btn => {
        if (btn.dataset.mode === mode) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // Update prompt label
    if (mode === 'definition') {
        promptLabel.textContent = 'English Definition';
    } else {
        promptLabel.textContent = 'German Word';
    }

    // Reset and load new entry
    resetQuiz();
    loadNextEntry();
}

// Load next vocabulary entry
async function loadNextEntry() {
    try {
        const response = await fetch('/api/random-entry');

        if (!response.ok) {
            throw new Error('Failed to load vocabulary entry');
        }

        currentEntry = await response.json();
        displayPrompt();
        resetAnswer();

    } catch (error) {
        console.error('Error loading entry:', error);
        promptContent.textContent = 'Error loading vocabulary. Please check data.txt';
        actionBtn.disabled = true;
    }
}

// Display the prompt based on current mode
function displayPrompt() {
    if (!currentEntry) return;

    if (currentMode === 'definition') {
        promptContent.textContent = currentEntry.definition || 'No definition available';
    } else {
        // Word mode - show article + reflexivity + word
        let wordDisplay = '';
        if (currentEntry.article) {
            wordDisplay += currentEntry.article + ' ';
        }
        if (currentEntry.reflexivity) {
            wordDisplay += currentEntry.reflexivity + ' ';
        }
        wordDisplay += currentEntry.word;
        promptContent.textContent = wordDisplay;
    }

    actionBtn.disabled = false;
    actionBtn.textContent = 'Reveal Answer';
    isAnswerRevealed = false;
}

// Reset answer display
function resetAnswer() {
    answerSection.classList.add('hidden');
    answerGrid.innerHTML = '';
    actionBtn.textContent = 'Reveal Answer';
    promptSection.classList.remove('has-answer');
}

// Reveal the answer
function revealAnswer() {
    if (!currentEntry || isAnswerRevealed) return;

    isAnswerRevealed = true;
    actionBtn.textContent = 'Next';
    promptSection.classList.add('has-answer');

    // Determine which fields to show based on mode
    let fieldsToShow = [];

    if (currentMode === 'definition') {
        // Show all German data points
        fieldsToShow = [
            'article',
            'reflexivity',
            'word',
            'plural_ending',
            'noun_declination',
            'present_conjugation',
            'verb_type',
            'simple_past',
            'helping_verb',
            'past_participle'
        ];
    } else {
        // Show all remaining data points except the word itself
        fieldsToShow = [
            'article',
            'reflexivity',
            'plural_ending',
            'noun_declination',
            'present_conjugation',
            'verb_type',
            'simple_past',
            'helping_verb',
            'past_participle',
            'definition'
        ];
    }

    // Build answer grid
    answerGrid.innerHTML = '';
    fieldsToShow.forEach(field => {
        const value = currentEntry[field];
        const isEmpty = !value || value === '';

        const answerItem = document.createElement('div');
        answerItem.className = `answer-item ${isEmpty ? 'empty' : ''}`;

        const label = document.createElement('div');
        label.className = 'answer-label';
        label.textContent = fieldLabels[field];

        const valueDiv = document.createElement('div');
        valueDiv.className = 'answer-value';
        valueDiv.textContent = isEmpty ? '—' : value;

        answerItem.appendChild(label);
        answerItem.appendChild(valueDiv);
        answerGrid.appendChild(answerItem);
    });

    // Show answer section with animation
    answerSection.classList.remove('hidden');
}

// Reset quiz state
function resetQuiz() {
    currentEntry = null;
    isAnswerRevealed = false;
    promptContent.textContent = 'Click "Next" to start';
    resetAnswer();
    actionBtn.disabled = false;
    actionBtn.textContent = 'Next';
}

// Start the application
init();
