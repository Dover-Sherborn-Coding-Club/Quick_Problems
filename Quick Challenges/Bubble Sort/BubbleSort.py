#Input for Sequence
def InputToList():
    input_string = input('Enter Numbers Separated By A Space \n')
    user_list = input_string.split()

#From ["1", "2"] (String List) --> [1, 2] (List)
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    return(user_list)


#Bubble Sort Code
def BubbleSort(seq):

    for i in range (len(seq)-1):
        for j in range (len(seq)-i-1):
            if seq [j] > seq [j+1]:
                temp = seq [j]
                seq [j] = seq [j+1]
                seq [j+1] = temp
    return seq

seq1 =  InputToList()

print (BubbleSort(seq1))
