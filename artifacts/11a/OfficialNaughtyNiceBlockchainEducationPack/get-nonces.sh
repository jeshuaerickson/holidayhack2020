#!/bin/bash


echo "" > data.out


for i in {1..624}

#generate nonces	
do
 python3 ./naughty_nice.py | grep Nonce: >> data.out
 tail -n 1 data.out
done

# get rid of nonce text
sed -i -e 's/              Nonce: //g' data.out

# get all but the first line
tail -624 data.out > nonces.txt

wc data.out

echo "All Done!"
