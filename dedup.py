import argparse
import re 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input filename", required=True)
    parser.add_argument("-o", "--outfile", help="output file name", type=str)
    parser.add_argument("-u", "--umilist", help="output file name", required=False)
    return parser.parse_args()

args=get_args()
f=args.filename
o=args.outfile
u=args.umilist

def position_changer(bitflag, cigar, position):
    '''This function calculates where the read should map to the reference and assigns this position to matched reads.
Sample input: 1573, '15S75M', forward
Sample output: 1558 (adjusted starting position)'''
        
    pos = 0    
    matches = re.findall(r'(\d+)([A-Z]{1})', cigar)
    print(matches)
    if((flag & 16) != 16): #if on plus strand
        if 'S' in matches[0][1]:
            adjusted_position = position-int(matches[0][0])
            return adjusted_position
        else:
            return position
    else:
        for i,match in matches:
            #print(f'i {i}')
            #print(f'match {match}')
            if i==0 and 'S' != match[1] or 'I' != match:
                pos+=int(i)
        return position + pos 

def strandedness(bitflag)
    '''placeholder'''
    return (bitflag & 0x10) != 0 #checking if minus strand 

umi_list=[]
with open(u, "r") as file:
    for line in file:
        line = line.strip("\n")
        umi_list.append(line)

alignment = set()    
with open (sorted_sam, 'r') as fh, open (o, 'w') as outfile:
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
            if umi not in umi list:
                continue
            if minus strand
