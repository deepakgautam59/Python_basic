car={
    "type":"electric",
    "model":"cybertruck",
    "company":"tesla",
    "mileage":"350 km/hr",
}

print(car)
print()
car.clear()
print(car)
dict_1={
    "name":"Deepak Gautam",
    "age":"40",
    "phone":"9939393993",
}
dict_2={"previous_school":"Gorkha",
"percentage":"20%",
        }
dict_3={**dict_1,**dict_2}
print(dict_3)