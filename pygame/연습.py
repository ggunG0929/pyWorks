


# for letter in word:
#     if guessed_letters.find(letter) > -1:  # 글자를 찾음
#         display_word += letter  # 단어를 추가해서 저장
#     else:  # 글자를 찾지 못한 경우
#         display_word += '-'  # blank(밑줄)을 추가함
# print(display_word)

display_word = "fro-g"

if display_word.find("-") <= -1:
    print("없음")
else:
    print("있음")

