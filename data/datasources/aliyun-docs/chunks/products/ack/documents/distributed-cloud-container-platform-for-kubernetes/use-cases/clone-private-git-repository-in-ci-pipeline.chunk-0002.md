## 在工作流集群中保存私有仓库凭据
Clone私有仓库前，您需要先在工作流集群中执行如下命令保存私有仓库所需的用户名、密码和ssh private key。
username、password和ssh-private-key需要替换为您实际使用的参数值。
kubectl create secret generic git-creds --from-literal="username=${username}" --from-literal="password=${password or token}" --from-file=ssh-private-key=${ssh private key path} # example # kubectl create secret generic git-creds --from-literal="username=demo" --from-literal="password=ghp_GePB****************d407" --from-file=ssh-private-key=$HOME/.ssh/id_rsa
