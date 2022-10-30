file_read = open("group_scores.txt")
file_write = open('averageScore.txt', 'w', encoding='utf-8')

for group_scores in file_read:  #ผลลัพธ์ จะเป็น '83 75 52 43 81'
    sum_score = 0
    group_scores_list = group_scores.split(' ') #แปลงข้อความเป็นlist แล้วเอาไปวนloop  จะเป็น ['83' '75' '52' '43' '81'] 
    for score in group_scores_list:
        score_int = int(score)  
        sum_score += score_int

    average_score = sum_score / len(group_scores_list)
    file_write.write(str(average_score) +'\n')


file_read.close()
file_write.close()