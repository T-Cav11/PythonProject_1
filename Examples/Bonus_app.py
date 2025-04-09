import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question text"])
    for index, answers in enumerate (question["answers"]):
        print(index + 1,"-", answers)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


for index, question in enumerate (data):
    if question["user_choice"] == question["correct answer"]:
        score = score + 1
        result = "correct answer"
    else:
        result = "wrong answer"
    message = f"{index +1} {result} - Your answer was: {question['user_choice']}, the correct answer is {question['correct answer']}"
print(message)

print(score, "/", len(data))