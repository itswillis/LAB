def create_year_dictionary(records_list):

    region_dictionary = {}
    regions = []

    for record in records_list:
        year, region, births = record
        if year not in region_dictionary:
            region_dictionary[year] = []
        if region not in regions:
            regions.append(region)
        region_dictionary[year].append((region, births))

        regions.sort()
        for region_key in region_dictionary.keys():
            region_dictionary[region_key].sort()
    return regions, region_dictionary
    

data = [(2022, 'Northland region', 2367), (2022, 'Auckland region', 20469), (2021, 'Northland region', 2262), (2021, 'Auckland region', 20520)]
a_list, a_dict = create_year_dictionary(data)
print(a_list)
for key in sorted(a_dict):
    print(key, a_dict[key])