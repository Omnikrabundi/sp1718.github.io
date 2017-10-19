"""
This exercise should (re-)introduce you to basic interactions 
with Python built-in types, functions, and the format of the
exercises in this course. We'll have a look at numbers, strings, 
lists, and regular expressions (=regex) in some simple exercises.

The instructions to a function are given in the comment section
within the function; the 'pass' statements are the slots that 
are to be replaced with correct code.
You can do command-line test runs with this code by entering
> python3 -m doctest -v hw01_basics/basics.py <
(when you are in the src directory.)


If you're stuck, try finding a solution online or ask your fellow
students. The internet is full of tips and tricks for almost every 
coding problem, and the best coding uses collective brain power.
Happy coding!
"""
#===BASICS AND NUMBERS====================================================


def hello_world():
    """ Print the string 'Hello, world!'.
    >>> hello_world()
    Hello, world!
    """
    pass


def expon(x, y):
    """ Return the x to the power of y.
    >>> expon(2, 3)
    8
    >>> expon(-2, 3)
    -8
    >>> expon(2, -3)
    0.125
    """
    pass


def dividable(x,y):
    """ return True or False wether x is dividable by y.
    >>> dividable(15, 3)
    True
    >>> dividable(15, 6)
    False
    >>> dividable(15, -3)
    True
    """
    pass

#===STRING OPERATIONS====================================================

def hello(name):
    """ Print "Hello, >name<!".
    >>> hello("Ludwig")
    Hello, Ludwig!
    """
    pass


def wordlength(w):
    """ return the length of the string w. You can use built-in functions.
    >>> wordlength("excalibur")
    9
    >>> wordlength("")
    0
    >>> wordlength('b')
    1
    """
    pass


def caps(w):
    """ return w, but IN ALL CAPS.
    >>> caps("ice")
    'ICE'
    >>> caps("Tiger")
    'TIGER'
    >>> caps("$lim shady")
    '$LIM SHADY'
    >>> caps("Waschbär")
    'WASCHBÄR'
    """
    pass

def substring(v, w):
    """ Return True or False whether v is a substring of w.
    >>> substring("art", "Earth")
    True
    >>> substring("de 1", "Die Wilde 13")
    True
    >>> substring("Au", "Kaufrausch")
    False
    """
    pass # checking whether there was a hit


#===LIST OPERATIONS====================================================
listOne   = ["this", "is", "a", "simple", "list"]
listTwo   = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def thirdElem(liste):
    """ return the third element of liste.
    >>> thirdElem(listOne)
    'a'
    >>> thirdElem(listTwo)
    2
    """
    pass


def lastElem(liste):
    """ return the last element of liste.
    >>> lastElem(listOne)
    'list'
    >>> lastElem(listTwo)
    55
    """
    pass


def firstHalf(liste):
    """ return the first Half of liste. With uneven-lengthed lists,
        return the smaller part. (tip: use integer division)
    >>> firstHalf(listOne)
    ['this', 'is']
    >>> firstHalf(listTwo)
    [1, 1, 2, 3, 5]
    """
    pass


def concatenate(liste1, liste2):
    """ return a list that contains all elements of liste1 
        followed by all elements of liste2.
    >>> concatenate(listOne, listTwo)
    ['this', 'is', 'a', 'simple', 'list', 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> concatenate(listTwo, listOne)
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 'this', 'is', 'a', 'simple', 'list']
    """
    pass

#===LOOP OPERATIONS====================================================

def isNegative(k):
    """ Return True if k is smaller than 0 and False otherwise.
        Use if-/else-statements for this problem
    >>> isNegative(-2)
    True
    >>> isNegative(3)
    False
    >>> isNegative(0)
    False
    """
    pass


def printElements(liste):
    """ print each element in liste. You can use a for-loop for this problem.
    >>> printElements(listOne)
    this
    is
    a
    simple
    list
    """
    pass

def countToZero(k):
    """ Print out the numbers counting from k to 0, excluding 0.
        If k is negative, count 'up' to 0, excluding 0.
        You can use a while-loop for this problem.
    >>> countToZero(3)
    3
    2
    1
    >>> countToZero(-2)
    -2
    -1
    >>> countToZero(0)
    """
    pass


#===REGULAR EXPRESSIONS====================================================
import re # module containing many useful Regex methods

def noVowels(w):
    """ Return True or False whether w contains no vowels.
    >>> noVowels("Neu-Halledau")
    False
    >>> noVowels("Öl")
    True
    >>> noVowels("Krk")
    True
    >>> noVowels("H00l4 h00p")
    True
    """
    #rex = re.compile("[aeiouAIEOU]")
    pass
  
  
def umlautsAndPunct(w):
    """ Return True or False whether w contains umlauts (äöü)
        and a punctuation mark (.!?) at the end. 
    >>> umlautsAndPunct("Motörhead!")
    True
    >>> umlautsAndPunct("Yoko Ono schwimmt im Mississipi")
    False
    >>> umlautsAndPunct("Wubba Lubba dub dub!")
    False
    >>> umlautsAndPunct("Flynn Lynch? Gräbt Glück")
    False
    """
    pass
    
#=======================================================


