#!/usr/bin/python

NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload';
NAT1 = NAT.replace('Fast' , 'Gigabit');
print(NAT1);

MAC = 'AAAA:BBBB:CCCC';
MAC = MAC.replace(':' , '.');
print(MAC);

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100';
CONFIG = CONFIG.split();
print(CONFIG[-1].split(','));

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100';
command2 = 'switchport trunk allowed vlan 1,3,100,200,300';
command1 = command1.split();
command1 = command1[-1].split(',');
command2 = command2.split();
command2 = command2[-1].split(',');
print(set(command1) & set(command2));

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10];
VLANS = set(VLANS);
VLANS = sorted(VLANS);
print(VLANS);


ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0';
a = ospf_route.split();
a[0] = 'OSPF';
print("{:20} {:20}".format("Protocol:" , a[0]));
print("{:20} {:20}".format("Prefix:" , a[1]));
print("{:20} {:20}".format("AD/Metric:" , a[2]));
print("{:20} {:20}".format("Next-Hop:" , a[4]));
print("{:20} {:20}".format("Last update:" , a[5]));
print("{:20} {:20}".format("Outbound Interface:" , a[6]));

MAC1 = 'AAAA:BBBB:CCCC';
MAC1 = MAC1.split(':');
MACA = bin(int(MAC1[0],16)) [2:];
MACB = bin(int(MAC1[1],16)) [2:];
MACC = bin(int(MAC1[2],16)) [2:];
print(MACA+MACB+MACC);

IP = '192.168.3.1';
IP = IP.split('.');
print(IP);
IPA = (int(IP[0]));
IPB = (int(IP[1]));
IPC = (int(IP[2]));
IPD = (int(IP[3]));
print("{:8}  {:8}  {:8}  {:8}".format(IP[0], IP[1], IP[2], IP[3]));
print("{:08b}  {:08b}  {:08b}  {:08b}".format(int(IP[0]), IPB, IPC, IPD));

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']


#d_keys = ['Protocol:', 'Prefix:', 'AD/Metric:','Next-Hop:','Last update:','Outbound Interface:'];
#print(d_keys);
#r1 = dict.fromkeys(d_keys);
#print(r1);

