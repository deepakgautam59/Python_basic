first_dict={
    "name":"Yamesh Gautam",
    "address":"kailali",
    "college":"Banke Bageshwori",
}
print(first_dict["name"])
print(first_dict["address"])
print(first_dict["college"])
print(first_dict.keys())
print(first_dict.items())
first_dict["name"]="Deepak Gautam"
print(first_dict["name"])
first_dict["phone"]="9848974004"
print(first_dict)
del first_dict['phone']
print(first_dict)
poped_key=first_dict.pop("address")
print(f"The poped value is {poped_key}")
poped_item=first_dict.popitem()
print(f"The poped item is {poped_item}")
print()
print(first_dict)
value_list=first_dict.values()
print(f"The Values are {value_list}")
