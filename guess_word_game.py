import random
from module1 import questions, answers

def question_key():
    questions_keys=list(questions.keys())
    rand_num=random.randint(1,len(questions.keys()))
    questions_keys.pop((rand_num-1))
    return rand_num
key=question_key()

def start(key):
    result=""
    print(questions[key])
    for a in answers[questions[key]]:
        result+="∎"
    return result +"\n"
hidden= start(key)
print(hidden)

def guess(guess_count):
    a=1
    letter=""
    guessed_letters=[]
    print(f"You can guess only {guess_count} letters\n")
    while a<=guess_count:
        input_1=input("Guess a letter: ")
        if len(input_1.strip())<2 and len(input_1.strip())>0 and input_1.strip().isalpha():
            letter+=input_1
            guessed_letters.append(letter)
            a+=1
            letter=""
        else:
            continue
    return guessed_letters
guess_list=guess(4)

def word_process(guess,word):
    print("\n==> Let's try to guess the word ")
    result=''.join("∎" if c not in guess else c for c in word.lower())
    return "\n" + result
print(word_process(guess_list, answers[questions[key]]))

def finish():
    answer=input("Write your answer: ")
    if answer.strip().lower()==answers[questions[key]].lower():
        print("\n*** Congratulations!!! ***\n")
        print(f"Answer: {answers[questions[key]]}")
    else:
        print("\n*** GAME OVER!!! LOSER!!!***\n")
        print(f"Answer: {answers[questions[key]]}")
finish()