t uri: http://us.archive.ubuntu.com/ubuntu
配置自动安装nginx服务
在自定义数据区域输入如下内容，以配置实例自动安装nginx服务。
#cloud-config packages: - nginx runcmd: - systemctl start nginx.service
配置自定义主机名
在自定义数据区域输入如下内容，以自定义设置主机名。
#cloud-config hostname: my-instance fqdn: my-instance.localdomain
配置自动运行自定义脚本
在自定义数据区域输入如下内容，以配置实例每次启动时自动运行Shell脚本。
#cloud-config bootcmd: - echo "Hello World. The time is now $(date -R)!" | tee /root/userdata_test.txt
