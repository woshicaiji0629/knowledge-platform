| 访问对象 | 公网访问域名 | 端口 | 说明 |
| --- | --- | --- | --- |
| 容器服务控制面 | cs-anony.aliyuncs.com cs-anony.{region}.aliyuncs.com | TCP 443（集群版本 ≥ 1.26） TCP 80（集群版本＜1.26） | 容器服务管控地址。 |
| 组件安装包 | aliacs-k8s-{region}.oss-{region}.aliyuncs.com | TCP 443（集群版本 ≥ 1.26） TCP 80 和 443（集群版本＜1.26） | OSS 下载地址。可通过 OSS 下载 edgeadm 、kubelet、CNI、runtime、edgehub 等安装包。 |
| API Server 公网端点 | 通过集群 基本信息 页签查看。 | TCP 6443 | 与 kube-apiserver 交互。 |
| Tunnel-server 公网 SLB（集群版本＜1.26） | 通过集群 Service（服务）资源查看： kube-system/x-tunnel-server-svc | TCP 10262、10263 | 边缘隧道。 |
| Raven 云端网关 SLB | 通过集群 Service（服务）资源查看： kube-system/x-raven-proxy-svc-gw-cloud-xxx kube-system/x-raven-tunnel-svc-gw-cloud-xxx | TCP [10280,10284] UDP 4500 | Raven 隧道。 |
| NTP | ntp1.aliyun.com cn.ntp.org.cn | 与 NTP 协议有关，一般是 UDP 123 端口。 | 时钟同步服务器地址。 接入时若选择配置 selfHostNtpServer 参数为 true ，即已手动完成时间同步，则不需要使用该地址。 |
| 系统组件镜像地址 | dockerauth.{region}.aliyuncs.com 重要 如果地域为 cn-zhangjiakou，此处对应的 Docker 公网访问域名需修改为 dockerauth-{region}.aliyuncs.com。 dockerauth-ee.{region}.aliyuncs.com registry-{region}.ack.aliyuncs.com | TCP 443 | 系统组件镜像需要使用的地址。 |
| 系统工具 | 系统工具在线安装（无需额外域名） net-tools、iproute、chrony（或者 ntpdate）、crontabs、pciutils、socat、ebtables、iptables、conntrack-tools | 不涉及
