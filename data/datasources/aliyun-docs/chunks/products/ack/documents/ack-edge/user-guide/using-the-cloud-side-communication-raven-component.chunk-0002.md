## 注意事项
Raven组件的跨域通信能力依赖弹性公网IP、传统型负载均衡CLB、访问控制ACL等云资源。
托管组件Edge-Controller-Manager（ECM）会根据您是否开启Raven的跨域通信能力来购买CLB、EIP、ACL等云产品资源；关闭或卸载Raven跨域能力则会释放相关云产品资源。您可以根据实际需求变配云产品的资源规格。
以上云资源的命名方式为k8s/raven-agent-ds/kube-system/{CLUSTER_ID}，请勿修改资源名称，否则可能导致ECM组件无法识别该资源，进而导致资源泄露问题。
请勿擅自删除以上资源导致Raven能力不可用。
云资源信息记录在集群资源configmap kube-system/raven-cfg中，请勿手动删除。
展开查看raven-cfg的示例代码
apiVersion: v1 kind: ConfigMap metadata: name: raven-cfg namespace: kube-system data: acl-id: acl-xxx acl-entry: "" eip-id: eip-xxx eip-ip: 47.XX.XX.47 enable-l3-tunnel: "false" enable-l7-proxy: "true" loadbalancer-id: lb-xxx loadbalancer-ip: 192.XX.XX.1
