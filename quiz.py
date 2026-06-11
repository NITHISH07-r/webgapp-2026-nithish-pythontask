questions=[
    {
        "question": "What is the capital of India?",
        "answer": "Delhi"
    },
    {
        "question": "Who developed Python?",
        "answer": "Guido van Rossum"
    },
    {
        "question": "What is 5 + 5?",
        "answer": "10"
    }
]

score = 0

for q in questions:
    print("\n"+q["question"])

    user_answer=input("Your Answer: ")

    if user_answer.lower()==q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:",q["answer"])

print("\nQuiz Completed")
print("Your Score:", score, "/" ,len(questions))