### 步骤一：配置HTTPS监听
在[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)顶部菜单栏选择ALB实例所属地域。
在ALB实例页面，单击目标实例ID。
在监听页签，单击创建监听。
在负载均衡业务配置向导页面，完成以下配置，然后单击下一步。
此处仅列出和本文强相关的配置项，[HTTPS](../user-guide/add-an-https-listener.md)[监听其他参数配置](../user-guide/add-an-https-listener.md)可保持默认值或根据实际情况修改。
在配置监听配置向导，选择监听协议为HTTPS，监听端口为443，然后单击下一步。
在配置SSL证书配置向导，选择已创建好的服务器证书。然后单击下一步。
在选择服务器组配置向导，选择已创建好的服务器组，并查看后端服务器信息，然后单击下一步。
在配置审核配置向导页面，确认配置信息，单击提交。
