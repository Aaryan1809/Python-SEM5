import time
book = open("Answers.txt" , "r")

file = book.read()
time.sleep(0.5)
print(file)




# with open('Answers.txt' , 'r') as book:
#     for line in book:   
#         print(line.strip())