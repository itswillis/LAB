def get_longest_string_length(dictionary):

    max = 0

    for key in dictionary.keys():
        if len(str(key)) > max:
            max = len(str(key))

    return max

def get_longest_column_length(columns_list):
    max_length = 5

    for col in columns_list:
        col_length = len(str(col))
        if col_length > max_length:
            max_length = col_length
            
    return max_length

def print_table(name, column_names, a_dict):
    # Get the maximum width for the label column
    label_width = get_longest_string_length(a_dict)

    # Get the maximum width for each data column
    data_width = get_longest_column_length(column_names)

    # Print the header row
    header = f"{name:<{label_width}} |"
    for col in column_names:
        header += f" {col:<{data_width}} |"
    print(header)
    print("-" * (len(header)))

    # Sort the dictionary by region name
    sorted_dict = dict(sorted(a_dict.items()))

    # Print each row of data
    for region, data in sorted_dict.items():
        row = f"{region:<{label_width}} |"
        for year, value in data:
            row += f" {value:<{data_width}} |"
        print(row)

years = [2021, 2022]
a_dict = {'Northland region': [(2021, 2262), (2022, 2367)], 'Auckland region': [(2021, 20520), (2022, 20469)]}
print_table("Regions", years, a_dict)