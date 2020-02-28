#!/usr/bin/env python
import sys
 
# initial values
temp_count = 0
temp_word = None
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    # check if we get the same word as before
    # if yes, then increase counter; 
    # if no, then output old results and start counting again
    if word == temp_word:
        temp_count = temp_count + count
    else:
        if temp_word != None:
            print('%s\t%s'% (temp_word, temp_count))
        temp_word = word
        temp_count = count

# output very last word in the list
print('%s\t%s'% (temp_word, temp_count))
