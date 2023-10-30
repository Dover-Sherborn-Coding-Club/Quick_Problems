myList=[1, 3, 5, 2, 4]

def bubble_sort(List):
  # Finds the length of the list
  len_List = len(List)
  # Iterates through the list
  for i in range(len_List):
    for n in range(0, len_List - i - 1):
      if (List[n] > List[n + 1]):
        # Switches the position of the two numbers
        List[n], List[n + 1] = List[n + 1], List[n]
  # Remember to return something, otherwise the function won't output anything
  return List

# Run the function on the list
sorted_myList = bubble_sort(myList)

""" If you're taking AP comp sci principles, then you'll this method of how to print should look familiar
    print("If %s is sorted, we'll get %s" %(myList, sorted_myList)) """

# Otherwise, you can print like this
print("If {0} is sorted, we'll get {1}".format(myList, sorted_myList))
