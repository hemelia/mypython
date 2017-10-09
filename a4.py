#!/usr/bin/env python3

IN = input('Enter IP address and mask in follow format 10.10.10.0/24: ')

#from sys import argv
#IN = argv[1:]
#IN = str(IN)
#IN = (IN[2:-2])
#print(type(IN))

print('\n' + '-' * 30)
IN = IN.split('/')
IP = IN[0]
MASK = int(IN[1])
IP = IP.split('.');
IPA = (int(IP[0]));
IPB = (int(IP[1]));
IPC = (int(IP[2]));
IPD = (int(IP[3]));
print('IP: ')
print("{:8}  {:8}  {:8}  {:8}".format(IP[0], IP[1], IP[2], IP[3]));
#print("{:08b}  {:08b}  {:08b}  {:08b}".format(IPA, IPB, IPC, IPD));
A = ("{:08b}".format(IPA));
B = ("{:08b}".format(IPB));
C = ("{:08b}".format(IPC));
D = ("{:08b}".format(IPD));
print(A,'', B,'', C,'', D,'')
E = (A+B+C+D)		# show as one string
E = E[:MASK] 		# show only left part minus  chnaged bits
E = E + '0'*(32-MASK)	# add zeros to right part
print('Network: ')
print("{:<8}  {:<8}  {:<8}  {:<8}".format(int(E[0:8], 2),  int(E[8:16], 2), int(E[16:24], 2), int(E[24:32], 2) ));
print("{:<8}  {:<8}  {:<8}  {:<8}".format(E[0:8], E[8:16], E[16:24], E[24:32] ));

print('Mask: ')
print('/',MASK, sep='');
MASKB = []
for i in range(int(MASK)):
        MASKB.append('1')
for i in range(32-int(MASK)):
	MASKB.append('0')
MASKC = ''.join(MASKB)
print("{:<8}  {:<8}  {:<8}  {:<8}".format(int(MASKC[0:8], 2),  int(MASKC[8:16], 2), int(MASKC[16:24], 2), int(MASKC[24:32], 2) ));
print(MASKC[0:8],'',MASKC[8:16],'',MASKC[16:24],'',MASKC[24:32])

