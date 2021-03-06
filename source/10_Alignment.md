# Lesson 8: Alignment

## Alignment Basics

Sequence alignment is the process of putting similar regions closer to each other, and inserting gaps (denoted by '-') where there may have been an insertion/deletion event. Identifying regions of similarity can help us identify structural, functional, or evolutionary relationships between sequences.  

There are hundreds of alignment methods for different types of information (DNA vs amino acid), different uses (finding common domans vs comparing homologous genes), and different special cases (antibody sequences, viral sequences). If you are interested in learning details about how some existing methods work (this is BENG 181 material): the most generic DNA alignment method is a pairwise dynamic programming method called [Smith-Waterman](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm), alignment of many sequences (multiple sequence alignment) can be done by [Fast Fourier Transforms](https://en.wikipedia.org/wiki/MAFFT), and alignment for accurate amino acid sequence homology is done by [HMM profile alignment](https://en.wikipedia.org/wiki/HMMER).

**This lesson will focus on hands-on learning of three types of alignment: global, local, and multiple sequence alignments.**

## Pairwise Alignemnt

Pairwise alignment is the alignment of one sequence to one other sequence. In order to look in detail at the usefulness of different types of alignments, we will start by looking at pairwise alignment methods implemented with the [Smith-Waterman](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm) method.

### Global Alignment

In this case, the word "global" just means that the **entire** first string is aligned as best as possible to the **entire** second string. It's used to compare two homologous sequences, like comparing the same gene between individuals or species. 

Make a new Python file ```aligners.py``` and import some stuff:
```
# Import pairwise2 module
from Bio import pairwise2

# Import seq objects
from Bio.Seq import Seq

# Import method for formatting alignments
from Bio.pairwise2 import format_alignment

```

Define strings ```TGCCTTAG``` and ```TGCTTGC``` and using global alignment on them:

```
pairwise2.align.globalxx()
``` 

The alignment method returns a list of the most high scoring(good) alignments. You can print those out by iterating through the alignments with a for-each loop and print them out one by one. Use this syntax to make them look better during printing:

```
print(format_alignment(*alignment_name))
```

What is that asteriks? In different languages an asteriks has different meanings, but in Python it denotes a variable quantity of arguments. In other words, methods that want this asteriks are capable of accepting either one, maybe two, or maybe more arguments(inputs). 

### What exactly is a good score? Why is one alignment better than another? 

Glad you asked! If you look at the score printed out below each alignment, you will notice that the score is coincidentially identical to the number of nucleotides that match between the two aligned sequences. The alignment we tried gives gaps, insertions, and deletions a score of zero and matches a score of one. Other alignments may have more complex behaviors, including negative scores for insertions/deletions, custom scores based on which nucleotide is mismatched with which, and more. There are several modes of alignment available on BioPython, each with customizable scoring. Look [over here](http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html) if you want to see the range of what BioPython has to offer.

Take the two strings ```ATGCGGCCATTATAAGTGGTCTCT``` and ```GATTATAATT```, for instance. In case you want to reward +10 for matches, -4 for mismatches, you could use:
```pairwise2.align.globalms(str1, str2, 10, -4)```
Now suppose you add gap penalty, deduct 3 for opening a gap (an indel not preceded by an indel), and deduct 2 for extending a gap (an indel preceded by an indel).
```pairwise2.align.globalms(str1, str2, 10, -4, -3, -2)```
For now, let us use +1 for matches, -1 for mismatches, -1 for opening a gap, and -1 for extending a gap.
### Local Alignment

While the Global alignment method above gave us all the highest score alignments, we might not want any of them. Do you think it is fair for strings ```ATGCGGCCATTATAAGTGGTCTCT``` and ```GATTATAATT``` to be aligned from the begining of both strings to the end of both strings? Notice that starting at index 7, ```"CATTATAAGT"``` in the first string looks more similar to the second string than any global alignment if we ignore the indel penalties at the flanking ends of the second string aligned and could have been a good place to find a conserved region.

The word "local" means the best alignment between two **subsequences**. This method can be used when looking for a conserved gene between two otherwise very different organisms. Aligning the messy differences between two different species is not useful, but finding two subsequences (two genes) that the species have in common without aligning the whole sequences can be very useful. 

Now, let's compare how these strings align with globally vs locally.
(Yes, there is a ```pairwise2.align.localms()``` function in biopython module)

Looking at the matching nucleotides in global and local alignments of these string, which one makes more sense? Does it make sense to care about the matches the global alignment has at the very end of the sequences? 

## Multiple Sequence alignment 

Multiple sequence alignment aligns multiple sequences, but its inner workings are a bit complicated (my way of saying I do not know them well enough to teach them) so we are just going to focus on their applications. This type of alignment is used on a large number of more or less related sequences in order to infer homology and build evolutionary trees. My multiple sequence aligner of choice is mafft, which can be called from inside python.

Grab [```D_db.fasta```](https://drive.google.com/file/d/1qHc1__7e5em8z4AS9D7hygCFNnIo8MkW/view?usp=sharing) and [```J_db.fasta```](https://drive.google.com/file/d/1wz7S4CgbhHBujx134MCjKahMAKPuPslr/view?usp=sharing)
```shell
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1qHc1__7e5em8z4AS9D7hygCFNnIo8MkW' -O D_db.fasta
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1wz7S4CgbhHBujx134MCjKahMAKPuPslr' -O J_db.fasta
```

Now align them with the default settings on mafft:  
```
import subprocess

in_file = "D_db.fasta"
subprocess.call(["mafft", "--out", "aligned.fasta", in_file])
```

D_db.fasta and J_db.fasta are the databases of known human diversity and joining genes, respectively. These genes are building blocks of the heavy chain on an antibody. We can see that the J's align pretty neatly, with some deletions, while the D alignment is a mess - many mismatches and gaps. This clearly indicates that J genes are much more highly conserved than D genes, which you probably guessed from their names. Find answers to your questions about heavy chains [over here](https://en.wikipedia.org/wiki/V(D)J_recombination)

Now that we are familiar with what alignment has to offer, let us get hands-on with a specific implementation: 

## Codon Alignment
[Challenge: Codon Alignment](/8.2_Codon_Alignment.md)

This challenge describes a method of alignment that can be used to track the differences between sequences on the codon level. The goal is achieved with mutliple sequence and some basic sequence manipulation tricks. 
