## 步骤三：测试会话保持的有效性
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏选择地域。找到目标ALB实例，复制其对应的DNS名称。
在浏览器中输入DNS名称，可访问某个服务器，多次刷新页面仍然访问相同服务器。
例如您第一次访问的是ECS01，则后续几次刷新后均是访问ECS01。
如果多次刷新页面后在ECS01与ECS02之间切换，则会话保持配置不生效，请您检查配置是否有误再重新测试。
