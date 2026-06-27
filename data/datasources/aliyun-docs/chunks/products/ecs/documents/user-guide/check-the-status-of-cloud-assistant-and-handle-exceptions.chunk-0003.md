## systemd
执行如下命令，查看云助手状态。
systemctl status aliyun.service
当云助手状态为inactive (dead)，说明云助手服务已停止，需要执行systemctl start aliyun.service启动云助手服务。
如果启动时报错或无法启动，请卸载云助手后重新安装。具体操作，请参见[停止和卸载云助手](stop-and-uninstall-the-cloud-assistant-agent.md)[Agent](stop-and-uninstall-the-cloud-assistant-agent.md)和[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
[ @iZuf68j5ei93s share]# systemctl status aliyun.service ● aliyun.service - Aliyun Assist Loaded: loaded (/etc/systemd/system/aliyun.service; enabled; vendor preset: enabled) Active: inactive (dead) since Mon 2023-09-11 17:18:33 CST; 47s ago Process: 1951 ExecStart=/usr/local/share/aliyun-assist/2.2.3.515/aliyun-service (code=exited, status=0/SUCCESS) Main PID: 1951 (code=exited, status=0/SUCCESS) Tasks: 2 (limit: 22694) Memory: 1.3G CGroup: /system.slice/aliyun.service ├─5608 gpg-agent --homedir /var/cache/dnf/remi-modular-6408ecca79e22107/pubring --use-standard-socket --daemon └─5648 gpg-agent --homedir /var/cache/dnf/remi-safe-ff04689114f71b24/pubring --use-standard-socket --daemon
当云助手状态为active (running)，说明云助手服务正常运行中，请继续执行步骤[4](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
[root@iZuf68j5ei93
