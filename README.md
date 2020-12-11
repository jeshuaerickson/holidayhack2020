# Holiday Hack Challenge 2020: Three French Hens


## Terminal Challenge: Kringle Kiosk

- Determined through errors that the application was "cowsay".
- Used command injection with "&&" to add another command to the end of the file which was "bin/bash"

## Terminal Challenge: Unescape Tmux

- Used "tmux a" to attach the available tmux session


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




