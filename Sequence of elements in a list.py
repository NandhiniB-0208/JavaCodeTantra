data_input = input("data: ")
seq_input = input("seq of elements: ")
list1 = list(map(int, data_input.split(',')))
seq_list = list(map(int, seq_input.split(',')))
all_present = True
for element in seq_list:
    if element not in list1:
        all_present = False
        break
if all_present:
    print("exist")
else:
    print("does not exist")
