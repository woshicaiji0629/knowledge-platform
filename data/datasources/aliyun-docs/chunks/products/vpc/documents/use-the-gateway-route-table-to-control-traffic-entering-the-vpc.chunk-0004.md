### 步骤二：配置安全设备
重要
本方案将ECS-A模拟为安全设备，需要配置IP流量转发。如果您使用第三方安全设备，您需要按照自身业务实际情况联系第三方安全设备提供商协助部署。
本方案配置以Alibaba Cloud Linux 3.2104 64位操作系统为例。
登录ECS-A，执行以下命令配置IP流量转发。
永久启用# 永久启用IP转发（写入配置文件） echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf # 立即生效 sysctl -p
实例重启后失效# 临时启用IP转发（重启后失效） sysctl -w net.ipv4.ip_forward=1
