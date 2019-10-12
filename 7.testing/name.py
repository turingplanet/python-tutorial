# names.py
from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nfirst name: ")
    if first == 'q':
        break
    last = input("\nlast name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}.")