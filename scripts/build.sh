#!/bin/sh

usage(){
    echo
    echo  " Usage:  #./build.sh  [pdf/man/html] "
    echo
}


# 
# Command Options 
#
if [ $# -eq 0 ]; then
    out="all"
else
    if [ $1 != "pdf" -a $1 != "man" -a $1 != "html" ]; then
        usage;
    else
        out=$1
    fi
fi

#
# Main program
#
for f in *.pod
do
	name=$(echo $f | awk -F'.' '{print $1}')
	echo $name

	if [ ! -e output ]
	then
		mkdir output
	fi

	if [ "$out" = "all" -o "$out" = "man" ]
	then
		pod2man $name.pod > output/$name.1m --center '' -s '1M' -r '' -d ' '
	fi

	if [ "$out" = "all" -o "$out" = "pdf" ]
	then
		if [ ! -e output/$name.1m ]
		then
			pod2man $name.pod > output/$name.1m --center '' -s '1M' -r '' -d ' '
		fi
		man -t output/$name.1m | ps2pdf - > output/$name.pdf
	fi

	if [ "$out" = "all" -o "$out" = "html" ]
	then
		if [ ! -e output/$name.1m ]
		then
			pod2man $name.pod > output/$name.1m --center '' -s '1M' -r '' -d ' '
		fi
		man2html output/$name.1m > output/$name.html
		# man -Thtml output/$name.1m > output/$name.html
	fi

done
