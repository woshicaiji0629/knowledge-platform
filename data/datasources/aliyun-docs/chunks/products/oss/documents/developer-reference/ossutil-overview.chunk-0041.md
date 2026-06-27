## 临时凭证
{ "AccessKeyId" : "ak", "AccessKeySecret" : "sk", "Expiration" : "2023-12-29T07:45:02Z", "SecurityToken" : "token" }
生成如下配置文件，并保存在~/.ossutilconfig。不支持通过环境变量或者命令行选项方式设置。
[default] mode = Process credentialProcess = user-cmd region=cn-hangzhou
通过如下命令查询examplebucket中的对象。
ossutil ls oss://examplebucket -c ~/.ossutilconfig
