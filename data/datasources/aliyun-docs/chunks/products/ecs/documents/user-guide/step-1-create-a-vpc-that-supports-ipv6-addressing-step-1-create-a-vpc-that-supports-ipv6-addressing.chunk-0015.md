rface ipv6 add address "本地连接 2" <IPv6 地址 2>
执行以下命令，添加默认路由。
netsh interface ipv6 add route ::/0 "本地连接 2" <IPv6 网关>
（条件必选）如果您的ECS实例运行的是Linux系统，请执行此步骤；否则，可跳过此操作。
执行以下命令，查看实例是否安装了多网卡配置工具。
ls /sbin/eni-ifscan
若返回信息如下图，则表示实例预装了多网卡配置工具，您需要修改多网卡配置工具的eni-function文件。
说明
如果Linux实例预装了多网卡配置工具，由于该工具默认不支持IPv6，将导致Linux系统内的IPv6网卡无法自动识别，实例重启后系统无法获取IPv6地址。
如何修改eni-function文件
执行以下命令，修改eni-function文件。
vim /etc/eni_utils/eni-function
按i键进入编辑模式，将IPV6INIT=no修改为IPV6INIT=yes，并添加DHCPV6C=yes行，修改后保存并退出。
验证，当输入ifconfig或ipconfig命令返回[第一步](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)的结果时即表示配置成功。
此时ECS实例已具备IPv6私网通信的能力，可以按如下步骤测试私网连通性。
测试私网连通性
说明
测试IPv6的网络连通性时，您需要确保服务端与客户端都支持并配置了IPv6。在此示例中，两台ECS实例互相访问的前提是您的ECS01实例与ECS02实例均已配置了IPv6。
在ECS01实例中执行ping6 <ECS02 IPv6私网地址>命令，ping6ECS02实例的IPv6地址，测试私网通信是否正常。
如果能接收到回复报文，表示通信正常。经测试，ECS01实例到ECS02实例的IPv6私网通信正常。
在ECS02实例中执行ping6命令，pingECS01实例的IPv6地址，测试私网通信是否正常。
如果能接收到回复报文，表示通信正常。经测试，ECS02实例到ECS01实例的IPv6私网通信正常。
