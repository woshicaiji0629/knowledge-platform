远程登录ECS01和ECS02实例，具体操作，请参见[ECS](../../../../ecs/documents/user-guide/connect-to-instance.md)[远程连接操作指南](../../../../ecs/documents/user-guide/connect-to-instance.md)。
在ECS01中执行如下命令，部署Nginx服务。
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! this is ipv4 rs." > index.html
在ECS02中执行如下命令，部署Nginx服务。
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! this is ipv6 rs." > index.html
配置ECS02实例的IPv6地址。具体操作请参见[IPv6](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
说明
如果您的ECS02实例镜像为Alibaba Cloud Linux 3.2104 LTS 64，并且在创建时已在IPv6处选中免费分配IPv6地址，可忽略此步骤。
远程登录VPC中的ECS02实例。
配置IPv6地址。
执行ip addr | grep inet6或者ifconfig | grep inet6命令。
如下所示，表示已成功配置IPv6地址，您可忽略此步骤。
[root@iZbpxxx fxe4Z ~]# ip addr | grep inet6 inet6 ::1/128 scope host inet6 2408:4005:xxx:xxx:7cd5:aa9c/128 scope global dynamic noprefixroute inet6 fe80::xxx:cc1c/64 scope link noprefixroute
如果未返回inet6相关内容，表示实例未开启IPv6服务，
