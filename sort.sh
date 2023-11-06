#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=bgmp               #REQUIRED: which partition to use
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=1                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB

conda activate deduper

#go to python directory
dir="/projects/bgmp/lmjone/bioinfo/Bi624/Deduper-laurjones"
cd $dir

#samtools sort 
samtools sort -O sam -o C1_SE_uniqAlign_sorted.sam  C1_SE_uniqAlign.sam  

/usr/bin/time -v ./Jones_deduper.py -f C1_SE_uniqAlign_sorted.sam -u STL96.txt -o outfile.sam 