# Name: Jacob
# Evergreen Login: morjac05
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

print 'x**2-5.86x+8.5408'

x={((5.86 + math.sqrt((-5.86)**2-(4*8.5408)))/(2*1)), ((5.86-math.sqrt((-5.86)**2-(4*8.5408)))/(2*1))}
print 'x='
print x


###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
print 'a=', hw1_test.a
print 'b=', hw1_test.b
print 'c=', hw1_test.c
print 'd=', hw1_test.d
print 'e=', hw1_test.e
print 'f=', hw1_test.f


###
### Problem 3
###

print "Problem 3 solution follows:"

print ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))


###
### Collaboration
###

# I work alone.
# Like Batman.
# (I'm Batman.)
# Proofreading credit to David Burke (burdav22)
# (He's not Batman.)
# He didn't actually change anything or have any comments or suggestions,
# I just asked him to look at it.
