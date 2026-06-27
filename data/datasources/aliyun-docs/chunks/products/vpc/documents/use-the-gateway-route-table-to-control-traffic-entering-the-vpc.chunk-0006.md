### 结果验证
注意检查[网络](network-acl-overview.md)[ACL](network-acl-overview.md)与[安全组概述](../../ecs/documents/user-guide/overview-44.md)的配置，避免VPC内的ECS测试连通性时受到影响。
验证公网入向流量访问
浏览器访问ECS-B公网IPhttp://<ECS-B 弹性公网IP>。
页面返回This is ECS–B!，表示请求已成功路由至 ECS-B 实例。
验证公网入向流量流经ECS-A
登录ECS-A，执行tcpdump dst host <ECS-B 私网IP>，抓取目的地为ECS-B的流量。
浏览器访问ECS-B公网IP，查看ECS-A抓包结果。
[root@ECS-A ~]# tcpdump dst host 10.0.1.221 dropped privs to tcpdump tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes 17:33:36.662426 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [S], seq 884222365, w 17:33:36.662445 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [S], seq 884222365, w 17:33:36.662818 IP 140.2xxx.xxx.37526 > 10.0.1.221.http: Flags [S], seq 3020843667, 17:33:36.662823 IP 140.2xxx.xxx.37526 > 10.0.1.221.http: Flags [S], seq 3020843667, 17:33:36.676731 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [.], ack 1519927262, 17:33:36.676737 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [.], ack 1, win 2058
