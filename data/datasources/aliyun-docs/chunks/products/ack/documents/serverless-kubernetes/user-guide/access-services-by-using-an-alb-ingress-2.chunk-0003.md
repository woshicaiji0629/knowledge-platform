## 步骤一：创建AlbConfig
拷贝以下内容到alb-test.yaml文件中，用于创建AlbConfig。
apiVersion: alibabacloud.com/v1 kind: AlbConfig metadata: name: alb-demo spec: config: name: alb-test addressType: Internet zoneMappings: - vSwitchId: vsw-uf6ccg2a9g71hx8go**** - vSwitchId: vsw-uf6nun9tql5t8nh15**** listeners: - port: 80 protocol: HTTP

| 参数 | 说明 |
| --- | --- |
| spec.config.name | （可选）表示 ALB 实例的名称。 |
| spec.config.addressType | （必选）表示负载均衡的地址类型。取值如下： Internet（默认值）：负载均衡具有公网 IP 地址，DNS 域名被解析到公网 IP，因此可以在公网环境访问。 Intranet：负载均衡只有私网 IP 地址，DNS 域名被解析到私网 IP，因此只能被负载均衡所在 VPC 的内网环境访问。 |
| spec.config.zoneMappings | （必选）用于设置 ALB Ingress 交换机 ID，您需要至少指定两个不同可用区交换机 ID，指定的交换机必须在 ALB 当前所支持的可用区内，且与集群处于同一 VPC。关于 ALB Ingress 支持的地域与可用区，请参见 [ALB](../../../../slb/documents/application-load-balancer/product-overview/supported-regions-and-zones.md) [支持的地域与可用区](../../../../slb/documents/application-load-balancer/product-overview/supported-regions-and-zones.md) 。 |

执行以下命令，创建AlbConfig。
kubectl apply -f alb-test.yaml
预期输出：
albconfig.alibabacloud.com/alb-demo created
创建并拷贝以下内容到alb.yaml文件中，用于创建IngressClass。
