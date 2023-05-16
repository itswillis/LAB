def print_table(words_list, width):
    for word in words_list:
        print(f"|{word:<{width}}|")

print_table(['input', 'test', 'answer', 'solution', 'name'], 8)