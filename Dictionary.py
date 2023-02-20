
"""
User = {
    "Name":"Kelwin",
    "Age": 24,
    "Verify": True
}
#How to get items from Dictionaries
print(User.get("Name"))

#How to add elements
User["Gender"] = "M"
print(User["Gender"])


#Exercice Spelling Numbers

Value= input("Phone: ")

Map = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five", 
}
output=""
for i in Value:
   output+= Map.get(i, "undefined") + " "

print(output)

"""

#Exercicies 2 - Converting emojis

Phrase= input("> ")
Word=Phrase.split(' ')
print(Word)

Emoji= {
    ":)" : "🙂",
    ":(" : "😟"

}

output2=""
for i in Word:
     output2 += Emoji.get(i,i) + " "

print(output2)







