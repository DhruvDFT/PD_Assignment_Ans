import re
import pytest

# Load student answers from a markdown file named 'answers.md'
with open('answers.md') as f:
    content = f.read()

questions = {
    1: {'points': 2, 'pattern': r'IR drop'},
    2: {'points': 1, 'pattern': r'metal (?:width|spacing)'},
    3: {'points': 2, 'pattern': r'DRC'},
    # ... add entries up to question 20 ...
    16: {'points': 1, 'pattern': r'create_power_straps'},
    17: {'points': 1, 'pattern': r'VDD.*VSS'},
    18: {'points': 1, 'pattern': r'regenerate power rings'},
    19: {'points': 1, 'pattern': r'missing tie cells'},
    20: {'points': 1, 'pattern': r'metal area'},
}

def test_questions():
    total = 0
    for qnum, spec in questions.items():
        match = re.search(spec['pattern'], content, re.IGNORECASE)
        earned = spec['points'] if match else 0
        print(f"Q{qnum}: {earned}/{spec['points']}")
        total += earned
    assert total >= 15, f"Total score too low: {total}/20"
