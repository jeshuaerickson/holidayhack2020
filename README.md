# Holiday Hack Challenge 2020: Three French Hens


## Terminal Challenge: Kringle Kiosk

- Determined through errors that the application was "cowsay".
- Used command injection with "&&" to add another command to the end of the file which was "bin/bash"

## Terminal Challenge: Unescape Tmux

- Used "tmux a" to attach the available tmux session

## Terminal Challenge: Linux Primer (Sugarplum Mary)

- Entered "yes" to begin
- Step 1: "ls"
- Step 2: "cat munchkin*"
- Step 3: "rm mun*"
- Step 4: "pwd"
- Step 5: "ls -al"
- Step 6: "history | grep mun"
- Step 7: "env"
- Step 8: "cd workshop"
- Step 9: 
- Step 10: "chmod +x ./lollipop_engine"
- Step 11: "mv /home/elf/workshop/electrical/blown_fuse0 /home/elf/workshop/electrical/fuse0"
- Step 12: "ln -s fuse0 fuse1"
- Step 13: "cp fuse1 fuse2"
- Step 14: "echo "MUNCHKIN_REPELLENT" >> fuse2"
- Step 15: "git status"
- Step 16: "find /opt/munchkin_den -user munchkin"
- Step 17: "find /opt/munchkin_den -size +108k -size -110k"
- Step 18: "ps aux"
- Step 19: "netstat --listen"
- Step 20: "curl localhost:54321"
- Step 21: "pkill 14516_munchkin"



## Objective No. 1: Uncover Santa's Gift List

There is a photo of Santa's Desk on that billboard with his personal gift list. What gift is Santa planning on getting Josh Wright for the holidays? Talk to Jingle Ringford at the bottom of the mountain for advice.


[Objective #1](screenshots/objective-1-completed.jpg)

- First stop in the Holiday Hack challenge! I talked to Jingle Ringleford and downloaded the billboard image.
- I used the tool suggested in the hint. Took several attempts at twirling and untwirling before I could see what was on the list for him.
- Once I saw what was on the list, I read it as "poxmark", but had no idea if this was a thing, so I googled it. YUP! A very interesting thing at that. :)

## Objective No. 2: Investigate S3 Bucket

- Added wrapper3000 to the wordlist
- Found this bucket (wrapper3000) and the file "package"
- Now attempting to decompress the file
- <a href="http://s3.amazonaws.com/wrapper3000/package">http://s3.amazonaws.com/wrapper3000/package</a>
- Step 1: "cat package" (and see that it was base64 encoded)
- Step 2: "base64 -d package > package.zip"
- Step 3: "unzip package.zip"
- Step 4: "tar -xvf package.txt.Z.xz.xxd.tar.bz2"
- Step 5: "xxd -r *.xxd > package.txt.Z.xz"
- Step 6: "xz -d package.txt.Z.xz"
- Step 7: "uncompress package.txt.Z"
- Step 8: "cat package.txt"
- Step 9: Find the answer! ---> "North Pole: The Frostiest Place on Earth"

## Objective No. 3:




