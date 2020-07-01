# Challenge 1

## Welcome
Welcome to Week 4 of the Crash Course! This will be our final session this quarter; good luck with finals, and we'll see you in Winter.

This week's lesson is, in some ways, a one-question "midterm" that covers the skills you've learned in Weeks 1-3. It's designed to be more challenging than anything we've done so far, so don't be discouraged if you have to think things over (and fail) before succeeding!

## Instructions
### Coverage
We assume that you've already covered (and only covered) all three of our previous sessions. For your reference, they're linked here: [Week 1](/1_Welcome.md) [Week 2](/3_AdvancedTerminal.md) [Week 3](/5_Biopython.md). The techniques for solving the problem below are, with 100% certainty, covered in the previous three lessons. 

*Note: This does not mean that they are explicitly mentioned in one of our previous lessons. Recall that we emphasize finding specific commands, options, and tools on your own. However, we have covered the core concepts before.*

### Logistics
The problem below does not specify *how* you should solve it. Instead, we'll present you with a task to perform and you'll need to determine the output.

Additionally, you'll never need to download any software. Everything you need is on EC2.

### Getting Help
In the real world, you're often on your own when you're stuck and need help. Reading through Google searches, documentations, tutorials, and manuals is a real life skill. 

However, we don't just want to throw you off the deep end. If you do get stuck on something and you can't figure it out, you can draft and email and send it to Sabeel. Provide a specific description of 1) what you're trying to accomplish 2) what issue you're running into 3) what you've already tried to troubleshoot it. If we find many common issues, we'll send out an FAQ/hints email on Sunday.

### Good luck, have fun!

## The Problem
We've previously described how and why we sequence DNA. The raw output of these sequencing machines are [FASTQ](https://support.illumina.com/bulletins/2016/04/fastq-files-explained.html) files. Recall that each base that a FASTQ file contains is paired with a quality score that's encoded in [ASCII](http://www.asciitable.com/) (proportional to how confident the machine is that the base was identified correctly). We, of course, do not want to have our downstream analyses tainted by low-confidence sequences. 

There are various techniques for cleaning up such raw data. Your goal here is to implement one possible method: We will only keep reads if:
```
1. No base in the read has a quality score (strictly) less than 50
2. The average base quality is (strictly) greater than 68
```

Our goal is to output a count of the number of reads that we kept.

As an example, imagine our FASTQ file contains only two sequences, each with three characters:
```
@SAMPLE1
AGG
+
DEF
@SAMPLE2
TGC
+
BCD
```

@SAMPLE1 has an average quality score of 69 (from the average ASCII of `DEF`), and no character is under 50. We will keep this sequence.
@SAMPLE2 has an average quality score of 67 (from the average ASCII of `BCD`), and no character is under 50. We will not keep this sequence.

The output, therefore, would be 1.

Make a copy of your input FASTQ file, available at `~/../smansuri/raw.fastq`. Have fun!

<details>
  <summary>Just getting 0 as your count over and over? Click me!</summary>
  
  Newline characters have an ASCII value of 10.
</details>

## Submitting Your Solution
First, a sanity check. Your answer should be in the mid-900's. 

If your answer matches these criteria, send Sabeel an email titled **[UBIC] Completed Week 4** containing your count.

## Congratulations! You've completed Week 4 AND Quarter 1 of the Bioinformatics Crash Course.

### Next, try our [fifth lesson](/8.1_Alignment.md)
