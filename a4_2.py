#!/usr/bin/env python3

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

IN = input('Enter device name: ')
print('Enter parameter name ', list(london_co[IN].keys()) ,':')
IN2 =input().lower()
print('\n' + '-' *30)

print(london_co[IN]['ios'])
ITEMS =(london_co[IN].items())

print(type(ITEMS))
print(ITEMS)

ITEMS = str(ITEMS)
print(type(ITEMS))
print(ITEMS)

KEYS =(london_co[IN].keys())
KEYS = list(KEYS)
K = len(KEYS)
print(KEYS)
VALUES =(london_co[IN].values())
VALUES = list(VALUES)
print(VALUES)

for i in range(K):
	print(KEYS[i],':',VALUES[i])

print(london_co[IN].get(IN2, "No such item"))
