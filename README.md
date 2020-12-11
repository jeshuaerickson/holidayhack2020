# Holiday Hack Challenge 2020: Three French Hens

## Challenges

### Kringle Kiosk (Shinny Upatree)
~~~
Welcome to our castle, we're so glad to have you with us!
Come and browse the kiosk; though our app's a bit suspicious.
Poke around, try running bash, please try to come discover,
Need our devs who made our app pull/patch to help recover?

Escape the menu by launching /bin/bash
~~~

- Determined through errors that the application was "cowsay".
- Used command injection with "&&" to add another command to the end of the file which was "bin/bash"

### Unescape Tmux (Pepper Minstix)
~~~
Can you help me?

I was playing with my birdie (she's a Green Cheek!) in something called tmux,
then I did something and it disappeared!

Can you help me find her? We were so attached!!
~~~

- Used "tmux a" to attach the available tmux session

### Linux Primer (Sugarplum Mary)

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

### The Elf C0de (Ribb Bonbowford)

Mischevious munchkins have nabbed all the North Pole's lollipops intended for good children all over the world. Use your JavaScript skills to retrieve the nabbed lollipops from all the entrances of KringleCon.

### Redis Bug Hunt (Holly Evergreen)
~~~
We need your help!!

The server stopped working, all that's left is the maintenance port.

To access it, run:

curl http://localhost/maintenance.php

We're pretty sure the bug is in the index page. Can you somehow use the
maintenance page to view the source code for the index page?
~~~

### Speaker UNPrep (Bushy Evergreen)
~~~
Help us get into the Speaker Unpreparedness Room!

The door is controlled by ./door, but it needs a password! If you can figure
out the password, it'll open the door right up!

Oh, and if you have extra time, maybe you can turn on the lights with ./lights
activate the vending machines with ./vending-machines? Those are a little
trickier, they have configuration files, but it'd help us a lot!

(You can do one now and come back to do the others later if you want)

We copied edit-able versions of everything into the ./lab/ folder, in case you
want to try EDITING or REMOVING the configuration files to see how the binaries
react.

Note: These don't require low-level reverse engineering, so you can put away IDA
and Ghidra (unless you WANT to use them!)
~~~

### Scapy Prepper (Alabaster Snowball)
~~~
╔════════════════════════════════════════════════════════════════╗
║  ___ ___ ___ ___ ___ _  _ _____   ___  _   ___ _  _____ _____  ║
║ | _ \ _ \ __/ __| __| \| |_   _| | _ \/_\ / __| |/ / __|_   _| ║
║ |  _/   / _|\__ \ _|| .` | | |   |  _/ _ \ (__| ' <| _|  | |   ║
║ |_| |_|_\___|___/___|_|\_| |_|   |_|/_/ \_\___|_|\_\___| |_|   ║
║                ___                                             ║
║               | _ \_ _ ___ _ __ _ __  ___ _ _                  ║
║               |  _/ '_/ -_) '_ \ '_ \/ -_) '_|                 ║
║               |_| |_| \___| .__/ .__/\___|_|                   ║
║                           |_|  |_|                             ║
║                (Packets prepared with scapy)                   ║
╚════════════════════════════════════════════════════════════════╝
Type "yes" to begin. 
~~~

### CAN-Bus Investigation (Wunorse Openslae)
~~~
Welcome to the CAN bus terminal challenge!

In your home folder, there's a CAN bus capture from Santa's sleigh. Some of
the data has been cleaned up, so don't worry - it isn't too noisy. What you
will see is a record of the engine idling up and down. Also in the data are
a LOCK signal, an UNLOCK signal, and one more LOCK. Can you find the UNLOCK?
We'd like to encode another key mechanism.

Find the timestamp of the UNLOCK code in candump.log and submit it to
./runtoanswer!
~~~

## Objective No. 1: Uncover Santa's Gift List

There is a photo of Santa's Desk on that billboard with his personal gift list. What gift is Santa planning on getting Josh Wright for the holidays? Talk to Jingle Ringford at the bottom of the mountain for advice.


![](screenshots/objective-1-completed.jpg)

There is a photo of Santa's Desk on that billboard with his personal gift list. What gift is Santa planning on getting Josh Wright for the holidays? Talk to Jingle Ringford at the bottom of the mountain for advice.

- First stop in the Holiday Hack challenge! I talked to Jingle Ringleford and downloaded the billboard image.
- I used the tool suggested in the hint. Took several attempts at twirling and untwirling before I could see what was on the list for him.
- Once I saw what was on the list, I read it as "poxmark", but had no idea if this was a thing, so I googled it. YUP! A very interesting thing at that. :)

## Objective No. 2: Investigate S3 Bucket

When you unwrap the over-wrapped file, what text string is inside the package? Talk to Shinny Upatree in front of the castle for hints on this challenge.

![](screenshots/objective-2-completed.jpg)

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

## Objective No. 3: Point-of-Sale Password Recovery

Help Sugarplum Mary in the Courtyard find the supervisor password for the point-of-sale terminal. What's the password?

- Step 1: Click on the Point-of-Sale terminal
- Step 2: Foo

## Objective No. 4: Operate the Santavator

Talk to Pepper Minstix in the entryway to get some hints about the Santavator.

![](screenshots/objective-4-completed.jpg)

- foo

## Objective No. 5: Open HID Lock

![](screenshots/objective-5-completed.jpg)





