Secret、挂载的NAS存储卷都需要与最终提交的工作流处于同一命名空间。kubectl create secret generic docker-config --from-literal="config.json={\"auths\": {\"$repositoryDomain\": {\"auth\": \"$(echo -nUSER_NAME:PASSWORD|base64)\"}}}"
