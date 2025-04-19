## Just Packets

Here pcap. Find flag.

## Solution

We were provided with a .pcap file containing 20 TCP packets, and the hint indicates that the flag is hidden in the URG pointer of these packets. 

Each TCP packet has a URG pointer field, which, when non-zero, indicates the presence of urgent data. We need to first identify which packets have a non-zero URG pointer.

![image](https://github.com/user-attachments/assets/c7e1af63-0aab-4886-91d8-66f4421b7a30)

By looking through Wireshark, we see that packets 6-18 have an URG pointer field that is non-zero.

By clicking on the `Urgent Pointer` field, and going through each packet, you will notice that some charecters in the ASCII translation are highlighted. 

By going through packets 6-18 and joining the highlighted text together, you get the flag.

FLAG: `dawgCTF{villagers_bonds}`


