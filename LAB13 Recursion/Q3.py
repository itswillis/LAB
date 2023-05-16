def print_pyramid(character, current_level, max_level):
    if current_level > max_level:
        return
    else:
        num_spaces = max_level - current_level
        spaces = ' ' * num_spaces
        characters = character * (2 * current_level - 1)
        print(f'{spaces}{characters}')
        print_pyramid(character, current_level + 1, max_level)

# Example usage:

print_pyramid("#", 1, 3)