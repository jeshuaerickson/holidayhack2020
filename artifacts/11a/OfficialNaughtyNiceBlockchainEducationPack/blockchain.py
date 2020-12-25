#!/usr/bin/env python3


import naughty_nice as nn
from Crypto.PublicKey import RSA
from naughty_nice import Chain


with open('official_public.pem','rb') as fh:
    official_public_key = RSA.importKey(fh.read())
c2 = Chain(load=True, filename='blockchain.dat')
print('C2: Block chain verify: %s' % (c2.verify_chain(official_public_key)))

for var in list(range(1548)):
    print(c2.blocks[var].block_data)
    #c2.blocks[var].dump_doc(1)
    me = var

print(me)




