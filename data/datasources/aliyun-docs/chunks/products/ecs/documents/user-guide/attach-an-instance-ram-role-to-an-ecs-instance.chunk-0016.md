## .NET
安装Credentials工具。
若使用加固模式获取临时身份凭证，credentials的版本不低于1.4.2。dotnet add package Aliyun.Credentials
配置ECS实例RAM角色作为访问凭证。
usingAliyun.Credentials.Models;namespacecredentials_demo{classProgram{staticvoidMain(string[] args){varconfig =newConfig(); { Type ="ecs_ram_role",// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置RoleNameRoleName ="ROLE_NAME",// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。DisableIMDSv1 =true} } } }
以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。
RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。usingSystem;usingAliyun.OSS;usingAliyun.Credentials.Models;usingAliyun.Credentials;namespaceEcsRoleDemo{classProgram{staticvoidMain(string[] args){stringroleName ="YOUR_ROLE_NAME";stringendpoint ="YOUR_ENDPOINT";stringbucketName ="YOUR_BUCKET_NAME";// 1. 配置 Credentials (ECS 模式)Config credConfig =newConfig { Type ="ecs_ram_role", RoleName = roleName }; Client credClient =newClient(credConfig);try{// 2. 获取凭证 (C# SDK 内部自动处理异步请求)stringak = credClient.GetAccessKeyId();stringsk = credClient.GetAccessKeySecret();stringtoken = credClient.GetSecurityToken();// 3. 初始化 OSS Client// 注意：在实际长驻服务中，建议封装逻辑以定期重新获取 TokenOssClient ossClient =newOssClient(e
