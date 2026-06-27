## 连接实例
通过SSH方式登录ECS实例，就可以进行部署业务、搭建应用等操作。
获取实例的公网IP信息。
调用[DescribeInstances](api-ecs-2014-05-26-describeinstances.md)，通过<实例ID>获取实例的公网IP信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds '["<实例ID>"]'
返回示例
参数PublicIpAddresses为实例的公网IP信息。
"PublicIpAddress": { "IpAddress": [ "115.29.xxx.xxx" ] }
连接ECS实例。
ssh <用户名>@<公网IP>[root@i-xxx bfZ ~ ]# ssh root@1xxx The authenticity of host 'xxx (xxx)' can't be established. ECDSA key fingerprint is SHA256:PVyhCaxxx4mecykrU. Are you sure you want to continue connecting (yes/no/[fingerprint])? yes Warning: Permanently added 'xxx' (ECDSA) to the list of known hosts. root@1xxx's password: Welcome to Alibaba Cloud Elastic Compute Service ! Last login: Thu Oct 10 13:31:58 2024 from xxx.67 [root@iZ xxx ugZ ~]#
