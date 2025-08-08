# Demonstrate List slicing
list_num = [i for i in range(1,11)]
print("Original List: ",list_num)
first_5 = list_num[:5]
print("Extracted First five elements: ",first_5)
first_5.reverse()
print("Reversed extracted elements: ",first_5)


