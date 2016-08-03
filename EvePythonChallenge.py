# Import Counter method and sys
from collections import Counter
import sys

#Store text from file into a list of strings in input_file
input_file = open(r"/Users/eve/Desktop/PythonPrograms/Documents/Fruit copy.txt")
input_file = input_file.readlines()

def strip_data(data_list):    
    #Strip the strings so that the \n character is removed
    j=0    
    for i in data_list:
        data_list[j]=i.rstrip('\n')
        j+=1    

def validate_data(data_list):
    # Make sure it isn't an empty string or shootin' blanks
    j=0
    if not data_list:
        print('Oops. There doesn\'t seem to be anything here.')
        sys.exit()

    for i in data_list:
        if data_list[j].isspace():
            print('This program is for fruit, not space. Try again.')
            sys.exit()
            
    # Check if there's only one word to a string
    if len(data_list[1].split())>1:
        print('You can only use a file with one fruit per line')
        sys.exit()      
            
    #Check if everything entered is alpha
    j=0
    for i in data_list:    
        if data_list[j].isalpha():
            j+=1
            continue
        else:
            print('Numbers are not fruit. Try again.')
            sys.exit()    
    
    # Make sure there's at least 15 items
    if len(data_list)<15:
        print('You don\'t have enough items to make a table')
        sys.exit()
    
    # Convert everything to Title case
    j=0
    for i in data_list:
        data_list[j]=data_list[j].title()
        j+=1
        continue 
    
    # Make sure all words are ten characters or less
    j=0
    for i in data_list:
        if len(data_list[j])<11:
            j+=1
            continue
        else:
            print('You can only have fruit that is ten characters or less')
            sys.exit()
          
    
def manipulate_data(data_list):  
    # Split the list into sublists of 15
    global chunks
    chunks = [data_list[x:x+15] for x in range(0, len(data_list), 15)]


    # Make sure the list doesn't have too much of the same item
    j=0
    for v in Counter(chunks[j]).values():  
        while j < len(chunks):
            if v > 6:
                print('You have too many of one item')
                j+=1
                sys.exit()
            else:
                break
            
def sort_data(chunks_list):
    # Sort chunks
    j=0
    while j<len(chunks_list):
        chunks_list[j].sort()
        j+=1

def print_data(chunks_list):
    # Print the tables
    j=0
    while j<len(chunks_list)-1:
        print(r'----------------------------------'+ '\n' + '|' + chunks_list[j][0].center(10) + '|' + chunks_list[j][1].center(10) + '|' + chunks_list[j][2].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[j][3].center(10) +'|'+chunks_list[j][4].center(10)+'|'+chunks_list[j][5].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[j][6].center(10) +'|'+chunks_list[j][7].center(10)+'|'+chunks_list[j][8].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[j][9].center(10) +'|'+chunks_list[j][10].center(10)+'|'+chunks_list[j][11].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[j][12].center(10) +'|'+chunks_list[j][13].center(10)+'|'+chunks_list[j][14].center(10)+'|'+
              '\n----------------------------------')
        j+=1

    # Increment j to the last string in the list
    j=len(chunks_list)-1

    # Check last list to make sure it has enough to make a table
    if len(chunks_list[j])<15:
        print('There aren\'t enough items remaining to make another table.')
        print('You only have ' + str(len(chunks_list)-1) + ' items left. A table requires 15 items.')
        sys.exit()
    else:
        print(r'----------------------------------'+ '\n' + '|' + chunks_list[-1][0].center(10) + '|' + chunks_list[-1][1].center(10) + '|' + chunks_list[-1][2].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[-1][3].center(10) +'|'+chunks_list[-1][4].center(10)+'|'+chunks_list[-1][5].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[-1][6].center(10) +'|'+chunks_list[-1][7].center(10)+'|'+chunks_list[-1][8].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[-1][9].center(10) +'|'+chunks_list[-1][10].center(10)+'|'+chunks_list[-1][11].center(10)+'|'+
              '\n----------------------------------'+ '\n' + '|' + chunks_list[-1][12].center(10) +'|'+chunks_list[-1][13].center(10)+'|'+chunks_list[-1][14].center(10)+'|'+
              '\n----------------------------------')

strip_data(input_file)
validate_data(input_file)
manipulate_data(input_file)
sort_data(chunks)
print_data(chunks)
