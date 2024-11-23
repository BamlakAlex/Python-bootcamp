name_list = ["Ben", "Almaz", "Sara", "Tolosa", "Seblewongel", "Selam", "Bunny"]


def group_names(names):

    group_dict= {name[0] : [Name for Name in names if Name.startswith(name[0])] for name in names}
    return group_dict
    
print(group_names(name_list))


