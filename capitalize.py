# capitilizes every word in a sentence

userinput = input('Enter a sentence or type "exit" : ')


def titlecase(userinput):
    titlecase = []
    for word in userinput.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
    return ' '.join(titlecase)

print(titlecase(userinput))