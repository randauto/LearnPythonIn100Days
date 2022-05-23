vanban = "Xin Chao The Gioi"
print(vanban[2:5])
print(vanban[:5])
print(vanban[2:])

# Modify Strings
a = "     chao cac ban      "
print(a.upper())
print(a.lower())
# remove whitespace
print(a.strip())  # remove white spaces in string
print(a.lstrip())  # remove white spaces in left string.
print(a.rstrip())  # remove white spaces in right string

# Replace string
print(vanban.replace("G", "j"))

# Split string
print(vanban.split(" "))
print(a.strip().capitalize())  # Converts the first character to upper case
print(vanban.swapcase())  # Swaps cases, lower case becomes upper case and vice versa

# format string
age = 33
txt = "My name is Tuan, I am {}"
txt = txt.format(age)
print(txt)

ten, tuoi, diachi = "Le Quoc Tuan", 33, "Ha Dong - Ha Noi"
sentence = "xin chao cac ban, ten toi la {0}, nam nay toi {1}, toi dang song o {2}"
print(sentence.format(ten, tuoi, diachi))
