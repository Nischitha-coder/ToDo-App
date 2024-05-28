import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)
print(data)

for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["alternative"]):
        print(index+1, "-", alternative)

    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_ans"]:
        score = score+1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    print(f"{index+1} {result} - Your answer: {question['user_choice']} Correct answer: {question['correct_ans']}")





