## 步骤一：配置会话保持
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏处，选择后端服务器组所属的地域。
在左侧导航栏，选择应用型负载均衡 ALB>服务器组。
在服务器组页面，找到目标服务器组，在操作列单击编辑基本信息。
在编辑基本信息对话框中，开启会话保持。
打开会话保持开关并选择Cookie处理方式。
选择植入Cookie，输入会话保持超时时间，然后单击保存。
超时时间不宜设置过长（建议短连接场景设置为60~300秒），否则同一客户端的请求会持续路由到同一台后端服务器，可能导致负载不均衡。
选择重写Cookie，输入Cookie名称，然后单击保存。
本文示例将Cookie名称设置为BACKEND_SERVER，该名称仅为示例，您可以自定义该名称。
