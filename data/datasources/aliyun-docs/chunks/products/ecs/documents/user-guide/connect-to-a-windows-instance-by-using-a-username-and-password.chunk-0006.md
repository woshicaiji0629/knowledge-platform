## 应用于生产环境
- 修改默认RDP远程连接端口
建议将默认的3389端口改为其他数值较大的非标准端口（如33890），以降低遭受自动化扫描和暴力破解的风险。
放行新端口：在实例所属的安全组中[添加入方向规则](start-using-security-groups.md)，放行新的端口（如33890）。
修改服务端口：登录实例，通过修改注册表来更改端口。
按Win+R输入regedit并按Enter键，打开注册表编辑器。
导航到路径HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp。
找到名为PortNumber的值，右键并单击修改，将其基数修改为十进制，然后输入新端口号（如33890）。
按Win+R输入services.msc并按Enter键打开服务窗口，找到Remote Desktop Services，右键单击并选择重新启动，使配置生效。
使用新端口连接：修改远程桌面端口后，在使用客户端连接实例时，应在实例公网 IP 地址后指定新端口，格式如下：<公网IP>:<端口号>。
- 仅授权可信的IP访问实例
[修改安全组规则](start-using-security-groups.md)，仅允许本机IP或其他受信任的IP访问实例RDP服务端口（默认为3389），拦截未知主机访问实例。
