# Python2Java [v0.8]
***


This project came about after I had written about 2,000 lines of code in python, and realized I wanted to make an Android game instead. I really didn't want to rewrite everything from scratch, so I wrote a regex parser that converted python to java. 

Obvisouly, this code does absolutely no type inferencing, safety checking, or anything of that sort. The primary purpose was to ease the pain of adding braces and parentheses everythwere, and appending semicolons to all lines.

In my particular scenario, this code correcly processed about 80% of my project. I then opened up the code in an IDE, fixed all syntax errors, added imports and types, and the project worked.

### Usage

	$ python3 python2java.py SCRIPT_TO_CONVERT.py



#### License

`Python2Java` is licensed with GPL

#### Contributors
Ivan Smirnov (http://ivansmirnov.name)
