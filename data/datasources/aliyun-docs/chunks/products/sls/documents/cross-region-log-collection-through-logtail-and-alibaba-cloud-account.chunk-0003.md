### 网络传输说明

| 传输方式 | 适用场景 |
| --- | --- |
| 公网 | 阿里云云服务器实例和日志服务 Project 属于不同地域。 服务器为其他云厂商服务器或自建 IDC。 |
| 传输加速 | 服务器分布在海外各地的自建机房或者来自海外云厂商，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，推荐选择 传输加速 。更多信息，参见 [管理传输加速](transmission-acceleration.md) 。 |

登录地域A的ECS实例，请参考[网络传输说明](cross-region-log-collection-through-logtail-and-alibaba-cloud-account.md)根据您的网络环境选择安装Logtail脚本。安装Logtail支持的Liunx系统，请参见[使用限制](install-logtail-on-a-linux-server.md)。
