### 配置流量镜像后，如何验证流量已被正确转发至镜像目的？
登录镜像目的ECS2，执行如下命令，查看是否可以获取到报文的数据包。
tcpdump -i eth0 udp port 4789 -nne
vni 1为镜像会话的标识，表示镜像目的通过镜像会话，成功获取到数据包。
[root@ixxxZ ~]# tcpdump -i eth0 udp port 4789 -nne dropped privs to tcpdump tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes 16:21:48.673510 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 110: 192.168.0.201.27551 > 172.16.0.105.4789: VXLAN, flags [I] (0x08), vni 1 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 60: 45.200.149.95.57388 > 192.168.0.201.7432: Flags [R], seq 950507569, win 1200, options [mss 1460], length 0 16:21:48.673706 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 188: 192.168.0.201.41566 > 172.16.0.105.4789: VXLAN, flags [I] (0x08), vni 1 ee:ff:ff:ff:ff:ff > 00:16:3e:13:51:9b, ethertype IPv4 (0x0800), length 138: 172.16.0.105 > 192.168.0.201: ICMP 172.16.0.105 udp port 4789 unreachable, length 104
该文章对您有帮助吗？
反馈
