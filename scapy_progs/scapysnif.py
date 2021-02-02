from scapy.all import *
a = sniff(count=10)
a.nsummary()


# 0000 Ether / IP / UDP 10.10.10.2:60587 > 45.10.234.49:15502 / Raw
# 0001 Ether / IP / UDP 10.10.10.2:60587 > 45.10.234.49:15502 / Raw
# 0002 Ether / IP / UDP 45.10.234.49:15502 > 10.10.10.2:60587 / Raw
# 0003 Ether / IP / UDP 45.10.234.49:15502 > 10.10.10.2:60587 / Raw
# 0004 Ether / IP / TCP 34.245.28.34:https > 10.10.6.14:35854 PA / Raw
# 0005 Ether / IP / TCP 34.245.28.34:https > 10.10.6.14:35854 PA / Raw
# 0006 Ether / IP / TCP 34.245.28.34:https > 10.10.6.14:35854 PA / Raw
# 0007 Ether / IP / TCP 34.245.28.34:https > 10.10.6.14:35854 PA / Raw
# 0008 Ether / IP / TCP 34.245.28.34:https > 10.10.6.14:35854 PA / Raw
# 0009 Ether / IP / TCP 34.245.28.34:https > 10.10.6.14:35854 PA / Raw
