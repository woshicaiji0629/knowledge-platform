## （可选）关闭按需加载镜像使用P2P加速
说明
以下是集群内修改单节点配置的参考步骤。您需关注节点的后续运维操作，是否会覆盖此配置。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点。
在节点页面，单击目标节点IP地址下的实例ID。
在实例详情页面，使用远程连接，登录节点。
使用vi命令编辑/etc/overlaybd/overlaybd.json文件中的p2pConfig，将enable改为false。
{ "p2pConfig": { "enable": false, "address": "https://localhost:6****/accelerator" }, ... ... }
执行如下命令，重新按需加载的组件。
service overlaybd-tcmu restart
