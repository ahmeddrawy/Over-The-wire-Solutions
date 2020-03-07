#!/bin/bash

for i in * .*;
do 
if [ "$i" != "." -a "$i" != ".." ];
then
echo $i
fi
echo $i
done
