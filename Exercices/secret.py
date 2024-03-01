
secret_word = "perfume"
right_words = ""


while True:

    question = input("Type a letter: ")
    if len(question) > 1:
        print("please type just a letter.")
    elif question.isdigit():
        print("please type a letter not a number")
    elif question in secret_word:
        right_words+=question

    formated = ""
    for s in secret_word:
        if s in right_words:
           formated += s
        else:
           formated+="*"

    
    print(formated)
    if "*" not in formated:
        print("You Won!")
        
       
