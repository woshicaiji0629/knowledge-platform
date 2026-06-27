a.kubernetes.io/alibaba-cloud-loadbalancer-protocol-port | https:443 |
| 注解二 | service.beta.kubernetes.io/alibaba-cloud-loadbalancer-cert-id | ${YOUR_CERT_ID} |

说明
将${YOUR_CERT_ID}替换成[步骤](access-applications-in-an-ack-cluster-over-https.md)[7](access-applications-in-an-ack-cluster-over-https.md)[配置](access-applications-in-an-ack-cluster-over-https.md)[SSL](access-applications-in-an-ack-cluster-over-https.md)[证书](access-applications-in-an-ack-cluster-over-https.md)生成的证书ID。
您还可以使用YAML方式添加注解内容，完整YAML示例如下：
apiVersion: v1 kind: Service metadata: annotations: service.beta.kubernetes.io/alibaba-cloud-loadbalancer-protocol-port: "https:443" service.beta.kubernetes.io/alibaba-cloud-loadbalancer-cert-id: "${YOUR_CERT_ID}" name: nginx namespace: default spec: ports: - name: https port: 443 protocol: TCP targetPort: 80 - name: http port: 80 protocol: TCP targetPort: 80 selector: run: nginx type: LoadBalancer
说明
HTTPS的443端口对应的targetPort端口需要配置成HTTP的端口80。
访问HTTPS的Nginx应用，在浏览器中输入https://<slb-instance-ip>并进行访问。
页面成功显示 nginx 默认欢迎页面，标题为Welcome to nginx!，表明 Nginx 应用已正常运行，HTTPS 访问配置生效。
