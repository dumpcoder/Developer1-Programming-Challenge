# Developer1-Programming-Challenge
HEB Developer1 Programming challenge

# Version Support
  I created and tested this programming challenge using Python 3.7.3.
Please use this version or a version that supports python's sorted function and f-strings.

# Approach 
  Due to the length and low complexity of the programming challenge I decided the
functional programming paradigm was best suited. Yes an objected oriented approach could of
made the code cleaner, but I think Python is better suited for functional programming. 
  In my functional programming approach I divided each task into it's own function in order to
bulid layers of abstraction. In the top layer of abstraction there are only three task(functions):
get words from file, create histogram and get justification length(this is done at the same time),
and write histogram to file.

# Challenge Extended
To make this programming challenge a practal piece of software, that is a command line application,
a filename would be given as an argument instead. This can be done using python's argparse libary, 
which is able to read any arguments passed in the console before executing the program. 
e.g  ~>histogram input.txt
Even better argparse can even handle flags/options like outputing to a specific filename
e.g ~>histogram input.txt -o customFilename.txt
