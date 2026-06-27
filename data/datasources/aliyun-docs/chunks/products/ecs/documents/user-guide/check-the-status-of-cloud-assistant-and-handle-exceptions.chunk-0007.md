## Windows实例
远程连接Windows实例。
具体操作，请参见[使用](connect-to-a-windows-instance-through-workbench.md)[Workbench](connect-to-a-windows-instance-through-workbench.md)[登录](connect-to-a-windows-instance-through-workbench.md)[Windows](connect-to-a-windows-instance-through-workbench.md)[实例](connect-to-a-windows-instance-through-workbench.md)。
查看云助手安装目录C:\ProgramData\aliyun\assist是否存在。
如果assist文件夹存在，请继续执行[步骤](check-the-status-of-cloud-assistant-and-handle-exceptions.md)[3](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
如果assist文件夹不存在，说明云助手被卸载，需要重新安装云助手，具体操作，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
查看云助手服务状态。
单击开始菜单，选择Windows 管理工具>计算机管理。
选择计算机管理（本地）>服务和应用程序>服务。
找到Aliyun Assist Service，查看Aliyun Assist Service状态。
若状态列为正常运行，表示Aliyun Assist Service状态正常。
若状态列无显示，表示Aliyun Assist Service已停止，请单击启动，启动Aliyun Assist Service。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
在控制台查看云助手Agent状态。
如果云助手Agent状态为正常，说明异常已解决。
如果云助手Agent状态还是异常，需要查看云助手日志来具体分析。
云助手默
