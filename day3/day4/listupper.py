elem_list=["Gta","Pubg","Freefire","Mobile Legends",5,1.23]

def list_elems(lists):
    new_list=[]
    for elem in lists:
        if type(elem) not in [int,float]:
           upper_elem=""
           upper_elem=elem.upper()
        else:
            upper_elem=elem
        new_list.append(upper_elem)
    return new_list       
all_upper_case_list=list_elems(elem_list)
# print(all_upper_case_list)



