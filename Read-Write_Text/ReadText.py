# # file = open("scores.txt")   #ตัวแปรรับไฟล์
# file = open("group_scores.txt")

# # print(file.read())
# # print(file.readline())

# pass_count = 0

# # for score in file:
# #     score_int = int(score)
# #     if score_int >= 50:
# #         pass_count += 1

# # print('Student passed = ' + str(pass_count))

# for group_scores in file:  #ผลลัพธ์ จะเป็น '83 75 52 43 81'
#     group_scores_list = group_scores.split(' ') #แปลงข้อความเป็นlist แล้วเอาไปวนloop  จะเป็น ['83' '75' '52' '43' '81'] 
#     for score in group_scores_list:
#         score_int = int(score)        
#         if score_int >= 50:
#             pass_count += 1

# print('Student passed = ' + str(pass_count))


# file.close()

# ------------------------------------------------

# file = open("scores.txt")   #ตัวแปรรับไฟล์
with open("group_scores.txt") as file:

    pass_count = 0

    for group_scores in file:  #ผลลัพธ์ จะเป็น '83 75 52 43 81'
        group_scores_list = group_scores.split(' ') #แปลงข้อความเป็นlist แล้วเอาไปวนloop  จะเป็น ['83' '75' '52' '43' '81'] 
        for score in group_scores_list:
            score_int = int(score)        
            if score_int >= 50:
                pass_count += 1

    print('Student passed = ' + str(pass_count))


file.close()