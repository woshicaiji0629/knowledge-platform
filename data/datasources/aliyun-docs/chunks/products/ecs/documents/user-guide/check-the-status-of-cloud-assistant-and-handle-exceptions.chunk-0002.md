## Linux实例
远程连接Linux实例。
具体操作，请参见[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行如下命令，查看云助手安装目录是否存在。
CoreOS操作系统
cd /opt/local/share/ ls
其他操作系统（Alibaba Cloud Linux、Ubuntu、Debian、RedHat、SUSE Linux Enterprise Server和OpenSUSE等）
cd /usr/local/share/ ls
如果aliyun-assist文件夹存在，请继续执行步骤[3](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
如果aliyun-assist文件夹不存在，说明云助手被卸载，需要重新[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
查看云助手服务状态。
先确定ECS实例的初始化系统，不同内核版本的Linux系统，查看云助手服务状态命令不同。
ls -l /sbin/init
如果输出指向systemd例如/lib/systemd/systemd，说明系统使用systemd。
如果输出指向upstart例如/sbin/upstart，说明系统使用Upstart。
如果输出指向init例如/sbin/init，说明系统使用sysvinit。
