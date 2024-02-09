'''Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''
exam_st_date = (11, 12, 2014)
# lizt = str(list(exam_st_date))
# output = ""
# print(lizt)
# for dt in lizt:
#     output += dt + "/"
# print(output) #--> [/1/1/,/ /1/2/,/ /2/0/1/4/]/
print("The exam will start from : %i / %i / %i" % exam_st_date)