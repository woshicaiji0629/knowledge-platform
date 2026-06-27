## Node.js
安装Credentials工具。
若使用加固模式获取临时身份凭证，credentials的版本不低于2.3.1。npm install @alicloud/credentials
配置ECS实例RAM角色作为访问凭证。
constCredential=require('@alicloud/credentials');constcredentialsConfig =newCredential.Config({type:'ecs_ram_role',// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置roleNameroleName:'ROLENAME',// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。disableIMDSv1:true, });constcred =newCredential.default(credentialsConfig);
以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。
RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。constOSS=require('ali-oss');constCredential=require('@alicloud/credentials');asyncfunctionlistObjects() {constroleName ='YOUR_ROLE_NAME';constbucketName ='YOUR_BUCKET_NAME';constregion ='YOUR_REGION';// 注意：OSS SDK 通常只需要 region// 1. 初始化 Credentials (ECS 模式)constcredentialsConfig =newCredential.Config({type:'ecs_ram_role',roleName: roleName });constcredClient =newCredential.default(credentialsConfig);try{// 2. 获取凭证constaccessKeyId =awaitcredClient.getAccessKeyId();constaccessKeySecret =awaitcredClient.getAccessKeySecret();constsecurityToken =awaitcredClient.getSecurityToken();// 3. 初始化 OSS Clientconstclient =newOSS({region:
