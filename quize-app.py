# quiz_app.py

def welcome():
    print("🎉 Welcome to the Python Basics Quiz! 🎉")
    name = input("Enter your name: ")
    print(f"Hi {name}! Let's begin...\n")
    return name

def ask_question(question, options, correct_option):
    print(question)
    for key in options:
        print(f"{key}. {options[key]}")
    
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == correct_option:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong! The correct answer is {correct_option}.\n")
        return False

def run_quiz():
    score = 0

    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": {'a': '.py', 'b': '.pt', 'c': '.pyt', 'd': '.python'},
            "answer": 'a'
        },
        {
            "question": "How do you insert COMMENTS in Python code?",
            "options": {'a': '// comment', 'b': '# comment', 'c': '-- comment', 'd': '/* comment */'},
            "answer": 'b'
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": {'a': 'function', 'b': 'fun', 'c': 'def', 'd': 'define'},
            "answer": 'c'
        },
        {
            "question": "What is the output of print(2 ** 3)?",
            "options": {'a': '6', 'b': '8', 'c': '9', 'd': '5'},
            "answer": 'b'
        },
        {
        "question": "1. What is the capital of India?",
        "options": {'a': 'Delhi', 'b': 'Mumbai', 'c': 'Kolkata', 'd': 'Chennai'},
        "answer": "a"
        },
        {
        "question": "2. What is 5 + 3?",
        "options": {'a': '6', 'b': '8', 'c': '9', 'd': '7'},
        "answer": "b"
        },
        {
        "question": "3. Who developed Python?",
        "options": {'a': 'James Gosling', 'b': 'Elon Musk', 'c': 'Guido van Rossum', 'd': 'Tim Cook'},
        "answer": "c"
        } 

    ]

    for q in questions:
        if ask_question(q['question'], q['options'], q['answer']):
            score += 1

    print(f"🎯 You got {score} out of {len(questions)} correct!")
    if score == len(questions):
        print("🏆 Excellent job!")
    elif score >= len(questions) // 2:
        print("👍 Good effort!")
    else:
        print("📘 Keep practicing!")

if __name__ == "__main__":
    welcome()
    run_quiz()
