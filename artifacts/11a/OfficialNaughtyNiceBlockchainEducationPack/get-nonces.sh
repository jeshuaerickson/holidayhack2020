#!/bin/bash


echo "" > data.out


for i in {1..5}

do
 python3 ./naughty_nice.py | grep Nonce: >> data.out
done

echo "All Done!"
