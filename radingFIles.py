'''#way 1

with open('text.txt','r') as f:
    for i in f :
        print(i) # it will print with newlines , if i won't => i.strip()

#way 2

with open('text.txt','r') as f:
    print(f.read())'''

'''===========wirting files==========='''
#way 1
'''
with open('text.txt','w') as f: # here is writing operation with overwriting contnet
    f.write('my name is , moahmmad \n')'''

#way 2
'''for i in range(101):
    with open('text.txt','a') as f: # here is writing operation without overwriting contnet because of parameter [a]
        f.write('my name is , moahmmad \n')'''

#way 3 
'''lines = ['aaa\n','bbb\n','ccc\n'] #multiple lines of text i want to add at once.
with open('text.txt','a') as f:
    f.writelines(lines)'''

'''===========task==========='''
### reading a file then count number of lines , words , and chars.

with open('text.txt','r') as f: #done of counting lines
    count = 0
    total_chars = 0
    total_words = 0
    for i in f:
        i = i.strip()
        total_chars += len(i) # [i] already represents a string
        count += 1
        total_words += len(i.split()) # split() returns a list of items of split words , so i need to count it.
    print(count,total_chars,total_words)