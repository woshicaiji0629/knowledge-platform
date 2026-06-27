rkbench.md)。
打开命令行工具，执行ipconfig命令，检查实例是否已开启IPv6服务。
如果未返回inet6相关内容：表示实例未开启IPv6服务，请开启IPv6服务。
如何开启IPv6服务？
选择控制面板>网络和共享中心>网络连接。
单击当前网络连接名，打开状态界面，再单击属性。
选中Internet 协议版本 6 （TCP/IPv6）。
Windows Server 2008/2012/2016/2019/2022的操作步骤如下：
检查IPv6协议这一行是否被选中。如果没有选中则需要先选中，然后单击确定。
Windows Server 2003的操作步骤如下：
根据IPv6协议是否存在，执行不同操作。
存在IPv6协议：
选中Internet 协议版本 6 （TCP/IPv6），再单击确定。
不存在IPv6协议：
在本地连接属性页面，单击安装，在网络组件类型页面单击协议>添加。
在选择网络协议页面，选择Microsoft TCP/IP 版本 6>确定完成安装。
选中Internet 协议版本 6 （TCP/IPv6），再单击确定。
如果返回inet6相关内容：表示实例已开启IPv6服务，请配置IPv6地址。
配置IPv6地址。
在实例详情页，获取已生成的IPv6地址。
配置IPv6地址。
Windows Server 2008/2012/2016的操作步骤如下：
选择控制面板>网络。
单击当前网络连接名，打开状态界面，再单击属性。
选择IPv6协议>属性。
选中使用以下IPv6地址，并填入IPv6地址、子网前缀长度和IPv6网关，单击确定。
（可选）绑定多个IPv6地址：在Internet 协议版本 6（TCP/IP）属性界面，单击高级打开高级设置界面，单击添加做批量处理。完成后单击确定。
Windows Server 2003的操作步骤如下：
选择控制面板>网络连接，查看当前网络连接名，假设为本地连接 2。
在Windows系统桌面使用Win+R组合键打开运行对话框，并输入cmd命令，然后单击确定，打开命令行工具。
添加IPv6地址。
单个IPv6地址执行以下命令：
netsh interface ipv6 add address "本地连接 2" <IPv6 地址>
多个IPv6地址执行以下命令：
netsh interface ipv6 add address "本地连接 2" <IPv6 地址 1> netsh interface ipv6 add address "本地连接 2" <IPv6 地址 2>
执行以下命令，添加默认路由。
netsh interface ipv6 add route ::/0 "本地连接 2" <IPv6 网关>
（条件必选）如果您的ECS实例运行的是Linux系统，请执行此步骤；否则，可跳过此操作。
执
