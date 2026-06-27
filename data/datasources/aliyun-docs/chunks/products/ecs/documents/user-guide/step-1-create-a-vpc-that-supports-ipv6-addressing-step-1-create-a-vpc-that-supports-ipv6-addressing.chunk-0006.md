## Windows实例
远程连接Windows实例。
具体操作，请参见[使用](connect-to-a-windows-instance-through-workbench.md)[Workbench](connect-to-a-windows-instance-through-workbench.md)[登录](connect-to-a-windows-instance-through-workbench.md)[Windows](connect-to-a-windows-instance-through-workbench.md)[实例](connect-to-a-windows-instance-through-workbench.md)。
打开命令行工具，执行ipconfig命令
如果返回信息如下图所示（一个全局单播地址和一个链路本地地址），则表示已成功识别IPv6地址，可以跳过此配置IPv6的步骤，如果没有，请继续执行以下操作。
配置IPv6地址。
重要
自动配置IPv6地址方式需安装云助手；若您的实例不支持或不方便安装云助手，请通过手动方式配置IPv6地址。
（推荐）自动配置IPv6地址前提条件
实例已安装云助手。若未安装，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
仅适用于以下操作系统：Alibaba Cloud Linux 2/3、CentOS 6/7/8、Red Hat 6/7、Anolis OS、Fedora、Ubuntu 14/16/18/20、Debian 8/9/10/11、SUSE 11/12/15、OpenSUSE 15/42、FreeBSD 11。
重要
配置过程需使用到云助手，可能会自动重启网卡、网络服务，短时间内网络可能会不可用，请慎重执行。
操作步骤
远程连接Linux实例。
具体操作，请参见[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行以下命令配置IPv6地址。
说明
在
