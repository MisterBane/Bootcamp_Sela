lst = [3, 7, 2]
lst = [item*'*' for item in lst]

print(lst)


lst1 = ["a", "b", "c"]
lst2 = ["x", "y", "z", "d", "e"]

new_lst = []
for i in range(0, len(lst1)):
    new_lst.append((lst1[i] + lst2[-i-1]))

print(new_lst)
