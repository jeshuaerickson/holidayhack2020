#!/usr/bin/env python3


import naughty_nice as nn
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5, SHA256
from naughty_nice import Chain


with open('official_public.pem','rb') as fh:
    official_public_key = RSA.importKey(fh.read())

files = ['blockchain.dat','bc1.dat']
for file in files:

    print(file + " ##################################################")

    c2 = Chain(load=True, filename=file)
    #c2 = Chain(load=True, filename='blockchain.dat')
    #print('C2: Block chain verify: %s' % (c2.verify_chain(official_public_key)))

    #iterate through blocks

    #jack's block sequence is 1010
    blocksequence = 1010
    c2.blocks[blocksequence].dump_doc(2)

    block_data = c2.blocks[blocksequence].block_data

    index = c2.blocks[blocksequence].index
    nonce = c2.blocks[blocksequence].nonce
    sign = c2.blocks[blocksequence].sign
    score = c2.blocks[blocksequence].score
    previous_hash =  c2.blocks[blocksequence].previous_hash
    current_hash  = c2.blocks[blocksequence].hash
    second = c2.blocks[blocksequence].second
    sig = c2.blocks[blocksequence].sig


    print(" ")
    print(" ")

    #print("block data:      " + str(block_data))
    print("index:           " + str(index))
    print("nonce:           " + str(nonce))
    print("sign:            " + str(sign))
    print("score:           " + str(score))
    print("previous hash:   " + str(previous_hash))
    print("hash:            " + str(current_hash))
    print("second:          " + str(second))
    print("sig:             " + str(sig))


    # Trying to get SHA256 hash of Jack's block.
    hash_obj_sha256 = SHA256.new()
    hash_obj_md5 = MD5.new()

    hash_obj_sha256.update(c2.blocks[blocksequence].block_data_signed())
    hash_obj_md5.update(c2.blocks[blocksequence].block_data())

    #print(c2.blocks[1010].block_data())

    print(" ")
    print("-------------------------------SHA256---------")
    print(hash_obj_sha256.hexdigest())
    print(" ")
    print("-------------------------------MD5------------")
    print(hash_obj_md5.hexdigest())
    print(" ")
    print(" ")


#print(c2.blocks[blocksequence].block_data())


#print(c2.blocks[1010])






    #print(c2.blocks[var].block_data)
    #print(c2.blocks[var].hash)
    
    #this is the block that has apparently been tampered with.
    #if c2.blocks[var].index == 129459:
        #print(c2.blocks[var].block_data)
         
    #print(c2.blocks[var].nonce)
        
        #suspicious binary file
        #c2.blocks[var].dump_doc(1)
        
        #associated pdf
        #c2.blocks[var].dump_doc(2)

        #checking to see if there are any more docs
        #c2.blocks[var].dump_doc(3)
        #This was out of index so no further documents.

        #this is so we get the array index of the block
        #print(var)


