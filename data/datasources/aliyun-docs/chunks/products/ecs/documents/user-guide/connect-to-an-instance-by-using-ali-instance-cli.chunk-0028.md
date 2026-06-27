00.0.0/16 | 用于访问云助手服务端。 |
| 允许 | 1 | 自定义 TCP | 443 | 100.0.0.0/8 | 访问 云助手 Agent 安装包所在服务器，用于安装或更新您的 云助手 Agent 。 |
| 允许 | 1 | 自定义 UDP | 53 | 0.0.0.0/0 | 用于解析域名。 |

此外，如果您计划仅通过会话管理连接实例，为了增加ECS实例的安全性，您可以取消放行安全组入方向上的SSH端口（默认22）或者RDP端口（默认3389）的规则。
执行命令后出现DeliveryTimeout提示（云助手Agent不在线）
如图所示，如果执行ali-instance-cli的命令时出现DeliveryTimeout提示，可能是云助手Agent不在线，检查云助手状态，请参见[检查实例云助手](connect-to-an-instance-by-using-ali-instance-cli.md)[Agent](connect-to-an-instance-by-using-ali-instance-cli.md)[是否已安装](connect-to-an-instance-by-using-ali-instance-cli.md)。
执行命令报错session manager is disabled, please enable first
如果执行ali-instance-cli的命令出现session manager is disabled, please enable first报错，代表会话管理功能未开启，请通过控制台开启会话管理功能，具体操作，请参见[开启会话管理服务](connect-to-an-instance-by-using-ali-instance-cli.md)。
长时间未连接自动断开
使用会话管理连接到目标实例后，如果长时间没有任何操作连接会自动断开。默认的连接空闲时间为3分钟，可以通过--idle-timeout参数自定义最大空闲时间。
例如执行以下命令连接到目标实例后，连接空闲达到10分钟就会自动断开。
./ali-instance-cli session --instance instance-id --idle-timeout 600
说明
此功能需确保ali-instance-cli不低于以下版本：
Linux：1.2.0.48
Windows：1.1.0.48
macOS：1.3.0.48
如何分析ali-instance-cli的日志
当使用会话管理CLI出现问题时，可以通过查看log分析具体问题。
查看会话管理CLI工具的日志：在使用会话管理CLI（ali-instance-cli）时，会在该工具所在目录下生成log目录，如~/log/aliyun_ecs_session_log.2022XXXX，可以进入该目录查看相关日志。
查看云助手Agent日志：
Linux
/usr/local/share/aliyun-assist/云助手版本号/log/
Windows
C:\ProgramData\aliyun\assist\云助手版本号\log
该文章对您有帮助吗？
反馈
