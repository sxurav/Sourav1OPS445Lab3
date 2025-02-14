#!/usr/bin/env python3
'''Lab 3 Part 2 script - free disk space retrieval'''
# Author ID: sourav1

import subprocess

def free_space():
    # Run the df command to get the disk space
    p = subprocess.Popen(['df', '-h', '/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Capture the output and any error
    output, error = p.communicate()

    if error:
        return f"Error: {error.decode('utf-8').strip()}"
    
    # Decode the output from bytes to string and strip extra spaces/newlines
    output = output.decode('utf-8').strip()

    # Split the output by lines and take the second line, which contains the disk info
    lines = output.splitlines()
    if len(lines) < 2:
        return "Error: Unexpected output from df command"
    
    # The second line contains the disk usage information
    line = lines[1].split()

    # The available space is in the 4th column (index 3)
    return line[3]

if __name__ == '__main__':
    print(free_space())
