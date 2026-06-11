def validate_answer(user_answer,correct_answer):
    if user_answer.lower()==correct_answer.lower():
        return True
    else:
        return False
question="What is the capital of India?"
correct="New Delhi"
print(question)
user_input=input("your answer: ")
if validate_answer(user_input,correct):      
    print("correct answer")
else:
    print("wrong answer")

