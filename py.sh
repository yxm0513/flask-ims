find . -name "*.pyc" -exec rm -rf {} \;
types=(.py .html)
for t in ${types[@]}
do
    echo TYPE: ${t}
    files=(`find ./ -name "*${t}"`)

    for f in ${files[@]}
    do
        echo ${f}
        sed 's/	/    /g' "${f}" > filename.notabs && mv filename.notabs "${f}"
    done
done
