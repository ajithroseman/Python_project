import random
list1 = ["apple","orange","grapes","papaya","banana"]
active_list = random.choice(list1)
hidden_list = ["_"] * len(active_list)
guessed_letter = set()
attempt = 6
while attempt > 0 and "_" in hidden_list:
    print(" ".join(hidden_list))
    print(f"Guessed letter:{','.join(sorted(guessed_letter))}")
    print("attempt left:",attempt)
    guess = input("Enter a letter you want to guess :").lower()
    if not guess.isalpha() or len(guess)!=1:
        print("Enter letter from a to z")
        continue
    if guess in guessed_letter:
        print("You have already entered letter")
        continue
    guessed_letter.add(guess)
    if guess in active_list:
        print("you have guessed correct letter")
        for i in range(len(active_list)):
            if active_list[i] == guess:
                hidden_list[i] = guess
    else:
        print("wrong guess")
        attempt = attempt-1
if "_" not in hidden_list:
    print("Found it",active_list)
else:
    print("Game Over the word was",active_list)

