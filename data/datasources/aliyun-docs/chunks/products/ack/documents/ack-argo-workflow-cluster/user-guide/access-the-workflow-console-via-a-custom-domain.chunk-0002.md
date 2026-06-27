## 操作步骤
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。
在集群信息页面，单击工作流控制台（Argo）。然后，从浏览器中复制工作流控制台IP地址。
登录[云解析](https://dnsnext.console.aliyun.com/authoritative)[DNS-公网权威解析](https://dnsnext.console.aliyun.com/authoritative)控制台，为自定义域名添加一条A类型记录，将自定义域名指向工作流控制台IP地址。
准备SSL证书，记录证书文件cert.pem和key.pem的路径。
将SSL证书配置到集群。
将CLUSTER_ID替换为集群ID，填入证书文件路径，然后执行以下命令，在集群中创建名为argo-server-tls的Secret。
kubectl create -nCLUSTER_IDsecret tls argo-server-tls \ --cert=/path/to/cert.pem \ --key=/path/to/key.pem
将已创建的Secret配置到集群的argo-server中。
将CLUSTER_ID替换为集群ID，填入证书文件路径，然后执行以下命令，编辑argo-server文件。
kubectl -nCLUSTER_IDedit deploy argo-server
在spec.template.spec.containers.args部分添加TLS配置信息。
spec: containers: - args: - server - --auth-mode=sso - --auth-mode=client - --kube-api-qps=300 - --kube-api-burst=500 - --tls-certificate-secret-name=argo-server-tls image: ******.ack.aliyuncs.com/acs/argo:v3.5.13-a06e2ae imagePullPolicy: IfNotPresent
将自定义域名修改至RAM中OAuth应用的回调地址中。
使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择集成管理>OAuth应用（公测）。
在企业应用页签，单击目标应用ac
