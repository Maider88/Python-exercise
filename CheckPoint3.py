#1
name = "Kristine"
years_old = 36
list = ["Laila", "Jordan", "Leila"]
query = "Laila" in list
sentence = """
My name is {name} I am {years_old} years old and my friends are the ones on the {list}
""".format(name=name, years_old=years_old, list=list)
print(sentence)
print(query)

#2
started_sentence = "Las ovejas son muy bonitas"
first_word = started_sentence[0:3]
new_sentence = first_word
print(new_sentence)

#3
sentence = "Las ovejas son muy bonitas"
print(sentence[:3])

#4
meal_completed = True
sub_total = 100  
tip = 10  
total = sub_total + tip
print(total)

#5
sentence = "Las ovejas son muy bonitas"
print(sentence[-7:])

#6
names = "Harry,Alex,Susie,Jared,Gail,Conner"
list_of_names = names.split(",")
print(list_of_names)

#7
sentence = "Las ovejas son muy bonitas"
first_word = sentence[:3]
last_words = sentence[-23:]
new_sentence = first_word.upper() + last_words.lower()
print(first_word)
print(last_words)
print(new_sentence)

#8
name = "Kristine"
years_old = 36
greeting = f"Hello, my name is {name} and I am {years_old} years old".format(name, years_old)
print(greeting)

#9
sentence = "hello world"
print(sentence)

