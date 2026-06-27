## 配置文件
生成如下的配置文件，并保存在~/.ossutilconfig。
[default] accessKeyID = yourSTSAccessKeyID accessKeySecret = yourSTSAccessKeySecret stsToken = yourSecurityToken region=cn-hangzhou
通过如下命令查询examplebucket中的对象。
ossutil ls oss://examplebucket -c ~/.ossutilconfig
