#!/bin/bash
n=1
while read file; do
    echo "part-$n"
    wget -O "part-$n.tar" ${file} -b 
    let "n += 1"
done < /trinity/home/abdulaziz.samra/Fork_VectorMapNet_code/nuSencesLinks.txt
