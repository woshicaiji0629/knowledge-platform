## 配置文件
生成如下配置文件，并保存在~/.ossutilconfig。
[default] mode = Ali-EcsRamRole # ecsRoleName可以不设置，当不设置时，自动获取。 ecsRoleName = EcsRamRoleOss region=cn-hangzhou
通过如下命令查询examplebucket中的对象。
ossutil ls oss://examplebucket -c ~/.ossutilconfig
