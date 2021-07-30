# Program to delete all occurrences of an element in a list.
l = list(input('Enter the list elements : ').split())
print('The original list is : ', l)
element = input('Enter the element you want to delete : ')
for i in l:
    if i == element:
        l.remove(i)
print('The list after removing all {} is : {}'.format(element, l))
