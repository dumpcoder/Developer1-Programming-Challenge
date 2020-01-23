# Developer1-Programming-Challenge
HEB Developer1 Programming challenge
![Console](https://raw.githubusercontent.com/dumpcoder/Developer1-Programming-Challenge/master/sample.gif)
# Version Support
  I created and tested this programming challenge using Python 3.7.3.
Please use this version or a version that supports python's sorted function and f-strings.

# Installing
In order to install and use this program as a enviorment command run the following commands on a terminal (Tested on Mac OS)</br>
</br>
<b>
1) git clone https://github.com/dumpcoder/Developer1-Programming-Challenge.git</br>
2) cd Developer1-Programming-Challenge</br>
3) sudo cp histogram.py /usr/local/bin/histo</br>
4) sudo chmod 777 /usr/local/bin/histo</br>
</b>

# Usage
<p>Once this program is installed as a command, a argument needs to passed. This is of course the input filename<p>
  e.g <b>> histo input.txt</b>
<p>Optionally a second argument can passed to name the output file. If this argument isn't passed the default
  ouput filename will be <b>output.txt</b></p>
  e.g. <b>> histo input.txt custom.txt</b>

# Approach 
 <p> Due to the length and low complexity of the programming challenge I decided the
procedural programming paradigm was best suited. Yes an objected oriented approach could of
made the code cleaner, but I think Python is better suited for procedural programming. 
  In my procedural programming approach I divided each task into it's own function in order to
bulid layers of abstraction. In the top layer of abstraction there are only three task(functions):
get words from file, create histogram and get justification length(this is done at the same time),
and write histogram to file.</p>

# Challenge Extended
<p>To make this programming challenge a practal piece of software, that is a command line application,
a filename would be given as an argument instead. This can be done using python's argparse libary, 
which is able to read any arguments passed in the console before executing the program.</p>
e.g  ~>histo input.txt
<p>Even better argparse can even handle flags/options like outputing to a specific filename</p>
e.g ~>histo input.txt customFilename.txt
