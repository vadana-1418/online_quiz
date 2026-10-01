score = 0

print("Welcome to Online Quiz")

answer = input("Python is used for Machine Learning? (yes/no): ")

if answer.lower() == "yes":
    score = 10
    print("Correct!")
else:
    print("Wrong!")

print("Score:", score)
