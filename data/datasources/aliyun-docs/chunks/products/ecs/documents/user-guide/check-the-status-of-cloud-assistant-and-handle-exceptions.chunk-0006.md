## sysvinit
执行如下命令，查看云助手状态。
/etc/init.d/aliyun-service status
当云助手状态为Stopped，说明云助手服务已停止，需要执行/etc/init.d/aliyun-service start启动云助手服务。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
[root@i7bp1hfzscxxx ~]# /etc/init.d/aliyun-service status Stopped
当云助手状态为Running，说明云助手服务正常运行中，请继续执行步骤[4](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
[root@i7bplhtzscxxxxxx ~]# /etc/init.d/aliyun-service status Running
在控制台查看云助手Agent状态。
如果云助手Agent状态为正常，说明异常已解决。
如果云助手Agent状态依旧异常，需要查看云助手日志来具体分析。
CoreOS操作系统：
cd /opt/local/share/aliyun-assist/<version>/log tail -100f aliyun_assist_main.log
其他操作系统（Alibaba Cloud Linux、Ubuntu、Debian、RedHat、SUSE Linux Enterprise Server和OpenSUSE等）：
cd /usr/local/share/aliyun-assist/<version>/log tail -100f aliyun_assist_main.log
