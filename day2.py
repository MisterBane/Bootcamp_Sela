from collections import Counter
##1.a


s = input('please enter a string : ');

ch_dict = {}
for ch in sorted(s):
    ch_dict[ch] = ch_dict.get(ch, 0)+1

for ch in ch_dict:
    print(f"{ch} - {ch_dict[ch]}")


##1.b

res = {}

for letter in set(s):
    letter_count = s.count(letter)

    if letter_count not in res:
        res[letter_count]= []
    res[letter_count].append(letter)

print(res)


##2.a

lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]

all_lists_dic = {"lst1": lst1, "lst2":lst2, "lst3":lst3}
fit_dic = {}

for name, lst in all_lists_dic.items():
    tmp_set= set(lst)
    if len(tmp_set) == len(lst):
        fit_dic[name] = tmp_set

print(fit_dic)
common_values = set.intersection(*fit_dic.values())
print(commom_values, fit_dic.keys())

#2.b

lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]

new_lst = list(set(lst1) & set(lst2))
print(new_lst)

##3

lst = [31, 99, 3, 1943]

for item in lst:
    new_lst = list(str(item))

sort_order = input("pick Ascending or Descending \n")

if sort_order == 'Ascending':
    new_lst.sort()
    print(new_lst)
elif sort_order == 'Descending':
    new_lst.sort(reverse=True)
    print(new_lst)


lst1 = [11, 7, 5, 8, 5, 37, 11, 5]lst2 = [22, 8, 10, 1, 11]lst3 = [71, 3, 22, 8, 2, 14, 1]all_lists_dic = {"lst1": lst1, "lst2": lst2, "lst3": lst3}fit_dic = {}for name, lst in all_lists_dic.items():tmp_set = set(lst)if len(tmp_set) == len(lst):fit_dic[name] = tmp_setprint(fit_dic)common_values = set.intersection(*fit_dic.values())print(common_values, " ".join(fit_dic.keys()))# lst = [10, 20, 30, 40]# s = " ".join([str(v) for v in lst])# print(s, lst)