def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        print("The line is currently:", end=" ")
        for i, person in enumerate(deli_line, start=1):
            print(f"{i}. {person}", end=" ")
        print()

def take_a_number(deli_line, new_person):
    deli_line.append(new_person)
    position = len(deli_line)
    print(f"Welcome, {new_person}. You are number {position} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving_person = deli_line.pop(0)
        print(f"Currently serving {serving_person}.")

def update_line_numbers(deli_line):
    for i, person in enumerate(deli_line, start=1):
        print(f"{i}. {person}", end=" ")
    print()

# Example usage
katz_deli = []

take_a_number(katz_deli, "Ada")  # Welcome, Ada. You are number 1 in line.
take_a_number(katz_deli, "Grace")  # Welcome, Grace. You are number 2 in line.
take_a_number(katz_deli, "Kent")  # Welcome, Kent. You are number 3 in line.

line(katz_deli)  # The line is currently: 1. Ada 2. Grace 3. Kent

now_serving(katz_deli)  # Currently serving Ada.

line(katz_deli)  # The line is currently: 1. Grace 2. Kent

take_a_number(katz_deli, "Matz")  # Welcome, Matz. You are number 3 in line.

line(katz_deli)  # The line is currently: 1. Grace 2. Kent 3. Matz

now_serving(katz_deli)  # Currently serving Grace.

line(katz_deli)  # The line is currently: 1. Kent 2. Matz

