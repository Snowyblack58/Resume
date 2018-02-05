#!/bin/bash
cat _core.html > index.html
core=`cat index.html`
echo "$core" | grep "<!--include" | while read -r line ; do
    file=$(echo $line | cut -d' ' -f 2 | cut -d'-' -f 1)
    contents=$(cat $file)
    awk -v contents="$contents" "/<!--include $file-->/ {print contents;}1" index.html > tmp.html
    cat tmp.html > index.html
done
rm tmp.html
