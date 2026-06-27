### 系统保留地址
交换机网段的地址空间中存在系统保留地址，无法将系统保留地址分配给ECS等云资源。
针对IPv4，每个交换机的第1个和最后3个IP地址为系统保留地址。
例如，交换机的网段为192.168.1.0/24，则192.168.1.0、192.168.1.253、192.168.1.254和192.168.1.255这4个地址是系统保留地址。
针对IPv6，每个交换机的第1个和最后9个IP地址为系统保留地址。
例如，交换机的IPv6网段为2408:xxxx:xxxx:6eff::/64，则第1个2408:xxxx:xxxx:6eff::和最后9个2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fff7、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fff8、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fff9、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffa、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffb、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffc、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffd、2408:xxxx:xxxx:6eff:ffff:ffff:ffff:fffe和2408:xxxx:xxxx:6eff:ffff:ffff:ffff:ffff为系统保留IP。
