s.org/@g" /etc/yum.repos.d/centos.repo sed -i "s@http://mirrors.cloud.aliyuncs.com/centos-stream/@https://mirror.stream.centos.org/@g" /etc/yum.repos.d/centos-addons.repo yum update -y # Modify NTP Server echo "server ntp1.aliyun.com" | tee /etc/ntp.conf systemctl restart ntpd.service
说明
其中114.114.114.114为DNS服务器地址、https://mirror.stream.centos.org为CentOS Stream的yum仓库地址、server ntp1.aliyun.com为阿里云的NTP服务器地址，请您根据实际环境替换。
您也可以使用Cloud Config数据更改yum源，但是不够灵活，不能适配阿里云已对部分yum源进行预配置的情况，建议使用User-Data脚本。
自定义管理员账号
Linux实例默认使用root用户作为管理员，您可以使用实例自定义数据使用其他用户作为管理员。
#!/bin/sh useradd test-user echo "test-user ALL=(ALL) NOPASSWD:ALL" | tee -a /etc/sudoers mkdir /home/test-user/.ssh touch /home/test-user/.ssh/authorized_keys echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCRnnUveAis****" | tee -a /home/test-user/.ssh/authorized_keys
说明
请使用您的公钥替换示例中的公钥ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCRnnUveAis****。
说明
当User-Data执行遇到问题时，可以通过云助手公共命令ACS-ECS-UserData-Check-for-linux.sh来获取失败相关的错误日志。如果返回有错误信息表示脚本执行有问题，如果没有返回错误信息表示执行没有报错，需要排查其他方面。关于云助手公共命令的更多信息，请参见[查看和执行公共命令](view-and-run-common-cloud-assistant-commands.md)。
