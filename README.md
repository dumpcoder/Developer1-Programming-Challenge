# Developer1-Programming-Challenge
HEB Developer1 Programming challenge

# Version Support
  I created and tested this programming challenge using Python 3.7.3.
Please use this version or a version that supports python's sorted function and f-strings.

# Installing
In order to install and use this program as a enviorment command run the following commands (Tested on Mac OS)</br>
</br>
<b>
git clone https://github.com/dumpcoder/Developer1-Programming-Challenge.git</br>
cd Developer1-Programming-Challenge</br>
sudo cp histogram.py /usr/local/bin/histo</br>
sudo chmod 777 /usr/local/bin/histo</br>
</b>

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
