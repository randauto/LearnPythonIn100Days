import mymodule  # import all element in mymodule
import mymodule as md  # import module with alias.
from mymodule import person  # only import person from module mymodule.

print(person)
print(person["name"])

mymodule.greeting()
md.greeting()
