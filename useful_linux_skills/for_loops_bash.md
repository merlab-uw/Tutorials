# For loops in bash (the most fun kind of loop!)

In large genomic datasets, we might have data from hundreds of individuals. Thus, we need an efficient way to process all of these files without having to write a separate line of code for each file. `For loop`' are one way to do this.

A ‘for loop’ is a bash programming language statement which allows code to be repeatedly executed. Also check out this great tutorial from [Software Carpentry](https://swcarpentry.github.io/shell-novice/05-loop/index.html) for an in-depth exploration of for loops.


The basic syntax of a `for loop` is as follows

``` bash

for thing in list_of_things
do
    operation_using $thing    # Indentation within the loop is not required, but aids legibility
done

```

When the shell sees the keyword `for`, it knows to repeat a command (or group of commands) once for each item in a list. Each time the loop runs (called an iteration), an item in the list is assigned in sequence to the variable, and the commands inside the loop are executed, before moving on to the next item in the list. Inside the loop, we call for the variable’s value by putting `$` in front of it. The `$` tells the shell interpreter to treat the variable as a variable name and substitute its value in its place, rather than treat it as text or an external command.

## Useful tips:
- When using variables it is also possible to put the names into curly braces to clearly delimit the variable name: $filename is equivalent to ${filename}
- Give files consistent names that are easy to match with wildcard patterns to make it easy to select them for looping.

## A simple example
In this example, we will print the file name of every file ending in ".txt" in a directory, and then also print the first several lines of that file. Note the use of the wildcard (asterisk) at the beginning of the `for loop`.

``` bash

for MYFILE in *.txt 
do
  echo $MYFILE #print filename
  head $MYFILE #print the first slines of filename
done

```

## An application of a `for loop` to run fastqc

Let's say you have some sequencing (.fastq) files and you would like to analyze them using the program FastQC. Here is how you might do that using a `for loop`:

``` bash

# this for loop will run FastQC on all files in a directory

for MYFILE in *.fastq
do
	fastqc -f fastq --extract $MYFILE
done
```
