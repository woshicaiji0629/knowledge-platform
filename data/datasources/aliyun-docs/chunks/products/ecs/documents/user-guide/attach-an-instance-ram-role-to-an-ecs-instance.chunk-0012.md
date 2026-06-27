## Go
安装Credentials工具。
若使用加固模式获取临时身份凭证，credentials-go的版本不低于1.3.10。
使用go get下载安装。
go get -u github.com/aliyun/credentials-go
使用dep来管理依赖包。
dep ensure -add github.com/aliyun/credentials-go
配置ECS实例RAM角色作为访问凭证。
packagemainimport("fmt""github.com/aliyun/credentials-go/credentials")func_main(args []*string){ credentialsConfig :=new(credentials.Config). SetType("ecs_ram_role").// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置RoleNameSetRoleName("ROLENAME").// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。SetDisableIMDSv1(true) credentialClient, err := credentials.NewCredential(credentialsConfig)iferr !=nil{panic(err) } }
以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。
RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。packagemainimport("fmt""github.com/aliyun/aliyun-oss-go-sdk/oss""github.com/aliyun/credentials-go/credentials")// 1. 定义结构体实现 OSS 的 CredentialsProvider 接口typeCredentialsProviderAdapterstruct{ credClient credentials.Credential }func(c *CredentialsProviderAdapter)GetCredentials() oss.Credentials {// 获取最新 Tokenid, _ := c.credClient.GetAccessKeyId() secret, _ := c.credClient.GetAccessKeySecret() token, _ := c.credClient.GetSecurityToken()returnoss.
