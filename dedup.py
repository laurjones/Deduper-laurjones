import argparse
import re 
import pprint

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input filename", required=True)
    parser.add_argument("-o", "--outfile", help="output file name", type=str)
    return parser.parse_args()

args=get_args()
f=args.filename
o=args.outfile

umi_dict={}

def umi_checker(qname):
    '''placeholder... sample in/out'''
    umi_line = re.findall('[ACTGUN]{0,8}',qname)
    umi = umi_line[len(umi_line)-2]
    return umi

def position_changer(flag, cigar, position):
    '''This function calculates where the read should map to the reference and assigns this position to matched reads.
Sample input: 1573, '15S75M', forward
Sample output: 1558 (adjusted starting position)'''
        
    matches = re.findall(r'(\d+)([A-Z]{1})', cigar)
    if((flag & 16) != 16):
        if 'S' in matches[0][1]:
            adjusted_position = position-int(matches[0][0])
            return adjusted_position
        else:
            return position
    else:
         deletions, last s, m, first s (everything except for I's)



