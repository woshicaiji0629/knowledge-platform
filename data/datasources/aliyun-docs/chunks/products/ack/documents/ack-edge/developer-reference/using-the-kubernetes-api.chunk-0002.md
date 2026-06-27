3A%22AliyunCSManagedNetworkRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedNetworkRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSDefaultRole%22%2C%22TemplateId%22%3A%22Default%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedKubernetesRole%22%2C%22TemplateId%22%3A%22ManagedKubernetes%22%7D%2C%7B%22RoleName%22%3A%22AliyunCSManagedArmsRole%22%2C%22TemplateId%22%3A%22AliyunCSManagedArmsRole%22%7D%2C%7B%22RoleName%22%3A%22AliyunCISDefaultRole%22%2C%22TemplateId%22%3A%22AliyunCISDefaultRole%22%7D%5D%2C%22Service%22%3A%22CS%22%7D%5D%7D)页面，然后单击确认授权。
完成以上授权后，刷新控制台即可使用容器服务ACK。
在左侧导航栏单击集群列表。
在集群列表页面，单击目标集群名称或者目标集群右侧操作列下的详情。
单击连接信息页签，查看集群访问凭证（KubeConfig），将KubeConfig文件保存到本地。
使用以下命令从KubeConfig文件中提取CA、Key和APIServer信息。
cat ./kubeconfig |grep client-certificate-data | awk -F ' ' '{print $2}' |base64 -d > ./client-cert.pem cat ./kubeconfig |grep client-key-data | awk -F ' ' '{print $2}' |base64 -d > ./client-key.pem APISERVER=`cat ./kubeconfig |grep server | awk -F ' ' '{print $2}'`
