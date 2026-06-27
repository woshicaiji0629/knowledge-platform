## PHP
安装Credentials工具。
若使用加固模式获取临时身份凭证，credentials的版本不低于1.2.0。composer require alibabacloud/credentials
配置ECS实例RAM角色作为访问凭证。
<?php use AlibabaCloud\Credentials\Credential; use AlibabaCloud\Credentials\Credential\Config; $credConfig = new Config([ 'type' => 'ecs_ram_role', // 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置role_name 'roleName' => '<RoleName>', // 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。 'disableIMDSv1' => true, ]);
以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。
RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。require'vendor/autoload.php';useAlibabaCloud\Credentials\Credential;useOSS\OssClient;useOSS\Core\OssException;$roleName='YOUR_ROLE_NAME';$bucketName='YOUR_BUCKET_NAME';$endpoint='YOUR_ENDPOINT';try{// 1. 配置 Credentials (ECS 模式)$credConfig=newAlibabaCloud\Credentials\Credential\Config(['type'=>'ecs_ram_role','roleName'=>$roleName]);$credClient=newCredential($credConfig);// 2. 获取凭证$ak=$credClient->getAccessKeyId();$sk=$credClient->getAccessKeySecret();$token=$credClient->getSecurityToken();// 3. 初始化 OSS Client$ossClient=newOssClient($ak,$sk,$endpoint,false,$token);echo"--- 开始查询 ---\n";// 4. 查询文件$options=array(OssClient::OSS
