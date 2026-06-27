ser-guide/create-certificate.md)。
在证书列表中，找到目标证书名称下面的证书ID。
在容器服务管理控制台的服务列表中，找到之前创建的服务，单击右侧操作列下的更新。
在更新服务对话框中的注解区域，添加以下两个注解内容。
请勿复用集群 APIServer 的 SLB，否则将导致集群访问异常。

| 注解 | 名称 | 值 |
| --- | --- | --- |
| 注解一 | service.beta.kubernetes.io/alibaba-cloud-loadbalancer-protocol-port | https:443 |
| 注解二 | service.beta.kubernetes.io/alibaba-cloud-loadbalancer-cert-id | ${YOUR_CERT_ID} |
