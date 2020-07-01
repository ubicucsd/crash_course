# Challenge 2

## Welcome
Welcome to Week 8 of the Crash Course! This will be the final session for the introductory part of our program. We hope that you'll apply for the advanced topics that we'll present in Spring.

This week's lesson is, in some ways, a "final exam" that covers the skills you've learned in Weeks 1-10.

## Instructions
### Coverage
We assume that you've already covered (and only covered) all of our previous sessions. The techniques for solving the problems below are, with 100% certainty, covered in the previous three lessons.

*Note: This does not mean that they are explicitly mentioned in one of our previous lessons. Recall that we emphasize finding specific commands, options, and tools on your own. However, we have covered the core concepts before.*

### Logistics
The problems below do not specify *how* you should solve them. Instead, we'll present you with tasks to perform and you'll need to determine the output.

Additionally, you'll never need to download any software. Everything you need is on EC2.

### Getting Help
In the real world, you're often on your own when you're stuck and need help. Reading through Google searches, documentations, tutorials, and manuals is a real life skill. 

However, we don't just want to throw you off the deep end. If you do get stuck on something and you can't figure it out, you can draft an email and send it to Sabeel. Provide a specific description of 1) what you're trying to accomplish 2) what issue you're running into 3) what you've already tried to troubleshoot it. If we find many common issues, we'll send out an FAQ/hints email on Sunday.

### Good luck, have fun!

## Problem 1
Find the 100th Fibonacci number (without Googling!). 

You may try to write a recursive solution, but it will not run in time. Perhaps this[https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/] can help?

## Problem 2
In the lab, you're often not going to be given an explanation (such as provided above) of how to perform a task. This challenge will test your ability to use your resources (internet, documentation, etc.) to extend phylogenetic analysis given only input and output.

**Input**   
Many times, phylogenetic trees are exported as XML files. XML stands for eXtensible Markup Language, and is used in a wide range of applications that require storage or transport of data in a structured fashion. Provided are two XML files, `single.xml`, containing one phylogenetic tree, and `many.xml`, containing many different phylogenetic trees.

(They'll be downloaded with different names than many or single)  
[many.xml](https://github.com/biopython/biopython/blob/master/Tests/PhyloXML/phyloxml_examples.xml)  
[single.xml](https://github.com/biopython/biopython/blob/master/Tests/PhyloXML/apaf.xml) 

**Output**  
When your program is executed, the following should be printed to the terminal for every tree (from both files):  
* [Tree Name] or "Unnamed"  
* [Tree Description] or "No description"  
* [Phylogenetic tree ordered with deepest clades* on top]  

*Clade depth is defined by the number of terminal nodes.

## Submitting Your Solutions
Send Sabeel an email titled **[UBIC] Completed Week 8** containing your output for the previous 3 problems.

## Congratulations! You've completed the introductory portion of the Bioinformatics Crash Course.
