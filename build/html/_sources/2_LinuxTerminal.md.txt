# The Linux Terminal

Bioinformatics is often memory and computation intensive, so we'll be outsourcing our computational work to a bigger computer called a server. This server will run on the Linux operating system. (This is no different than your laptop running on a Windows or Mac operating system.)

***Why Linux?*** The majority of servers run on Linux, a free operating system which inherited its predecessor's (GNU's) mission to give users freedom. Linux is completely open source, allowing users to see and modify any part of its inner workings. Linux is also extremely stable, allowing servers to be up for years at a time without restarting.

## How Can I Connect?

***Secure Shell(ssh)*** is a protocol which creates a secure channel for two computers to communicate. This is how we will connect to our server.

**Mac or Linux users:** skip to **Exploring the Server**. Your device has a built-in ssh client!

**Windows users:** We do not like Windows terminals, you do not like Windows terminals, no one likes Windows terminals. Go to [The Putty website](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and download Putty. A window should appear to guide you through the installation.

## Exploring the Server

We've created an account for you on our server (which is, by the way, called EC2). Your username for EC2 is the same as your UCSD username. Your password has been emailed to you.

### Connecting

**Mac or Linux:** Open an application on your device called "Terminal". This should open up a window that prompts you to enter some text. Copy-paste this command into the terminal: ```ssh your-username@[the host for this week's lesson]```. Replace "your-username" with your UCSD username, and "[the host for this week's lesson]" with the EC2 host found on the front page of today's lesson, and press enter. You're now connected to EC2!

*Note: you may need to use Ctrl-shift-V to paste into terminal.*

**Windows:** Open putty, paste ```[the host for this week's lesson]``` into the Host Name section (replacing "[the host for this week's lesson]" with the EC2 host found on the front page of today's lesson) and select port 22 and SSH on that same page. Type any name of your choice under Saved Sessions and click the Save icon on the right. Now, press Open and type your username and password when prompted. 

**Password:** ubic2019 . Unless you had an account last year, in which case it is the password you made. 

### Your First Commands

1. Discover your identity. Type `whoami` into the window that just opened up and hit `enter`. And just like that you're talking
with your computer, you bioinformatician, you.

2. The password we provided you with isn't particularly safe. Let's change your password using the terminal. Type ```passwd [your-username]``` and follow the prompts to set your own password. (Replace "your-username" with your username.)

### So... Commands?

Commands are things you can type into the terminal to perform different actions. There are an endless number of commands, each with a ridiculous amount of options, so **do NOT attempt to memorize them on the first try**. 

How do you know what command to use to do sometihng you want? Simple: for now, we'll explain commands as you need them. Actually learning (or memorizing) the commands will come naturally from repeated use of the terminal.

*Note: Anytime you need a refresher on what a command does, type the command line with the --help option like so: ```ls --help```. If that does not work, try ```man ls```. One (or both) of these will pull up information on how to use the command. Can you figure out what the ls command does?*

### What Am I Looking At?

When you open up your laptop, you are presented with your "Desktop". When you open up a terminal (or connect to a server via ssh!), you are presented with your "Home".

When you want to open up the "Pictures" folder on your laptop, you find the folder labeled "Pictures", and then open it. Uh-oh... we don't know how to (1) find something or (2) open something!

Let's take a step back and talk about all the files in your computer are organized. As you know, you can have different files stored in different places on your computer. You do this by creating folders (inside of other folders), and creating files inside of them. This is **exactly how our server works**, except we call folders "directories".

Similar to how "Desktop" is a folder on your computer, "Home" is a directory on your account on the server. And similar to how your "Desktop" can have folders created in it, so can "Home". You can look at what's inside with the `ls` command, which is short for "list". Type `ls` to see what's in your "Home" directory. (We now know how to find something!)

### What Can I Do?

There's nothing in your home directory! Let's change that by creating a directory. You can do this with the `mkdir` command. Let's create a directory called "software" by doing `mkdir software`. Confirm that this worked by looking at your home directory again.

Now that we can find the "software" directory, let's move into it (the equivalent of opening a folder on your laptop). Type `cd software` to **c**hange **d**irectory to software. Next, type `ls` and confirm that nothing is in this freshly created directory. Create another directory here called "docs" (yes, directories can contain other directories, much like folders can contain folders!).

Great! You can now make a directory and enter it. The last step is to exit the directory. You can do this by just telling the terminal to change directory to whatever contains the current directory (i.e. the parent directory). The alias for the parent directory is `..`. Confirm you've moved back to the home directory using `ls`.

On your laptop, if you want to get to a deeply nested folder, you have to keep unfolding the layers by opening multiple folders. Wouldn't it be nice to be able to just get directly to a folder? We can do this using `cd` by specifying multiple layers we want to change into. For example, we just created a "docs" inside of "software". We can get into this directory by typing `cd software/docs`, where the terminal will recognize "/" as a sign that what follows will be inside of "software".

Finally, let's go back home. You might think that `cd ../..` will take you there, and you would be right! You'd look at the parent's parent, which is the home directory. However, there's an easier way. Much like `..` is an alias to the parent directory, `~` is an alias to your home directory. Simply do `cd ~` from anywhere and you'll end up home!

`.` is a special alias too! Can you figure out what it refers to? Try `cd .` and see where you go.

### [Your Turn!] Investigate Genetic Data

Let's get to work with some real genetic data!

Start in your home directory. Create and enter a directory called "week1". Then run the following command:
```shell
wget https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta
```

You've just downloaded a file full of a bunch of genetic data! You can take a peek at the first few lines by doing `head ls_orchid.fasta`. Your job is to analyze this file.

You have 3 tasks:

1. Print all the contents of the downloaded dataset to terminal window ("standard output")
2. Print how many lines there are in the file
3. Print how many lines there are in the file **THAT CONTAIN GENETIC DATA** (no headers)

The commands cheat sheet below and the hint above about deciphering commands you're not familiar with are your friends. Good luck!

### Once you're done, show your answers to an instructor to get checked off. Congratulations! You've completed the first lesson of the Bioinformatics Crash Course!

### Next, try our [second lesson](/3_AdvancedTerminal.md)

## Commands Cheat Sheet

```ls```(list files) Print out the contents of a directory. 

```mkdir```(make directory) Create a directory with the same name as the argument you give it.

```cd```(change directory) Change directory to whatever is specified.

```head``` Print the beiginning of the specified file to the terminal.

```cat``` Print whatever follows to the terminal. If a file name is specified, print the contents to the terminal.

```wc``` (word count) Print the number of words in the file name specified after the command.

```grep``` Print out lines matching the specified conditions.
