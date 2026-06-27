## 操作步骤
将下方的示例保存到rds-user.yaml，然后执行kubectl apply -f rds-user.yaml创建Secret。
apiVersion:v1stringData:username:DATABASE_USERNAME# 替换为数据库的用户名。password:DATABASE_PASSWORD# 替换为数据库的密码。kind:Secretmetadata:name:argo-mysql-confignamespace:defaulttype:Opaque
将下方命令中的CLUSTER_ID替换为集群ID，然后执行命令编辑ConfigMap， 添加持久化相关配置。
kubectl edit configmap -nCLUSTER_IDworkflow-controller-configmap
配置项：
host：设置为RDS MySQL实例的地址。
database：设置为数据库的名称。
archive：开启持久化功能，需要设置为true。
archiveTTL：持久化数据的保存时间。示例中设置为30d，表示工作流持久化到数据库中保存30天。
nodeStatusOffLoad：开启工作流状态卸载（Offload）功能，需设置为true。开启后，工作流节点状态将存储在数据库中而非etcd，从而支持包含大规模子任务的单体工作流。
persistence: | connectionPool: maxIdleConns: 100 maxOpenConns: 0 connMaxLifetime: 0s # 0 means connections don't have a max lifetime. archiveTTL: 30d archive: true nodeStatusOffLoad: true mysql: host: rm-xxx.mysql.cn-beijing.rds.aliyuncs.com port: 3306 database: argo-workflow tableName: argo_workflows userNameSecret: name: argo-mysql-config key: username passwordSecret: name: argo-mysql-config key: password
配置完成后，重启Argo Server，并确认Pod是否正常更新。
kubectl rollout restart deployment -nCLUSTER_IDargo-server
重要
如果重启Argo Server后，Pod出现反复重启状况，可能是由于网络连接出现问题。请检查集群和数据库实例是否处于同一个VPC，数据库白名单是否允许集群访问。
该文章对您有帮助吗？
反馈
