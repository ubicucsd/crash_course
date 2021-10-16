'''
These imports will take care of everything you need.
You don't need to import anything else!
'''
import socket
import sys
from sys import exit
from Bio.Seq import *
from Bio.SeqUtils import *

'''
Whenever you see the variable seqObject, it is your 
original sequence converted to a Seq object.
'''

'''
Your goal is to use Biopython to get the complement of
the ORIGINAL sequence. The method should return this
complement.
'''
def complement(seqObject):
  return seqObject



'''
Your goal is to use Biopython to return a RNA sequence
representing the ORIGINAL sequence. The method
should return this RNA sequence.
'''
def transcribe(seqObject):
  return seqObject



'''
Your goal is to use Biopython to check if the
sub-sequence (passed in as 'subseq) appears in 
the original sequence (seqObject). The method should
return either True or False. (Alternatively, you can
return a positive number for True and negative number
for False. Either works.)
'''
def checkSubstring(seqObject, subseq):
  return seqObject



'''
Your goal is to use Biopython to calculate the
GC content (% of G's and C's) of the sequence.
The method should return this value (i.e. the 
method will return 22 for a sequence with 22%
GC).
'''
def getGC(seqObject):
  return seqObject



###########################################
###########################################
###########################################
###########################################
###########################################
#### Do not edit code under this line #####
###########################################
###########################################
###########################################
###########################################




def main():
  print("Trying to open file...")
  try:
    file = open("unidentified.fasta", "r")
  except:
    print("You don't have the unidentified.fasta file!")
    return;
  print("File opened!")

  sequence = ""
  for line in file:
    if line[0] != '>':
      sequence = sequence + line.strip()

  print("Original Sequence " + str(sequence)[0:10] + "...\n")


  print("Trying to get complement...")
  comp = complement(Seq(sequence))
  print("Complement generated: " + str(comp)[0:10] + "...")
  if comp == sequence:
    print("Your complement is the same as your original sequence! Make sure you are editing the complement method, and that you changed the return statement at the end to return the complement, not the original sequence.")
    return;
  if comp == str(Seq(sequence).complement()):
    print("Success! Move on to the next section.\n")
  else:
    print("Oh no! Your complement method isn't quite right. Try again.")
    return;
   
 
  print("Trying to transcribe...")
  transc = transcribe(Seq(sequence))
  print("Transcribed as: " + str(transc)[0:10] + "...")
  if transc == sequence:
    print("Your transcription is the same as your original sequence! Make sure you are editing the transcribe method, and that you changed the return statement at the end to return the transcription, not the original sequence.")
    return;
  if transc == str(Seq(sequence).complement().transcribe()):
    print("You're making a common mistake. You're attempting to transcribe the complement sequence. Try again.")
    return;
  if transc == str(Seq(sequence).transcribe()):
    print("Success! Move on to the next section.\n")
  else:
    print("Oh no! Your transcribe method isn't quite right. Try again.")
    return;


  print("Trying to check if sequence is present...")
  orig = 'ACGTGT'
  sub = 'CGT'
  test1 = checkSubstring(Seq(orig), sub)
  test2 = checkSubstring(Seq(sequence), "ATGGAGCTGACTGTGGAGGCATG")
  print("Found subsequence? " + str(test2))
  if (test1 == True and test2 == False) or (test1 > 0 and test2 < 0):
    print("Success! Move on to the next section.\n")
  else:
    print("Oh no! Your checkSubstring method isn't quite right. Try again.")
    return;


  print("Trying to calculate GC content")
  gcVal = getGC(Seq(sequence))
  print("Reported GC content " + str(gcVal))
  if gcVal == GC(Seq(sequence)):
    print("Success! You're done!\n")
  else:
    print("Oh no! Your getGC method isn't quite right. Try again.")
    return;

  print("####################")
  print("#### Great Job! ####")
  print("####################")

main()
