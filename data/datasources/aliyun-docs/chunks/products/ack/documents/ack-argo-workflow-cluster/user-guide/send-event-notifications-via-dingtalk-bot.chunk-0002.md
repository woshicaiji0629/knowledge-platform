## 工作原理
外部系统一般通过暴露HTTP Webhook接口的方式，接收消息输入。
Argo工作流支持Exit Handler机制，可以在步骤中或在工作流本身定义exit-handler。
Exit Handler以容器的方式运行。您可以在容器中运行curl命令向外部系统发送HTTP消息，从而实现事件通知。
