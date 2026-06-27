## 前提条件
待连接实例状态为运行中
实例运行状态可以在ECS控制台中的实例模块查看，运行中的实例如图所示：
查看实例状态的操作说明，请参见[查看实例信息](view-instance-information.md)。

|  |  |
| --- | --- |

实例需安装云助手Agent
会话管理基于云助手的功能实现，需要在实例中安装云助手Agent。云助手Agent状态可以在ECS控制台的云助手模块查看，已经安装云助手的实例如图所示：
2017年12月01日之后使用官方公共镜像创建的ECS实例，默认预装了云助手Agent。如果您的实例是2017年12月01日之前购买的或使用自行上传的自定义镜像创建的实例，需自行安装云助手Agent，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。

|  |  |
| --- | --- |

查看云助手Agent状态以及处理异常状态的具体操作，请参见[查看云助手状态及异常状态处理](check-the-status-of-cloud-assistant-and-handle-exceptions.md)。
确保网络连通（设置安全组）
通过会话管理连接ECS实例时，需要确保ECS中运行的云助手Agent与云助手服务端的网络连通性，即在安全组出方向设置以下规则：
与SSH、RDP等连接方式不同，由于会话管理是由云助手Agent主动与会话管理服务端建立WebSocket连接，因此仅需放行出方向的云助手服务端的WebSocket端口。关于会话管理的原理，请参见[会话管理工作原理](connect-to-an-instance-by-using-session-manager-2.md)。
重要
如果使用普通安全组（包括默认安全组），默认情况下会放行所有的出方向流量，无需配置。
如果使用企业安全组，默认情况下会禁用所有出方向的流量，需要配置以下规则。更多关于企业安全组的说明，请参见[普通安全组与企业级安全组](basic-security-groups-and-advanced-security-groups.md)。
添加安全组规则的具体操作，请参见[添加安全组规则](add-a-security-group-rule.md)。
