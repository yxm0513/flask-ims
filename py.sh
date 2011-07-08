#!/bin/bash
# 1. find all pyc files and remove them
# 2. convert all .py .html files with tab to 4 space 

find . -name "*.pyc" -exec rm -rf {} \;
types=(.py .html .css .js)
for t in ${types[@]}
do
    echo TYPE: ${t}
    files=(`find ./ -name "*${t}"`)

    for f in ${files[@]}
    do
        echo ${f}
        dos2unix ${f} 1>/dev/null 2>&1
        sed 's/	/    /g' "${f}" > filename.notabs && mv filename.notabs "${f}"
    done
done
