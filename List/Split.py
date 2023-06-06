
phrase1 = '  kelwin, higor, ana, agata, gabi, janaina, jessica '

#Strip works like Trim from JS, cut both side spaces
phraseTRIM = phrase1.strip()

#Turn into Array by split(argument_to_separate)
phrase_gross = phraseTRIM.split(', ')

phrase = []




result = ', '.join(phrase)

print(result)



