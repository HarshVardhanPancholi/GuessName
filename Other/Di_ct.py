import json
data = json.load(open("original.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0:
        return data[get_close_matches(word , data.keys())[0]]  #difflib shoud be installed for such use
    else:
        print("Data not found")

z=1
while z == 1:
    word = input("Enter the word which you want to know\n")
    mean = translate(word)
    if type(mean) == list:
        for it in mean:
            print(it)
    else:
        print(mean)
    z = int(input("Press 1 to continue \nTo exit press 0\n"))

'''Now we can add '''
