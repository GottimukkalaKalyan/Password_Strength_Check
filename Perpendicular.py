def final_result(list_a,max_len):
    for i in range(1,max_len+1):
        res = ""
        for each in list_a:
            if i <= len(each):
                res += each[i-1]
            else:
                res += " "
        print(res)

word = "ABC DEF GHIK".split(" ")
max_lenght = len(word[0])
for i in word:
    if max_lenght < len(i):
        max_lenght = len(i)
final_result(word,max_lenght)