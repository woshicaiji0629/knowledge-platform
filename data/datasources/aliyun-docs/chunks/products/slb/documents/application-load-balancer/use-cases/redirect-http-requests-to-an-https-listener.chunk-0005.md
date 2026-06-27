## 前提条件
已[创建公网](../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)（基础版、标准版和WAF增强版均支持）。
已为ALB实例[创建服务器组](../user-guide/create-and-manage-a-server-group.md)（后端协议为HTTP）。
已在ALB实例的服务器组中分别添加ECS01和ECS02实例，并在ECS01和ECS02中均部署了应用服务。
本文以Alibaba Cloud Linux 3操作系统为例，并使用Nginx配置HTTP 80服务。
参考示例：ECS01部署测试服务
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is ECS01." > index.html
已为ALB实例[创建](../../add-an-http-listener.md)[HTTP](../../add-an-http-listener.md)[监听](../../add-an-http-listener.md)。
已[注册自有域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)并完成[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)，且通过自有域名[为](../user-guide/configure-cname-resolution-for-alb.md)[ALB](../user-guide/configure-cname-resolution-for-alb.md)[配置](../user-guide/configure-cname-resolution-for-alb.md)[CNAME](../user-guide/configure-cname-resolution-for-alb.md)[解析](../user-guide/configur
