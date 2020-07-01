# Bioinformatics x Python (v2)

## Welcome

Congratulations! After your hard work honing your Unix and Python skills, you've been selected for a bioinformatic research project! Soon, you're going to be trusted with genetic data from an unknown source. Your goal will be to use bioinformatics to determine where this data came from.

## Warm Up (Packages)

Before you're allowed to work with real genetic data, you'll need to familiarize yourself with Python packages. Think of packages as Python programs someone else has written that you can borrow and use for your own purposes.

For example, earlier you determined the GC content of your sequence by writing your own algorithm. Instead, it's a lot easier to find a Python package that already has a built-in GC counter, and just run it by doing something like `sequence.count_gc()`, for example.

The Python package we'll be using for our bioinformatics purposes is called Biopython. This is already installed on our cluster. If it wasn't, you could install it by doing (DO NOT ACTUALLY DO THIS): `pip3 install --user biopython`.

Instead, prove to yourself that Biopython is already on the cluster by doing:
```
pip3 list
```

## Warm Up (Biopython)

Great, we have Biopython. Let's figure out what it does and how to use it.

### Seq Objects

Much like the fundamental building block of genetics is DNA, the fundamental building block of Biopython (at least for what we're doing) is the Seq object. As we move forward in the course, we'll introduce other Biopython features.

First, you'll need to import the Seq package (which is part of the Biopython library). This gives you access to use the Seq object in your file:

```python
 from Bio.Seq import Seq
```

Next, create a Seq object (think of that as a nucleotide sequence) and assign it to a variable:
```python
rna = Seq("AGUACACUGGUG")
```

Now, print out that variable:
```python
print(rna)
```

The output (while boring) is probably what you'd expect--the sequence you specified. But, as you know, you could have done the same thing with a simple string! What makes Seq's especially useful?

### Biopython Methods

The answer - methods! See, the Seq object knows what's inside is either DNA or RNA, so it has specific genetics-related methods you can easily use! For example, you can translate this RNA! Do:

```python
print(rna.translate())
```
Check out [this table](http://www.fao.org/3/y2775e/y2775e0e.htm) to see what amino acids this translated to.

*Note: Methods belonging to the Seq type will all be executed in the format above: SeqObj.method(). All but one method you'll use today will be in this format. The other is a method outside the type, which usess Seq as a parameter: method(SeqObj).*

## The First Glimpse

### Access

You'll be using the same genetic data as before. This time, instead of having various files for various methods, we're going to be using just one file. Isn't that handy? Copy it to your directory:
```
cp ~/../smansuri/biopython.py .
```

This program will provide you with feedback as you progress through the next few steps. Run the program as you complete each step. You'll find the [Biopython package documentation](http://biopython.org/DIST/docs/api/) useful.

*Hint: You really don't want to look through this vast documentation. Can you figure out which specific sub-packages the `biopython.py` file uses, and only look for that documentation? Ask an instructor if you're stuck for more than 3 minutes.*

*Hint 2: Every single task below can be completed in one line of code. Although you need not be this efficient, be wary of writing long methods. The whole point of Biopython is that you don't need to think about any of the logic; it's all done for you.*

## Transcription Simulation

### Reverse Complement

Follow the instructions in the file.

### RNA Transcription

Follow the instructions in the file.

## A Potential Breakthrough

Recall the two markers that could suggest your unknown sample may, in fact, be related to the one seen in rats:
1. The sequence "ATGGAGCTGACTGTGGAGGCATG" is often present.
2. The GC Content is above 55%.

Follow the instructions in the file.

### Congratulations! You've completed Week 3 of the Bioinformatics Crash Course.

### Next, try our [fourth lesson](/7_Challenge1.md)

#### Credits
Exercises are adapted from [Rosalind](http://rosalind.info), the official [Biopython tutorial textbook](http://biopython.org/DIST/docs/tutorial/Tutorial.pdf), and a [course](http://disi.unitn.it/~teso/courses/sciprog/python_biopython_exercises.html) from the University of Trento.
