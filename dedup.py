#!/usr/bin/env python

import argparse
import re 

def get_args():
    parser = argparse.ArgumentParser(description="A program to hold input+output filename and umi list")
    parser.add_argument("-f", "--filename", help="This is my sorte sam file.", required=True)
    parser.add_argument("-o", "--outfile", help="output file name", type=str)
    parser.add_argument("-u", "--umilist", help="umilist", required=False)
    return parser.parse_args()

args=get_args()
f=args.filename
o=args.outfile
u=args.umilist

def umi_list_builder(umi_filename: str) -> list[str]:
    '''Function to build umilist from STL96.txt'''
    umilist = []
    with open (umi_filename, "r") as f:
        for line in f: 
            # e.g., line = AACGCCAT\n
            line = line.strip()
            umilist.append(line)
    return umilist

my_new_umilist = umi_list_builder(args.umilist) 

def position_changer(flag, cigar, position):
    '''This function calculates where the read should map to the reference and assigns this position to matched reads.
Sample input: 1573, '15S75M', forward
Sample output: 1558 (adjusted starting position)'''
    
    pos = 0    
    matches = re.findall(r'(\d+)([MNDS])', cigar)
    print(matches)
    if((flag & 16) != 16): #if on plus strand
        if 'S' in matches[0][1]:
            adjusted_position = position-int(matches[0][0])
            return adjusted_position
        else:
            return position
    else:
        #for i,match in enumerate(matches):
        if 'S' == matches[0][1]:
            matches = matches[1::]
        for i in range(len(matches)):
                pos+=int(matches[i][0])
        return position + pos 

alignment = set()    
with open (f, 'r') as fh, open (o, 'w') as outfile:
    for line in fh:
        if line.startswith("@"):
            outfile.write(line)
        else:
            #focus on second column
            line = line.split('\t')
            bitflag = int(line[1])
            strand = strandedness(bitflag)
            chromosme = line[2]
            qname = line[0]
            umi = line[0][-8:]
            cigar = line[5]
            position = int(line[3])
            adjusted_position = position_changer(bitflag, cigar, position)
            if umi not in my_new_umilist:
                continue
            if minus_strand:
                position = position_changer(bitflag, cigar, position)
            else:
                if soft_clipped:
                    position = position_changer(bitflag, cigar, position)
                else:
                    position = int(line[3])
            items=(chromosme, strand, position, umi)

        if items in alignment:
            duplicate +=1
            continue
        else:
            alignment.add(items)
            outfile.write("\t".join(line))

        if chrome != prev_chromosome:
            alignment.clear()
            prev_chrome = chrome
print(duplicate)

    
