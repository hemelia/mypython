#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk),
  * пример текста запроса: 'Enter interface mode (access/trunk): '
* номере интерфейса (тип и номер, вида Gi0/3)
  * пример текста запроса: 'Enter interface type and number: '
* номер VLANа (для режима trunk будет вводиться список VLANов)
  * пример текста запроса: 'Enter vlan(s): '
'''

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']


