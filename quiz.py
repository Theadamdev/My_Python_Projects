#My first pythn quiz using loops and collections
questions = ("What does GPT in chatGPT mean? : ",
             "What's the biggest animal in the world? : ",
             "What is the largest planet in the solar system? :",
             "How many bones are in the human body? : ",
             "What is the first element in the periodic table? : ")

options = (("A. Generative Pre-trained Transformer","B. Generative Pretrained Transformer","C. General Pre-trained Transformer","D. Generative Pre-informed Transformer"),
           ("A. The giraffe","B. The lion","C. The elephant","D. The blue whale"),
           ("A. Earth", "B. Saturn","C. Jupiter","D. Neptune"),
           ("A. 105","B. 206","C. 121","D. 201"),
           ("A. Oxygen","B. Carbon","C. Aluminium","D. Hydrogen"))

answers = ("A","D","C","B","D")
guesses = []
score = 0
question_num = 0

for question in questions :
    print("------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your guess (A ,B ,C ,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("-----------------------")
print("        Results        ")
print("-----------------------")
print("guesses" , end="")
for guess in guesses :
    print(guess, end = " ")
print()
score = int(score/len(questions)*100)
print(f"Your final score is : {score}%")
if score >= 50:
    print("Congratulations! You passed !")
else :
    print("Sorry! You failed !")

