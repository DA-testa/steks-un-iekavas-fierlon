# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
            last = opening_brackets_stack.pop().char
            if not are_matching(last, next):
                return i+1
    if len(opening_brackets_stack)>0:
        return opening_brackets_stack[0].position
            
def main():
    choice = input("Enter F or I")
    if choice == 'F':
        file_name = input("Enter the filename:")
        with open(file_name, 'r') as file:
            text = file.read().strip()
    elif choice == 'I':
        text = input("Enter the brackets:")
    else:
        print("Invalid choice")
        return
    mismatch = find_mismatch(text)
    print(mismatch)
if __name__ == "__main__":
    main()
