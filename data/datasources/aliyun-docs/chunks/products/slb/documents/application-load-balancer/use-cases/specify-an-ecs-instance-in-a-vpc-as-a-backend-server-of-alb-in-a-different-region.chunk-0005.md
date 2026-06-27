6.1.0/24 |
| VSW2 | 可用区 B | 172.16.2.0/24 |  |  |
| 华东 1（杭州） | VPC2 主网段：192.168.0.0/16 | VSW3 | 可用区 H | 192.168.1.0/24 |
| VSW4 | 可用区 I | 192.168.2.0/24 |  |  |

已在VSW1中创建ECS01，在VSW3中创建ECS02，且ECS01和ECS02中均部署了应用服务。
单击查看ECS中测试服务部署命令示例。
ECS01部署命令示例
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is chengdu ECS01." > index.html
ECS02部署命令示例
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is hangzhou ECS02." > index.html
已在VPC1中创建了一个公网[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。
已[注册域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)并完成[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)，且通过自有域名[为](../user-guide/configure-cname-resolution-for-alb.md)[ALB](../user-guide/configure-cname-resolution-for-alb.md)[配置](../user-guide/configure-cname-resolution-for-alb.md)[CNAME](../user-guide/configure-cname-resolution-for-alb.md)[解析](../user-guide/configure-cname-resolution-for-alb.md)。
已创建[云企业网实例](../../../../cen/documents/user-guide/cen-instances-1.md)，并在云企业网实例下的西南1（成都）地域和华东1（杭州）地域分别创建了[转发路由器实例](../../../../cen/documents/user-guide/transit-routers.md)。
