## 在自己的应用中集成会话管理远程登录功能
通过会话管理远程连接到云服务器或托管实例的完整代码，请参考开源项目[cloud-assistant-starter](https://github.com/aliyun/cloud-assistant-starter)。本项目中[AxtSession.tsx](https://github.com/aliyun/cloud-assistant-starter/blob/master/src/main/resources/static/components/session/AxtSession.tsx)文件包含了调用API接口[StartTerminalSession - 开始终端会话](../developer-reference/api-ecs-2014-05-26-startterminalsession.md)获取WebSocketURL并建立连接的示例代码，将这段代码移植到您自己的企业应用中，即可使用会话管理连接实例。
该文章对您有帮助吗？
反馈
