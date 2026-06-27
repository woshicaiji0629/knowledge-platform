x Enterprise Server、FreeBSD、CoreOS、Fedora CoreOS、Fedora、Rocky Linux 和 AlmaLinux 等 | 对于开源操作系统镜像，建议联系开源社区获得技术支持，同时阿里云提供相应的技术协助。 对于商业版镜像，阿里云提供许可证并联合操作系统原厂提供技术支持。 |

说明
以上技术支持的前提条件是镜像在生命周期之内，如果操作系统版本结束了生命周期（EOL），则参照EOL镜像的支持策略。更多信息，请参见[操作系统生命周期概述](eol-overview.md)。
针对各个操作系统的新特性、安全补丁等，阿里云会定期更新公共镜像的版本，详情请参见[公共镜像发布记录](release-notes-for-2023.md)。您在ECS购买页面选中某个公共镜像时，默认为最近更新的版本。如果您希望购买到较旧的版本，可以通过调用OpenAPI[RunInstances](../api-runinstances.md)指定镜像ID来实现。
阿里云会定时从开源社区官方或者操作系统原厂同步至[阿里云镜像站](https://developer.aliyun.com/mirror/)，您可以按需更新新特性、安全补丁等。
安全性是阿里云和客户的共同责任。阿里云负责云平台自身的安全，包括云平台硬件、软件和网络安全。客户负责ECS实例的安全，包括ECS操作系统的管理（包括安装更新和安全补丁）、在ECS上安装的任何应用程序软件或工具，以及阿里云提供的安全组防火墙的配置。更多信息，请参见[云服务器](best-security-practices.md)[ECS](best-security-practices.md)[安全性](best-security-practices.md)。
如果操作系统EOL，阿里云可能会对该操作系统停止技术支持，并可能下线相关的公共镜像。此时无法使用镜像族系查询对应的公共镜像后创建ECS实例。建议您尽快将运行的工作负载迁移到替代的操作系统，以继续获取软件更新和安全补丁。更多信息，请参见[操作系统维护周期和](image-eol.md)[EOL](image-eol.md)[应对方案](image-eol.md)。
