from random import randint
from sorting import *

def guess_the_number():
    upper_bound = 10_000
    lower_bound = 1
    answer = None
    asn = None
    print("Think of a number between 1 and 10,000")
    while True:
        num = randint(lower_bound, upper_bound)
        answer = input(f"The number in your head is `{num}` is this right? (Y/N) ")
        if answer.lower() == "y":
            print(f"Total size of all the variable { asn.__sizeof__() + answer.__sizeof__() + num.__sizeof__() + upper_bound.__sizeof__() + lower_bound.__sizeof__()} bytes")

            break
        else:
            asn = input("Is the number I guess lower or higher than your number?(lower, higher) ")
            if asn.lower() == "higher":
                upper_bound = num
            else:
                lower_bound = num

def get_database():
    db = {}
    with open('database.txt') as f:
        for i in f.readlines():
            split = i.split()
            id = split[0]
            db[id] = {'first_name':'', 'email': '', 'major':'', 'full_name': ''}
            db[id]['first_name'] = split[1]
            db[id]['email'] = split[-2]
            db[id]['major'] = split[-1]
            db[id]['full_name'] = " ".join(split[1:-2])

    return db

def print_database(db: dict):
    for k,v in db.items():
        print(k)
        for kk, vv in v.items():
            print(f"\t{kk} : {vv}")

def print_memory(mem: list):
    for i in mem:
        stats = i.statistics('traceback')
        for s in stats[:-1]:
            a = s.traceback.format(most_recent_first=True)[-1]
            if "=" in a and 'print(' not in a:
                print(f"{s.size} Bytes | {a}")

def id():
    db = get_database()
    bubble_time, bubble_memory, bubble_sorted = id_sort(db, bubble_sort)
    insertion_time, insertion_memory, insertion_sorted = id_sort(db, insertion_sort)
    selection_time, selection_memory, selection_sorted = id_sort(db, selection_sort)
    merge_time, merge_memory, merge_sorted = id_sort(db, merge_sort)
    write_db(bubble_sorted, "id_bubble_sorted")
    write_db(insertion_sorted, "id_insertion_sorted")
    write_db(selection_sorted, "id_selection_sorted")
    write_db(merge_sorted, "id_merge_sorted")
    print(f"""Id Sort: 
    {bubble_time = } seconds | Memory Peaks: {bubble_memory[1]} Bytes
    {insertion_time = } seconds | Memory Peaks: {insertion_memory[1]} Bytes
    {selection_time = } seconds | Memory Peaks: {selection_memory[1]} Bytes
    {merge_time = } seconds | Memory Peaks: {merge_memory[1]} Bytes""")
    print_memory([bubble_memory[0], insertion_memory[0], selection_memory[0], merge_memory[0]])

def fn():
    db = get_database()
    bubble_time, bubble_memory, bubble_sorted = fn_sort(db, bubble_sort)
    insertion_time, insertion_memory, insertion_sorted = fn_sort(db, insertion_sort)
    selection_time, selection_memory, selection_sorted = fn_sort(db, selection_sort)
    merge_time, merge_memory, merge_sorted = fn_sort(db, merge_sort)
    write_db(bubble_sorted, "fn_bubble_sorted")
    write_db(insertion_sorted, "fn_insertion_sorted")
    write_db(selection_sorted, "fn_selection_sorted")
    write_db(merge_sorted, "fn_merge_sorted")
    print(f"""First name Sort: 
    {bubble_time = } seconds | Memory Peaks: {bubble_memory[1]} Bytes
    {insertion_time = } seconds | Memory Peaks: {insertion_memory[1]} Bytes
    {selection_time = } seconds | Memory Peaks: {selection_memory[1]} Bytes
    {merge_time = } seconds | Memory Peaks: {merge_memory[1]} Bytes""")
    print_memory([bubble_memory[0], insertion_memory[0], selection_memory[0], merge_memory[0]])


guess_the_number()

id()
print("-------------------------------")
fn()