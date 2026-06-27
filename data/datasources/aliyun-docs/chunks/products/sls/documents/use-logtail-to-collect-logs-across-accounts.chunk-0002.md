## 步骤一：创建用户标识文件
登录阿里云账号B下的ECS服务器。
重要
您需要在ECS集群B的每台ECS服务器中创建用户标识文件。
执行如下命令创建用户标识文件。
您需要配置阿里云账号A为用户标识，即创建阿里云账号A的同名文件。更多信息，请参见[配置用户标识](configure-a-user-identifier.md)。
touch /etc/ilogtail/users/12****456
