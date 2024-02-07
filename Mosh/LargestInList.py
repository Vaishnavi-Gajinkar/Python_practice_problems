li = [21, 36, 82, 19, 52]
max = 0
for item in li:
    if item > max:
        max = item
print(max)
# -------------------------------------------
print('Removing List Duplicates')
org_list = [21,36,82,19,52,36,82,82,52,52,52,52,52,36]
uniques = []
for n in org_list:
    if n not in uniques:
        uniques.append(n)
print(uniques)
#
# org_list = [21,36,82,19,52,36,82,82,52,52,52,52,52,36]
# cpy_list = org_list.copy()
# temp = []
# for i in org_list:
#     count_occurnce = org_list.count(i)
#     if count_occurnce > 1:
#         for c in range (0, count_occurnce):
#             firstindex = int(org_list.index(i))
#             nextindex = int(org_list.index(i, firstindex+1))
#             org_list.pop(nextindex)
# print(org_list)











