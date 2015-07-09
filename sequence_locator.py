# -*- coding: utf-8 -*-
"""
Created on Thu Jul 09 10:10:43 2015

@author: keriambermudez
"""

"""This is the script for the homework
Build a python script named sequence_locator.py saved to
python_scripts folder that:

1. assigns the vector and short-hairpin sequences to variables – use
these variables from here on

2. counts the number of occurrences of the short-hairpin sequence
within the vector sequence

3.finds the start position of the short-hairpin sequence within the
vector sequence

4. finds the end position of the short-hairpin sequence within the
vector sequence (this will probably require two steps and some math)

5. Uses the start position and end position of the short-hairpin to
find the sequence within the vector that supposedly matches

Hint: run each step interactively until you can get it to work. Save
things that work to your script

Hint: you will want to assign each steps output to a variable"""

# <codecell> 1. assigns the vector and short-hairpin sequences to variables – use these variables from here on

vector= "NNNNNNNNNNNNNNNNNNNNNGGCTGTGGCNAGTACTGCGACCTCCTAGCAAACTGGGGCACAGATAATC\
GATAGTTTGTTTGAATGAGGCTTCAGTACTTTACAGAATCGTTGCCTGCACATCTTGGANCACTTGCTGG\
GATTACTTCTTCAGGTTAACCCAACAGAAGGCTCGAGAAGGTATATTGCTGTTGACAGTGAGCGCGTAGT\
GTGATGTGTCTGAACTTAGTGAAGCCNNNNNATGTAANNTTCAGACACATCACACTACATGCCTACTGNC\
TCGGAATTCAAGGGGCTACTTTANGGNNNCAATTATNNTTGTTNNNNNAAAANNTGAANANCNTTGNNNN\
TNNNCTTTGNNANNNTTTTNNNNANNGCNNNNNNNNAAANNGGGNANAAANTNAANNNNNNTTTTTTTCA\
NNNGNANNANNNANNNNGNCNNGNNNNNNNNNCNNNNNNNNNGNNTNGNNGNNNNNNGNNNNNNCNNNNN\
NTNANNNNNNNNNNNGNNNNNANNNNNNNNNNNTNNNNNNNNNNNNNNNNNNNNNTNNNNNNCCNNGGNN\
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGNNNNNNNNNNNNNNNNNNNANNNNN\
NNCNNNNNNNNNNTNNNNNNNNNNNNNNNNNTNNNNNNNNNNNNNNNNNNNNNNNNNGANNNNNGNNNNN\
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"

hairpin = "GTAGTGTGATGTGTCTGAACT"

# <codecell> #2. counts the number of occurrences of the short-hairpin sequence
#within the vector sequence

counts = vector.count(hairpin)
print(counts)

# <codecell> #3.finds the start position of the short-hairpin sequence within the
#vector sequence

position = vector.find(hairpin)
print(position)

end_position = vector.find(hairpin)+ len(hairpin)
print(end_position)

# <codecell>
print("The sequence occurs: " + str(counts)+ " times")
print("The sequence can be found at start position: " +str(position) + ", and end position: " + str(end_position))
