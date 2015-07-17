#import numpy as ny
#import os as os
#s = "uxwrpxlwocnimr";
s="axabc";
count = True;
lstring = "";
length = len(s)
for i in range(0,length):
    count = True;
    for j in range(i+1,length):
        if(s[j-1] > s[j]):
            subStr = s[i:j];
            if(len(subStr) > len(lstring)):
                lstring = subStr;
            count = False;
            break;
    if count:
        if len(s[i:length]) > len(lstring):
            lstring = s[i:length];
print "Longest substring in alphabetical order is:",lstring;