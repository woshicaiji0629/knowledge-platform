## 配置使用RDS
创建阿里云RDS MySQL实例。具体操作，请参见[快速创建](../../../../rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](../../../../rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](../../../../rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)。
重要
设置网络时，选择的VPC和工作流集群所使用的VPC要保持一致，设置白名单时需放开该VPC网段。
创建数据库和账号。具体操作，请参见[创建数据库和账号](../../../../rds/documents/create-databases-and-accounts-for-an-apsaradb-rds-for-mysql-instance.md)。
将下方YAML模板保存到argo-mysql-config.yaml，然后执行kubectl create -f argo-mysql-config.yaml，在工作流集群中创建一个名为argo-mysql-config的Secret，用于保存数据库的账号和密码。
username和password需要分别替换为您上一步骤实际创建的数据库账号和密码。apiVersion: v1 stringData: username: database-username password: database-password kind: Secret metadata: name: argo-mysql-config namespace: default type: Opaque
编辑workflow-controller-configmap，增加持久化配置。
说明
workflow-controller-configmap文件位于以集群ID命名的命名空间中。
host为RDS实例地址RDS MySQL实例的地址。
database为数据库的名称。
archive需要设置为true。
archiveTTL为持久化的保存时间，本示例设置为30d，表示工作流持久化到数据库中可以保存30天。该参数取值大小无限制。
persistence: | connectionPool: maxIdleConns: 100 maxOpenConns: 0 connMaxLifetime: 0s # 0 means connections don't have a max lifetime. archiveTTL: 30d archive: true mysql: host: rm-xxx.mysql.
