#!/bin/bash



# blockchain.py is the script shown above
./blockchain.py | tail -n 624 > blockchain32.out

wc blockchain32.out

cat blockchain32.out | mt19937predict | head -8 | tail -n 2

echo "All Done!"
