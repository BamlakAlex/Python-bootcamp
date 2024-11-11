
'''
Discount Calculator challenge

'''
def discount_calculator(discount_percentage):
    shopping_mall_name= "walmart"
    total_cost =0
    item = []
    def sum_costs(*items):
        nonlocal total_cost
        print(f"Welcome to {shopping_mall_name}!")
        items= input("Please write your costs separated by comma? ").split(",")
        for i in items:
            i = float(i.strip())
            total_cost += i
            item.append(i)
        discount_amount= (discount_percentage * total_cost) / 100
        discounted_cost= total_cost - discount_amount
        return f"Your discounted cost is: {discounted_cost}, Thank you for choosing {shopping_mall_name}!"
    return sum_costs()
    

# final_price, thank_you_message = discount_calculator()
# print(f"Discounted Cost: {final_price}")
# print(thank_you_message)

print(discount_calculator(15))


'''
Word counter challenge

'''

words_with_count= {}
sentence= input("what is your sentence? ")
words = sentence.split()
def count_words(sentence,*words)-> dict[str,int]:
    for word in words:
        count=0
        count += words.count(word)
        words_with_count[word]=count
    return words_with_count
    

print(count_words(sentence, *words ))

'''
Person challenge

'''


class Person:

    def __init__(self,name:str, age:int, occupation:str):
        self.name = name
        self.age = age
        self.occupation = occupation
    def introduce(self):
        print(f"Hello! This is {self.name} aged {self.age} working as a {self.occupation}")
    def change_occupation(self, new_occupation):
        if self.occupation != new_occupation:
            self.occupation = new_occupation
            print(f"Hello! This is {self.name} aged {self.age} working as a {self.occupation}")
 
person_1= Person("Christina, 19, "Project Manager")
person_2= Person("Bamlak", 23, "Civil Engineer")

person_1.introduce()
person_2.introduce()
person_2.change_occupation("Developer")
