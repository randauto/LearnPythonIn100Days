import json
from difflib import get_close_matches

data = json.load(open("092 data.json"))


# translate word
def translate(w):
    message = "The word doesn't exist. Please double check it."
    w = w.lower()
    # Kiem tra xem tu nhap co nam trong key data cua dictionary khong?
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:  # Kiem tra xem co tu nao dong nghia khong.
        yn = input("Did you mean %s insted? Enter Y if yes, or N if No:" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return message
        else:
            return "We didn't understand your entry"
    else:
        # Neu khong thi dua ra la khong ton tai, kiem tra lai.
        return message


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
