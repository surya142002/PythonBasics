# My Journey Begins...

I already have some experience using Java, C, and C++ from my projects at Purdue.
Maybe a lot of people feel like this, but I believe I am still completely clueless. 

Hopefully documenting my progress will do some good... I will also learn source control.

## Learning Simple Syntax

I have spent a fair deal of time watching tutotials on Python syntax.
It is time to get off my a$$ and actually implement/solidify my knowledge.

https://www.youtube.com/watch?v=rfscVS0vtbw (My Favorite!!)

Shoutout to that guy ^^^

## Simple Projects

I searched around for the best projects to work on and found some simple projects 
which will hopefully give me a good base in Python.

### Project 1: Number Guessing Game

This was very straightforward. 

I had to search how to find a random number...
```python
# random number from 1 to 100 (inclusive)
import random
target = random.randint(1, 100)
```

I also forgot about converting integers to strings before printing them
This is easily done with str() function

When using a for loop or any other situation, range(1, 11) would include numbers from 1 to 10 

### Project 2: Rock Paper Scissors

This was a pretty simple concept because I already understood "random"

I wanted to use a dictionary to store the values

```python
valueDict = {1: "Rock", 2: "Paper", 3: "Scissor"}

# this was how I accessed value from dict
print("Tie Game Both Picked: " + str(valueDict[computer]))
```
I decided to use a function to check the winner.
I forgot that there were no main methods built into python because it is a scripting language.
I needed to define the function before I could use it in my code.

### Project 3: Hangman

I got to play around with strings for this project. 
I figured out how to print without a new line character as well.
```python
print("blah blah", end =" ")
```

I was too lazy to draw a whole hanging dude so I just made
a fake bullet instead. The quit() function is useful to end the program whenever
I need to.

I made use of lists and learned to append and search 
within a list. After learning C, strings are so much
easier to learn in Python. There are so many powerful
functions. 

"in" is also very powerful in if statements. 
I needed this to search whether guesses were accurate.

This was a simple yet fun little project.

### Project 4: Password Generator

This was straightforward and much easier than Hangman.

The only problem I had was figuring out how to efficiently
generate a random letter. I chose to use the String class
for that. 

```python
import random
import string

random.choice(string.ascii_letters)
```

The above code returned a random letter from a-z.

### Project 5: Tic Tac Toe

Tic Tac Toe was a bit more complicated because I had to
develop methods to constantly keep the board updated and
check for winners. 

The concepts were overall straightforward. I made use
of the "continue" command as well as learning how
to increment ranges to have more flexibility in a for loop.

```python
# below code starts at 0 and increments by
# 3 positions (0, 3, 6) 
# Useful in checking for vertical winners
for i in range(0,7,3):
```



