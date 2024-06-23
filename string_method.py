my_string= "hello Everyone"
print(my_string.lower(),"all Lower")
print(my_string.upper(),"all Upper")
print(my_string.capitalize())
new_string= "hello Everyone. how are you all?"
print(new_string.title())
print(new_string.count("yo"))
print(len(my_string))
string_from_wikipedia=""" officially the Federal Democratic Republic of Nepal[b], is a 
landlocked country in South Asia. It is mainly situated in the Himalayas,
 but also includes parts of the Indo-Gangetic Plain. """

print(string_from_wikipedia.count("the"))
print("__________Starts With And End With______")
string_check="Why Are you running?"
print(string_check.startswith("Why"))
print(string_check.startswith("why"))
print(string_check.endswith("g?"))
print(string_check.endswith("?"))
yamesh= 'Yamesh Said, "Why are you Running"'
print(yamesh)
string_3=" Here You go again! "
print(f"start{string_3}end")
print(f"start{string_3.strip()}end")
print(string_3.strip())
print("________split______________")
fruit_name="Apple Banana Orange Gauva"
print(fruit_name.split(","))
print(fruit_name.split("a"))
print(fruit_name[0:10:2])
