## 前置准备
开通服务与准备账号
开通日志服务：首次使用时，请登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.36447c08Bv7DT1)，根据页面提示开通服务。
准备账号：
阿里云主账号登录：默认拥有全部权限，可直接操作。
RAM用户登录：需要主账号[授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)相应权限策略：
AliyunLogFullAccess：用于创建和管理日志服务的Project和LogStore等资源。
AliyunECSFullAccess：用于在ECS实例上安装采集Agent。
AliyunOOSFullAccess：用于通过阿里云运维编排服务（OOS）在ECS实例中自动安装采集Agent。
在实际生产过程中，可以通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)，对RAM用户实现更精细化的权限管理
准备ECS实例
确保[ECS](../../ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)[实例](../../ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)的安全组配置满足出口方向开放80（HTTP）端口和443（HTTPS）端口。
生成模拟日志
[登录](../../ecs/documents/user-guide/connect-to-an-instance-overview.md)[ECS](../../ecs/documents/user-guide/connect-to-an-instance-overview.md)[实例](../../ecs/documents/user-guide/connect-to-an-instance-overview.md)。
创建脚本文件generate_nginx_logs.sh并粘贴以下内容。该脚本向/var/log/nginx/access.log文件中每5秒写入一条标准的Nginx访问日志。
generate_nginx_logs.sh
#!/bin/bash #============================================================================== # 脚本名称: generate_nginx_logs.sh # 脚本描述: 模拟NGINX服务器，持续向access.log写入日志。 #========
