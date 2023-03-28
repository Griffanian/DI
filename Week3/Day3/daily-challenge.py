# Daily Challenge 1

# word_input=input("give me a word. ")
# word_dict={}

# for i,char in enumerate(word_input) :
#     print(char, i)
#     if char in word_dict.keys():
#         word_dict[char].append(i)
#     else:
#         word_dict.update({char:list([i])})
#     print(word_dict)

# Daily Challenge 2

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# items_purchasable = []
# wallet = "$300"
# wallet_list=list(wallet)
# wallet_list.remove("$")
# wallet="".join(wallet_list)
# wallet_int=int(wallet)

# for key, value in items_purchase.items():
#     value_list=list(value)
#     value_list.remove("$")
#     if "," in value_list:
#         value_list.remove(",")
#     value_int=int("".join(value_list))
#     if value_int > wallet_int:
#         pass
#     else:
#         items_purchasable.append(key)
#         wallet_int-=value_int

# items_purchasable.sort()
# if not items_purchasable:
#     print("Nothing")
# else:
#     print(items_purchasable)
