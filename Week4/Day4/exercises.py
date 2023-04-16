# Exercise 1
import random
def get_words_from_file():
    with open('words_list.txt','r') as file:
        Lines=file.readlines()
        return Lines

def get_random_sentence(length:int):
    Lines=get_words_from_file()
    sentence_list=[Lines[random.randint(0,len(Lines))] for i in range(length)]
    sentence_list2=[]
    for item in sentence_list:
        l=list(item)
        l.remove('\n')
        sentence_list2+=f" {''.join(l)}"
    return (''.join(sentence_list2))

def main():
    while True:
        print("This code generate sentences of random words for a user given length")
        user=input("how long should sentence be (1-20)? ")
        if type(user) == int:
            print(f"{get_random_sentence((user))}.")
            break
        else:
            print("Learn to follow instruction")

# main()
# Exercise 2
import json,ast
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
print(ast.literal_eval(sampleJson))