import time
import random


l = []
d = {}
list_time = []
dict_time = []
rando = []
for x in range(0, 1000):
    i = random.randint(1, 1000)
    l.append(i)
    d[x] = ""

for x in range(0, 1000):
    i = random.randint(1, 1000)
    rando.append(i)

# 1ST QUESTIONS
def p(item: dict | list):
    time_start = time.perf_counter()
    for i in item:
        print(i)
    time_end = time.perf_counter()
    return time_end - time_start


# 2ND QUESTIONS
def r(item: dict | list):
    time_start = time.perf_counter()
    
    for i in rando:
        if i in item:
            print(True)

    time_end = time.perf_counter()
    return time_end - time_start    


# 3RD QUESTIONS
def insertion_list():
    item = []
    time_start = time.perf_counter()
    for i in rando:
        item.append(i)

    for i in item:
        print(i)

    time_end = time.perf_counter()
    return time_end - time_start

def insertion_dict():
    item = {}
    time_start = time.perf_counter()
    for i in rando:
        item[i] = ""

    for i in item:
        print(i)

    time_end = time.perf_counter()
    return time_end - time_start

# 4TH QUESTIONS

def deletion(item: dict | list):
    time_start = time.perf_counter()
    for i in rando:
        try:
            del item[i]
        except:
            pass

    time_end = time.perf_counter()
    return time_end - time_start

for _ in range(0, 3):

    # # first question
    input("Press Enter to see result of Question 1")
    list_time.append(p(l))
    dict_time.append(p(d))

    # # Second question
    input("Press Enter to see result of Question 2")
    list_time.append(r(l))
    dict_time.append(r(d))

    # # Third question
    input("Press Enter to see result of Question 3")
    list_time.append(insertion_list())
    dict_time.append(insertion_dict())

    # Fourth question
    input("Press Enter to see result of Question 4")
    list_time.append(deletion(l))
    dict_time.append(deletion(d))

print(f"{list_time = }\n{dict_time = }")
