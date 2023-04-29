def print_sorted(a_dict):
    keys = sorted(a_dict.keys())  
    for key in keys:
        print (key, a_dict[key])

data = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print_sorted(data) 