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



#var = 1236

# we only need 312 nonces

for var in list(range(1548)):
    # start on block 1236
#    var = var + 1236
    print(c2.blocks[var].block_data)
    print(c2.blocks[var].hash)
    #print(c2.blocks[var].nonce)
#    currentNonce = c2.blocks[var].nonce
#    hexNonce = (str('%016.016x' % (currentNonce)).encode('utf-8'))
   

    # this is actually first (though it is the second half of the nonce)
#    hexNonce_32a = (currentNonce  >> 32 ) & 0xffffffff

    # this is second (though it is the first half of the nonce)
#    hexNonce_32b = currentNonce & 0xffffffff

#    print(hexNonce_32b)
#    print(hexNonce_32a)

    #print(hexNonce)
    #print(hex(hexNonce_32a))
    
    #print(hex(hexNonce_32b))
    #print(c2.blocks[var].index)
    #c2.blocks[var].dump_doc(1)




