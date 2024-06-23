# for j in range(10):
#     print(j)
# for j in range(1, 40, 5):
#     print(j)
# i=0
# while i<5:
#     print(i)
#     i+=1
    
# list_1=["apple","banana","orange","gauva"]
# elements_in_list = len(list_1)
# for index in range(elements_in_list):
#     print(list_1[index])

# list_2=[]
# list_2.append("new element")
# for elem in list_1:
#       print(elem)

list_fruits=["mango","apple","orange","grapes"]
list_new=[]
for fruit_list in list_fruits:
     list_new.append(fruit_list.upper())
print(list_new)
for index,element in enumerate(list_fruits):
    print(index,element)
