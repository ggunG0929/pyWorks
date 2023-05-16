"""
# hangman 게임
-단어의 각 글자 자리에 짧은 선이 그려진다.
-글자 1개를 맞추면 글자가 표시되고, 추가로 계속 맞추면 글자가 표시된다.
-틀리면 기회가 1번 줄어든다.
-전체 글자를 입력하여 맞추면 프로그램이 바로 종료된다.


+ 글자를 하나씩 입력하여(순서대로 X) 맞추었을 때도 프로그램을 종료시키고 싶다..!
"""
import random
words = ['dog', 'cat', 'monkey', 'chicken', 'frog', 'horse']
lives_remaining = 10
guessed_letters = ''
temp = 0


def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("You win! Well done!")
            break
        if lives_remaining == 0:
            print("You are Hung")
            print("The word was: " + word)
            break


def pick_a_word():
    word = random.choice(words)
    return word


def get_guess(word):
    print_word_with_blanks(word)
    if temp == 1:   # -가 없는 경우는 정답을 맞춘 경우이므로 guess를 word와 일치시켜줌
        guess = word
        return guess
    else:   # -가 남아있는 경우
        print('Lives Remaining:' + str(lives_remaining))
        guess = input("Guess a letter or whole word?")
        return guess


def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word += letter
        else:
            display_word += '-'
    print(display_word)
    if display_word.find("-") <= -1:    # 선생님 예제를 보고 display_word에서 -가 없는 경우를 추가함
        global temp
        temp = 1    # 임시로 temp에 1을 지정
        return temp


def process_guess(guess, word):
    global lives_remaining
    global guessed_letters
    lives_remaining -= 1
    guessed_letters += guess
    if guess == word:
        return True
    return False


play()
