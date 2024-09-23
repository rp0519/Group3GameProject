questions_and_answers = {
    1: {
        "How do you open a file for reading?": "open('file.txt', 'r')",
        "What is the purpose of the close() method?": "It closes the file"
    },
    2: {
        "How do you write to a file?": "with open('file.txt', 'w') as f: f.write('text')",
        "What does the with statement do in file handling?": "Ensures proper closing of the file"
    },
    3: {
        "How do you read all lines from a file and store them in a list?": "file.readlines()",
        "What file mode appends to a file?": "'a'"
    },
    4: {
        "What does the following code do? 'with open(file.txt, 'r+') as f: data=f.read(); f.write('New')'": "Reads and appends 'New'",
        "How do you handle FileNotFoundError?": "Using try-except"
    }
}
