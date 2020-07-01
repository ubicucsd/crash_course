# Bioinformatics x Python

### EC2: Please use the EC2 host for this week's lesson.

## Welcome

Congratulations! After your hard work honing your Unix and Python skills, you've been selected for a bioinformatic research project! Soon, you're going to be trusted with genetic data from an unknown source. Your goals will be to use bioinformatics to 1) analyze features of the data and 2) determine where this data came from.

## Warm Up

Before you're allowed to work with real genetic data, you'll need be familiar with [command line](/2_LinuxTerminal.md) and [Python](/4_Python.md) basics. 

Review these materials before moving forward, especially creating, editing, and writing Python3 files. Additionally, create and enter a `week3` directory to contain all the work you'll do today

## The First Glimpse

### Access

Great! You've now been granted access to the data you're tasked with identifying. Copy it to your working directory:
```
cp ~/../smansuri/unidentified.unknown .
```

As you've always done, explore the data to get a sense of what you're working with. (*This is a good check to see if you're understanding what to do. What are some techniques we've used in the past?*).

### File Extenstion

The file you downloaded is called `unidentified.unknown`. Having worked with genetic data files before, you know what type of file this is. Change the file extension from `.unknown` to the appropriate extension. *For example, if you thought this was a PDF file, you would rename the file to `unidentified.pdf`.*

## Transcription Simulation

### Complement

It's clear that this file contains a DNA sequence. Your colleague reminds you that DNA is double stranded and runs anti-parallel. 

This means that a sequence "ACGT" from 5' to 3' ([what's this?](https://en.wikipedia.org/wiki/Directionality_(molecular_biology))) is paired up with another sequence "TGCA" from 3' to 5'. These two sequences are called **complements** of one another. You can read more about DNA complementarity [here](https://en.wikipedia.org/wiki/Complementarity_(molecular_biology)).

She recommends that you also extract the complement of the unidentified sequence. Run the following on the command line:
```
cp ~/../smansuri/comp.py .
```
This will add an incomplete Python program called `comp.py`. Follow the instructions to determine the complement.

Once you get the program running correctly, you'll see a success message and a file called `unidentified_complement.fasta` created.

### RNA Transcription

RNA is created by taking the template strand (in our example, the complement strand), and using an RNA polymerase to create a complement of the complement, but with Uracil (U) instead of Thymine (T). This means the RNA will have the same sequence as the original strand, but with U's instead of T's. For example:
```
Original:   ACTG
Complement: TGAC
RNA:        ACUG
```

Run the following on the command line:
```
cp ~/../smansuri/transcribe.py .
```
This will add an incomplete Python program called `transcribe.py`. Follow the instructions to transcribe the complement to RNA (*Hint: This will be very similar to your implementation in comp.py*).

Once you get the program running correctly, you'll see a success message and a file called `unidentified_rna.fasta` created.

*Note: The template strand is read from 5' to 3', which is the orientation of our complement data. Therefore, you don't need to do any sort of reversal. You'll soon see another instance where you will need to reverse.*

## A Potential Breakthrough

You compare this RNA sequence with some others in your lab's database. The transcribed RNA you submitted has a sequence that's fairly similar to one seen before in rats. 

There are two markers that could suggest your unknown sample may, in fact, be related to the one seen in rats:
  1. The sequence "ATGGAGCTGACTGTGGAGGCATG" is often present.
  2. The GC Content is above 55%.

Determine if this sequence appears in your sample, and see if the GC content is in the range you expect.

## BLAST

Your colleague notices what you've been trying to do. She suggests you use an online tool called [NCBI BLAST](https://blast.ncbi.nlm.nih.gov/BlastAlign.cgi) to compare your sequence to a database of sequences online. Click the link and use the Nucleotide Blast tool to copy-paste the **original DNA sequence** to determine what this sample is.

Great! You've identified what organism this comes from. What exactly is this organism? Is there anything particularly interesting about it?

## Let's Try That Again

What you just did--exploring an unknown sequence--is one of the simplest and most common bioinformatic tasks. Ask yourself this: does everyone who wants to do this have to write their own algorithms, manually parse through sequences, and copy-paste into a web browser? 

Nope. Let's explore a far more efficient method in the [second part of today's lesson](6_BiopythonV2.md).
