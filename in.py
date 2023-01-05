text="Name: Kelwin"

element="kelwin"

#it means if exists element inside the text, return boolean
verify=element.upper() in text.upper()

#Not in means If not exist
verify2=element.upper() not in text.upper()
print(verify)