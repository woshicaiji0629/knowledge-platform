### Linux实例
步骤一：检查是否已安装云助手Agent
[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)。
判断初始化系统类型。
初始化系统（init system）负责在系统启动时加载和管理服务进程，不同初始化系统对应的云助手Agent的命令不同。
systemd：Alibaba Cloud Linux、CentOS 7+、RHEL 7+、Fedora 15+、Ubuntu 15.04+、Debian 8+等。
Upstart：Ubuntu 6.10-14.10、RHEL 6、CentOS 6等。
SysVinit：RHEL 5、CentOS 5、Debian 6等。
验证是否安装云助手Agent。
systemdsystemctl status aliyun.service
若回执信息包含Unit aliyun.service could not be found提示，表示未安装。
upstart/sbin/initctl status aliyun-service
若回执信息包含initctl: Unknown job: aliyun-service提示，表示未安装。
sysvinit/etc/init.d/aliyun-service status
若回执信息为空，表示未安装。
步骤二：下载并安装云助手Agent
脚本适用于阿里云ECS实例，默认安装最新版本的Agent，安装指定版本请修改VERSION=latest。
#!/bin/bash VERSION=latest PACKAGE= PKG_URI= REGION=$(curl -s http://100.100.100.200/latest/meta-data/region-id) DOMAIN=aliyun-client-assist-${REGION}.oss-${REGION}-internal.aliyuncs.com arch=$(uname -m) echo "[main] arch = ${arch}" # 检测是否为 openSUSE 或 SLES 系统 is_suse_lik
