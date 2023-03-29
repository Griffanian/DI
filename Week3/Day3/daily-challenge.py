# Daily Challenge 1

# word_input=input("give me a word. ")
# word_dict={}

# for i,char in enumerate(word_input) :
#     if char in word_dict.keys():
#         word_dict[char].append(i)
#     else:
#         word_dict[char]=[i]
# print(word_dict)

# Daily Challenge 2

items_purchase1 = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

items_purchasable = []
wallet = "$300"


def caculate_purchases(items_purchase:dict[str,str] , wallet:str) -> tuple[ list, str]:
  for key, value in items_purchase.items():
      wallet_int = int(wallet.strip("$"))
      value_update=value.strip("$")
      value_update=value_update.replace(",","")
      value_int=int(value_update)
      if value_int <= wallet_int:
          items_purchasable.append(key)
          wallet_int-=value_int
  return (sorted(items_purchasable),(f'${wallet_int}') if items_purchasable else "Nothing")

def full_info(**kwargs):
   out=''
   for key, value in kwargs.items():
      out += f'{key}:{value}\n'
      
      return out

def add_repeat(x:int,times:int) ->int:
  list1=[int(str(x)*(i+1))for i in range(times)]
  return sum(list1)


numbers=[1,2,3,4,5,5,6,7,8]

result_list=list(map(lambda num: num * 2, numbers))


words= ['dogs','cat','ball']

result_list1=list(map(lambda item: item.capitalize(), words))

print(result_list1)