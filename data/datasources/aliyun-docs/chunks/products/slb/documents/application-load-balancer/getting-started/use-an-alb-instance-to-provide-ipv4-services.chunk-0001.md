## 前提条件
您已在华东2（上海）地域创建了一个专有网络VPC1，并分别在可用区E和可用区G创建了一个交换机VSW1和VSW2。具体操作，请参见[创建专有网络和交换机](../../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)。
如果计划将ALB部署在交换机VSW1和VSW2，需注意：[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)会从每个指定的交换机中分配3个IP地址，包含1个VIP（对外提供服务）和2个Local IP（用于与后端服务器通信），如果IP不足会出现报错并且无法创建实例，请确保交换机VSW1和VSW2中已预留足够的可用IP；升级前的ALB实例不受该限制。
说明
为确保ALB升级实例各项弹性能力可用，建议您在ALB实例所在的每个交换机内预留至少8个IP地址。
为确保ALB升级实例与后端服务正常连通，如您的后端服务中存在访问策略（包括iptables或其他任何第三方安全策略软件），建议您提前放通ALB实例所属交换机网段。
您已分别在VSW1和VSW2创建ECS01和ECS02实例，且ECS01和ECS02实例中部署了应用服务。
关于创建ECS实例，请参见[自定义购买实例](../../../../ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。
本文ECS01和ECS02部署测试应用示例如下：
ECS01服务部署命令
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is ECS01." > index.html
ECS02服务部署命令
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is ECS02." > index.html
您已经注册域名并完成备案。具体操作，请参见[注册阿里云域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)、[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案流程](https://help.ali
