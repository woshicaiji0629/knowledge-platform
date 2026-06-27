## 适用范围
已[获取集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[KubeConfig](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[并通过](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[kubectl](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[工具连接集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)。
已[创建](../../../../rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[RDS MySQL](../../../../rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)[实例与配置数据库](../../../../rds/documents/apsaradb-rds-for-mysql/step-1-create-an-apsaradb-rds-for-mysql-instance-and-configure-databases.md)。
重要
RDS MySQL实例需要和已创建的容器Argo工作流集群处于同一VPC，并将该VPC网段添加到RDS实例的白名单中。
操作过程中，请记录数据库名称、数据库的用户名和密码（需要具有数据库的读写权限）、RDS实例地址等信息，用于后续步骤。
Argo工作流持久化功能支持RDS MySQL数据库、RDS PostgreSQL数据库。
