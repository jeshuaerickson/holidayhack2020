#!/usr/bin/env python3


import naughty_nice as nn
from Crypto.PublicKey import RSA
from naughty_nice import Chain


with open('official_public.pem','rb') as fh:
    official_public_key = RSA.importKey(fh.read())
c2 = Chain(load=True, filename='blockchain.dat')
#print('C2: Block chain verify: %s' % (c2.verify_chain(official_public_key)))
#print(c2.blocks[0])
#c2.blocks[0].dump_doc(1)

#iterate through blocks

for var in list(range(1548)):
    #print(c2.blocks[var].block_data)
    #print(c2.blocks[var].hash)
    
    #this is the block that has apparently been tampered with.
    if c2.blocks[var].index == 129459:
        print(c2.blocks[var].block_data)
    
    #print(c2.blocks[var].nonce)
        
        #suspicious binary file
        c2.blocks[var].dump_doc(1)
        
        #associated pdf
        c2.blocks[var].dump_doc(2)

        #checking to see if there are any more docs
        #c2.blocks[var].dump_doc(3)
        #This was out of index so no further documents.




