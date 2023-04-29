

# [(2022, 'Northland region', 2367), (2022, 'Auckland region', 20469), (2021, 'Northland region', 2262), (2021, 'Auckland region', 20520)]

def create_region_dictionary(records_list): 
    region_dictionary = {}
    list = [] 

    for records in records_list: 
        year, region, birth = records
        if year not in list: 
            list.append(year)
        if region not in region_dictionary: 
            region_dictionary[region] = []
        region_dictionary[region].append((year, birth))
    
    list.sort()
    for region_key in region_dictionary.keys():
        region_dictionary[region_key].sort()
    return list, region_dictionary
    

data = [(2022, 'Northland region', 2367), (2022, 'Auckland region', 20469), (2021, 'Northland region', 2262), (2021, 'Auckland region', 20520)]
a_list, a_dict = create_region_dictionary(data)
print(a_list)
for key in sorted(a_dict):
    print(key, a_dict[key])