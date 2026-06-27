## 已知问题
Alibaba Cloud Linux 2在内核版本4.19.91-23.al7.x86_64中所包含的SGX驱动在特定情况下存在内存泄漏问题，该问题已在最新版本中修复，建议您更新到最新内核版本解决该问题。如果您需要继续使用该内核版本，建议安装补丁规避此问题，安装命令如下。
sudo yum install -y alinux-release-experimentals && \ sudo yum install -y kernel-hotfix-5577959-23.al7.x86_64
该文章对您有帮助吗？
反馈
