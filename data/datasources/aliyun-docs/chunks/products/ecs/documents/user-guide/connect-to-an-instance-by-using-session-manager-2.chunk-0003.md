### 使用限制&前提条件
仅支持连接到运行中状态的实例。
实例需安装云助手Agent：会话管理基于云助手的功能实现，需要在实例中安装云助手Agent。
2017年12月01日之后使用官方公共镜像创建的ECS实例，默认预装了云助手Agent。如果您的实例是2017年12月01日之前购买的或使用自行上传的自定义镜像创建的实例，若需要使用云助手相关功能，需自行安装云助手Agent，具体操作，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
使用前请确保网络连通：由于云助手Agent会通过WebSocket协议与云助手服务端通讯，需要确保实例与云助手服务端的网络连通性，具体说明，请参见[相关安全组设置](connect-to-an-instance-by-using-session-manager-2.md)。
会话限制：在同一地域下，已创建并可用的会话不能超过 1000 个，单台实例处于连接状态的会话不能超过 20 个，单个会话连接的带宽限制为200kb/s。
