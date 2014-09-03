#!/usr/bin/env python3

import re
import sys

## This script converts python3 source to java source
## Author: Ivan Smirnov


def main():
    # set input and output files
    out_name = sys.argv[1] + "-p2j.java"
    out_file = open(out_name, 'w')
    in_file = open(sys.argv[1], 'r')

    def writeline(string):
        out_file.write(string + "\n")

    prev_count = 0
    for line in in_file.readlines():
        #detect blank lines
        test_line = line.strip()
        if len(test_line) == 0:
            pass
            
        else:
        
            cur_count = 0
            for char in line:
                if char == " ":
                    cur_count += 1
                else:
                    break
            
            if cur_count == len(line):
                # empty line, do nothing
                break
                    
            if prev_count > cur_count:
                # we stepped out a block
                
                # NOTE - if we went from 12 indents to 4, we should add two closing brackets, one at 12 and one at 4
                # FIXME ERROR
                count = (prev_count - cur_count) // 4
                while count != 0:
                    writeline(" " * count * 4 + "}")
                    count -= 1
                pass
                
            if prev_count < cur_count:
                # we stepped in a block. should write open paren
                writeline(" " * prev_count + "{")

            # now run regex suite on the line
            # might cause error if none
            
            line = re.sub("False","false", line)
            line = re.sub("@property","", line)
            line = re.sub("self","this", line)
            line = re.sub("\(this,","(", line)
            line = re.sub("\(this\)","()", line)
            line = re.sub("True","true", line)
            line = re.sub("print\(","System.out.println\(", line)
            line = re.sub("and","&", line)
            line = re.sub("not","!", line)
            line = re.sub("#","//", line)
            line = re.sub("def","public void", line)
            
            
            # handle if elses - add parenthesis
            p = re.compile('(?<=if)(.+)(?=\:)')
            if p.search(line) != None:
                string = p.search(line).group(0)
                string = "( " + string + " ) "
                line = "if " + string + "NOEND"
            
            # finish regex
            line = re.sub(":",'', line) #since brackets already handled
            
            
            
            
            
            # HANDLE """ xxx """ --> /* xxx */ (can do by hand if need be)
            r = re.compile('(?<=\"\"\")(.+)(?=\"\"\")')
            if r.search(line) != None:
                string = r.search(line).group(0)
                string = "/* " + string + " */ "
                
            # add ;
            line = line.rstrip()
            
            
            if len(line) != 0 and line[len(line)-5:len(line)] == "NOEND":
                line = line[:len(line)-5]
            
            else:
                if len(line) != 0 and line[len(line)-1] not in ("(" , "{" , "}"):
                    line = line + ";"
            
            
            # remove extra ; in method declarations
            z = re.compile("public void")
            if z.search(line) != None:
                line = line[:len(line)-1]
                
            
            
            
                
            # update counts
            prev_count = cur_count
            writeline(line)
            
    # file is done, inform user
    print("converted {0} to {1}".format(sys.argv[1], out_name))
    
    
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 p2j.py SCRIPT_TO_CONVERT.py")
        exit

    main()
