# Lesson 3: Advanced Command Line

## Jumping in the Deep End

At the beginning of this course, we said that we believe in active learning. Below are a bunch of exercises in roughly increaisng order of difficulty. [Here's](/extras/2.1_AdvancedCommands.md) a bunch of advanced command line info you might find useful, though Google is probably your best friend.

***Behind the Scenes:** You might wonder, "Why are we being given tasks that we haven't been taught how to complete?" The answer: that's science. One of the most powerful skills in bioinformatics is simply being able to parse documentation to figure out what you need to do. Taking the general knowledge from last lesson and applying it to scenarios you've never seen before is very, very valuable!*

## Assignment
<!--
**(0.) Copy-paste the following command into your terminal in order and hit enter.**
`cp -r ~/../smansuri/week2/ ~`
**1. Enter the directory that was just created**
**2. Name all of the files (not other directories!) inside this directory. How many are there?**
**3. Execute the "instructions" file, and follow the prompts. (hint: `./instructions`)**
-->

Get file1.txt and file2.txt:

File1.txt: 
```shell
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1DozuwGq6nQRSf2Dx6VNXSv6Vha8OMCIM' -O file1.txt
```

File2.txt: 
```shell
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=17kYqxphGrkCK30FQuOUDIXOUhiZvjAMd' -O file2.txt
```
**1. file1.txt contains the text of a Sherlock Holmes book. How many lines of the file does it take to recount his tale in Bohemia?**
*Hint: The table of contents is form line 48 to 70*
<details>
  <summary>Stumped? Click me!</summary>
    
  Does this command give you an idea of what you can search for?
  
  ```shell
  head -n 70 file1.txt | tail -n 22
  ```
  You can also use command `awk` which is a great multipurpose effecitent text processing command.
  ```shell
  awk "NR<70" file1.txt | awk "NR>48"
  ```
</details>

**2. How many lines in file2.txt contain a period? (*Hint: The answer is not 60*)**

**3. Confirm your answers to 2-5 with an instructor or tutor. Then, delete the directory you downloaded in step 0.**

## Your Own File

So far, you've been working with files provided to you. However, for most things you'll want to do moving forward, you'll need to create your own. How do you do that?

### vim

We're going to be using a text editor called "vim". Think of vim as Microsoft Word, but for your command line. You can use vim to open a file containing text or create your own (just like Word!).

Vim is navigated through keyboard commands, which at first are confusing and mostly non-intuitive. However, once you become familiar with using these keyboard shortcuts, vim can become one of the fastest text-editors to use. (Note: An advanced user may also edit the .vimrc file to customize vim to better fit your habits or adjust UI style.)
  
Here is a helpful interactive online resource on learning the vim keyboard commands: [openVim](https://www.openvim.com/)
  
Here's a walkthrough of exactly what you'd need to hit on your keyboard to create a file called "new.txt" that contains "hello there" inside of it:

```
vim new.txt
i
hello there
'esc'
:x
```

<details>
  <summary>Unsure what these commands do? Click me!</summary>
  
  1. `vim new.txt` - Open a file called new.txt in vim. If no file exists in the directory (true for us!) create a new one
  2. `i` - Moves you into insert mode (where you're actually allowed to type) 
  3. `hello there` - Adds text into the file
  4. `esc` - Moves out of insert mode
  5. `:x` - Saves and quits the file
</details>

Use `ls` and `cat` to confirm that you've succeeded in creating this file.

### Your Turn
Create an executable file called `greet.sh` that can be executed to print "Hello World" to the command line. 

<details>
  <summary>No idea where to start? Click me!</summary>
  
  Tackle these subproblems:
  1. What is an executable file?
  2. How do I make a file print "Hello World"?
  3. How can I execute a file?
  4. [Optional, depending on if #3 fails] How can I make a file executable?
</details>

Update your program to print "Hello [your_username]". This should NOT be hardcoded, meaning if your program prints "Hello jsmith" on your laptop, it should print "Hello smansuri" on mine without any changes.
