## Upstart
执行如下命令，查看云助手状态。
/sbin/initctl status aliyun-service
当云助手状态为stop/waiting，说明云助手服务已停止，需要执行/sbin/initctl start aliyun-service启动云助手服务。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
/sbin/initctl status aliyun-service aliyun-service stop/waiting
当云助手状态为start/running，说明云助手服务正常运行中，请继续执行步骤[4](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
/sbin/initctl status aliyun-service aliyun-service start/running, process 1129
