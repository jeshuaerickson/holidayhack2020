#!/usr/bin/env python3


import naughty_nice as nn
from Crypto.PublicKey import RSA
from naughty_nice import Chain


with open('official_public.pem','rb') as fh:
    official_public_key = RSA.importKey(fh.read())
c2 = Chain(load=True, filename='blockchain.dat')
print('C2: Block chain verify: %s' % (c2.verify_chain(official_public_key)))
print(c2.blocks[0])
c2.blocks[0].dump_doc(1)





