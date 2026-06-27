### 步骤一：在工作流集群中创建ACR EE访问凭证
ACR EE访问凭证主要用于BuildKit推送镜像。
为ACR EE配置访问凭证。具体操作，请参见[配置访问凭证](https://help.aliyun.com/zh/acr/user-guide/configure-access-credentials)。
执行如下命令，在工作流集群中创建Secret保存ACR EE的密码，供BuildKit使用。
$username:$password需要替换为您实际为ACR EE配置的访问凭证信息。
kubectl create secret generic docker-config --from-literal="config.json={\"auths\": {\"$repositoryDomain\": {\"auth\": \"$(echo -n $username:$password|base64)\"}}}"
