# 给ECS实例授予RAM角色-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/attach-an-instance-ram-role-to-an-ecs-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 实例RAM角色

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

使用实例RAM角色可以在ECS实例内部无需配置AccessKey即可获取STS临时凭证（STS Token），从而调用其他云产品的API。

## 功能优势

- 

安全便捷：无需在ECS上的代码或配置文件中保存AccessKey，通过实例元数据服务（Instance Metadata Service, IMDS）即可自动获取STS临时凭证调用API，从而降低AccessKey泄露的风险。

- 

无缝切换：如需更换应用程序的RAM身份，只需在控制台调整授予ECS的RAM角色，无需修改代码或重启服务。

- 

权限精细化：可以为不同的ECS实例分配不同的RAM角色，实现最小权限原则。

## 操作步骤

若使用RAM用户执行操作步骤，请确保该用户拥有ram:CreateRole（创建角色）、ecs:AttachInstanceRamRole（授予角色）以及 ram:PassRole（传递角色）等权限。更多信息，请参见[如何使用](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)[RAM](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)[用户给实例授予](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)[RAM](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)[角色？](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)。

### 步骤一：创建RAM角色

为ECS实例创建一个RAM角色，并为其分配权限。

控制台

- 

登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)，选择身份管理 > 角色，单击创建角色，填写以下参数，单击确定。

- 

信任主体类型：选择云服务。

- 

信任主体名称：选择云服务器ECS / ECS。

- 

在创建角色对话框，输入角色名称，然后单击确定。

创建成功的RAM角色默认没有任何权限，需要为该RAM角色授权。可将系统策略或已创建的[自定义权限策略](products/ram/documents/create-a-custom-policy.md)授权给RAM角色，使其拥有相关的资源访问或操作权限。具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

API

- 

调用[CreateRole](products/ram/documents/developer-reference/api-ram-2015-05-01-createrole.md)接口创建RAM角色。

信任策略参数（AssumeRolePolicyDocument）：

{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "ecs.aliyuncs.com" ] } } ], "Version": "1" }

- 

（可选）调用[CreatePolicy](products/ram/documents/developer-reference/api-ram-2015-05-01-createpolicy.md)接口新建权限策略。如果已有可用权限策略，可跳过该步骤。PolicyDocument（权限策略）需按如下设置：

{ "Statement": [ { "Action": [ "oss:Get*", "oss:List*" ], "Effect": "Allow", "Resource": "*" } ], "Version": "1" }

- 

调用[AttachPolicyToRole](products/ram/documents/developer-reference/api-ram-2015-05-01-attachpolicytorole.md)接口为实例RAM角色授权。

### 步骤二：为ECS实例授予RAM角色

将创建好的角色身份赋予指定的ECS实例。

控制台

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击目标ECS实例ID，在实例详情页单击全部操作，选择实例设置>授予/收回RAM角色。

- 

在对话框中，操作类型选择授予，然后选择授予ECS实例的RAM角色，单击确定。

API

调用[AttachInstanceRamRole](products/ecs/documents/api-attachinstanceramrole.md)接口将RAM角色授予ECS实例。

### 步骤三：验证角色授予是否成功

在集成应用前，确认ECS实例已成功获取角色身份。

控制台

- 

登录ECS实例。

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

进入目标实例详情页，单击远程连接，选择通过Workbench远程连接。根据页面提示登录，进入终端页面。

- 

查询实例当前被授予的角色名称。

该命令返回已授予的角色名称列表，用于验证角色是否成功绑定。

curl http://100.100.100.200/latest/meta-data/ram/security-credentials/

- 

成功：若返回授予的角色名称，表示角色授予成功。

- 

失败：

- 

返回404 Not Found：表示实例未被授予任何RAM角色。请返回[步骤二](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)，检查授予操作是否成功。

- 

若命令无响应或连接超时：表示实例无法访问元数据服务。请检查安全组和防火墙是否拦截了IP地址100.100.100.200。

API

调用[DescribeInstanceRamRole](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstanceramrole.md)接口查询ECS实例被授予RAM角色。

### 步骤四：在应用程序中集成

在应用程序中，可通过阿里云Credentials工具配合各语言的云产品SDK自动获取STS临时凭证。STS临时凭证每15分钟自动刷新，Credentials SDK内置刷新逻辑，应用无需处理过期逻辑。

如果使用加固模式，请确保您使用的SDK版本满足以下最低要求。

| 语言 | 包名/工具 | 加固模式最低版本 |
| --- | --- | --- |
| Python | alibabacloud_credentials | 0.3.6 |
| Java | credentials-java | 0.3.10 |
| Go | github.com/aliyun/credentials-go | 1.3.10 |
| Node.js | @alicloud/credentials | 2.3.1 |
| .NET | Aliyun.Credentials | 1.4.2 |
| PHP | alibabacloud/credentials | 1.2.0 |
| 阿里云 CLI | aliyun | 3.0.248 |


Python

- 

安装Credentials工具。

若使用加固模式获取临时身份凭证，alibabacloud_credentials的版本应不低于0.3.6。pip install alibabacloud_credentials

- 

配置ECS的RAM角色作为访问凭证。

fromalibabacloud_credentials.clientimportClientasCredClientfromalibabacloud_credentials.modelsimportConfigasCredConfig credentialsConfig = CredConfig(type='ecs_ram_role',# 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置role_namerole_name='ROLE_NAME',# 选填，默认值：False。True：表示强制使用加固模式。False：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。disable_imds_v1=True) credentialsClient = CredClient(credentialsConfig)﻿

- 

以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。

RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。importoss2fromalibabacloud_credentials.clientimportClientfromalibabacloud_credentials.modelsimportConfigfromoss2importCredentialsProviderfromoss2.credentialsimportCredentials# 1. 定义凭证适配器：将 Credentials 工具获取的 Token 转换为 OSS SDK 可用的格式classCredentialProviderWrapper(CredentialsProvider):def__init__(self, client): self.client = clientdefget_credentials(self):# SDK 自动请求 http://100.100.100.200 获取临时凭证access_key_id = self.client.get_access_key_id() access_key_secret = self.client.get_access_key_secret() security_token = self.client.get_security_token()returnCredentials(access_key_id, access_key_secret, security_token)deflist_objects_using_instance_role(bucket_name, endpoint, role_name):# 2. 配置 ECS 实例角色模式config = Config(type='ecs_ram_role', role_name=role_name ) cred_client = Client(config)# 3. 初始化 OSS Bucketauth = oss2.ProviderAuth(CredentialProviderWrapper(cred_client)) bucket = oss2.Bucket(auth, endpoint, bucket_name)print(f"--- 开始查询 Bucket:{bucket_name}---")try:# 4. 调用 ListObjects 接口fori, objinenumerate(oss2.ObjectIterator(bucket)):print(f"文件 found:{obj.key}")ifi >=9:# 仅展示前10个print("... (更多文件略)")breakprint("--- 查询成功，实例角色权限正常 ---")exceptExceptionase:print(f"查询失败:{e}")if__name__ =="__main__":# 配置role_name ='YOUR_ROLE_NAME'# 替换为你的角色名bucket_name ='YOUR_BUCKET_NAME'# 替换为你的Bucket名endpoint ='YOUR_ENDPOINT'# 替换为对应Endpointlist_objects_using_instance_role(bucket_name, endpoint, role_name)

Java

- 

添加credentials依赖。

若使用加固模式获取临时身份凭证，credentials-java的版本不低于0.3.10。<!-- https://mvnrepository.com/artifact/com.aliyun/credentials-java --> <dependency> <groupId>com.aliyun</groupId> <artifactId>credentials-java</artifactId> <version>0.3.10</version> </dependency>

- 

配置ECS实例RAM角色作为访问凭证。

importcom.aliyun.credentials.Client;importcom.aliyun.credentials.models.Config;publicclassDemoTest{publicstaticvoidmain(String[] args)throwsException {ConfigcredentialConfig=newConfig(); credentialConfig.setType("ecs_ram_role");// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置RoleNamecredentialConfig.setRoleName("ROLENAME");// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。credentialConfig.setDisableIMDSv1(true);ClientcredentialClient=newClient(credentialConfig); } }

- 

以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。

RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。importcom.aliyun.credentials.Client;importcom.aliyun.credentials.models.Config;importcom.aliyun.oss.OSS;importcom.aliyun.oss.OSSClientBuilder;importcom.aliyun.oss.common.auth.Credentials;importcom.aliyun.oss.common.auth.CredentialsProvider;importcom.aliyun.oss.common.auth.DefaultCredentials;importcom.aliyun.oss.model.OSSObjectSummary;importcom.aliyun.oss.model.ObjectListing;// 1. 实现 OSS 的 CredentialsProvider 接口classInstanceRoleCredentialProviderimplementsCredentialsProvider{privatefinalClient credClient;publicInstanceRoleCredentialProvider(String roleName)throwsException {Configconfig=newConfig(); config.setType("ecs_ram_role"); config.setRoleName(roleName);this.credClient =newClient(config); }@OverridepublicvoidsetCredentials(Credentials credentials){}@OverridepublicCredentialsgetCredentials(){// 自动从 ECS 元数据服务获取凭证returnnewDefaultCredentials( credClient.getAccessKeyId(), credClient.getAccessKeySecret(), credClient.getSecurityToken() ); } }publicclassDemo{publicstaticvoidmain(String[] args)throwsException {StringroleName="YOUR_ROLE_NAME";Stringendpoint="YOUR_ENDPOINT";StringbucketName="YOUR_BUCKET_NAME";// 2. 使用自定义 Provider 初始化 OSS 客户端CredentialsProviderprovider=newInstanceRoleCredentialProvider(roleName);OSSossClient=newOSSClientBuilder().build(endpoint, provider); System.out.println("--- 开始查询 ---");try{// 3. 列举文件ObjectListingobjectListing=ossClient.listObjects(bucketName);for(OSSObjectSummary objectSummary : objectListing.getObjectSummaries()) { System.out.println("文件 found: "+ objectSummary.getKey()); } System.out.println("--- 成功 ---"); }catch(Exception e) { e.printStackTrace(); }finally{ ossClient.shutdown(); } } }

## Go

- 

安装Credentials工具。

若使用加固模式获取临时身份凭证，credentials-go的版本不低于1.3.10。

- 

使用go get下载安装。

go get -u github.com/aliyun/credentials-go

- 

使用dep来管理依赖包。

dep ensure -add github.com/aliyun/credentials-go

- 

配置ECS实例RAM角色作为访问凭证。

packagemainimport("fmt""github.com/aliyun/credentials-go/credentials")func_main(args []*string){ credentialsConfig :=new(credentials.Config). SetType("ecs_ram_role").// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置RoleNameSetRoleName("ROLENAME").// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。SetDisableIMDSv1(true) credentialClient, err := credentials.NewCredential(credentialsConfig)iferr !=nil{panic(err) } }

- 

以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。

RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。packagemainimport("fmt""github.com/aliyun/aliyun-oss-go-sdk/oss""github.com/aliyun/credentials-go/credentials")// 1. 定义结构体实现 OSS 的 CredentialsProvider 接口typeCredentialsProviderAdapterstruct{ credClient credentials.Credential }func(c *CredentialsProviderAdapter)GetCredentials() oss.Credentials {// 获取最新 Tokenid, _ := c.credClient.GetAccessKeyId() secret, _ := c.credClient.GetAccessKeySecret() token, _ := c.credClient.GetSecurityToken()returnoss.Credentials{ AccessKeyID: *id, AccessKeySecret: *secret, SecurityToken: *token, } }funcmain(){ roleName :="YOUR_ROLE_NAME"endpoint :="YOUR_ENDPOINT"bucketName :="YOUR_BUCKET_NAME"// 2. 配置 Credentials 客户端 (ECS 模式)config :=new(credentials.Config). SetType("ecs_ram_role"). SetRoleName(roleName) credClient, err := credentials.NewCredential(config)iferr !=nil{panic(err) }// 3. 初始化 OSS Clientprovider := &CredentialsProviderAdapter{credClient: credClient} client, err := oss.New(endpoint,"","", oss.SetCredentialsProvider(provider))iferr !=nil{panic(err) } bucket, err := client.Bucket(bucketName)iferr !=nil{panic(err) }// 4. 查询文件fmt.Println("--- 开始查询 ---") lsRes, err := bucket.ListObjects(oss.MaxKeys(10))iferr !=nil{ fmt.Println("查询失败:", err)return}for_, object :=rangelsRes.Objects { fmt.Println("文件 found:", object.Key) } fmt.Println("--- 成功 ---") }

## Node.js

- 

安装Credentials工具。

若使用加固模式获取临时身份凭证，credentials的版本不低于2.3.1。npm install @alicloud/credentials

- 

配置ECS实例RAM角色作为访问凭证。

constCredential=require('@alicloud/credentials');constcredentialsConfig =newCredential.Config({type:'ecs_ram_role',// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置roleNameroleName:'ROLENAME',// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。disableIMDSv1:true, });constcred =newCredential.default(credentialsConfig);

- 

以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。

RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。constOSS=require('ali-oss');constCredential=require('@alicloud/credentials');asyncfunctionlistObjects() {constroleName ='YOUR_ROLE_NAME';constbucketName ='YOUR_BUCKET_NAME';constregion ='YOUR_REGION';// 注意：OSS SDK 通常只需要 region// 1. 初始化 Credentials (ECS 模式)constcredentialsConfig =newCredential.Config({type:'ecs_ram_role',roleName: roleName });constcredClient =newCredential.default(credentialsConfig);try{// 2. 获取凭证constaccessKeyId =awaitcredClient.getAccessKeyId();constaccessKeySecret =awaitcredClient.getAccessKeySecret();constsecurityToken =awaitcredClient.getSecurityToken();// 3. 初始化 OSS Clientconstclient =newOSS({region: region,accessKeyId: accessKeyId,accessKeySecret: accessKeySecret,stsToken: securityToken,bucket: bucketName,// 如果需要自动刷新，建议使用 refreshSTSToken 机制，此处为简化演示单次获取refreshSTSToken:async() => {return{accessKeyId:awaitcredClient.getAccessKeyId(),accessKeySecret:awaitcredClient.getAccessKeySecret(),stsToken:awaitcredClient.getSecurityToken() } } });// 4. 查询文件console.log("--- 开始查询 ---");constresult =awaitclient.list({'max-keys':10});if(result.objects) { result.objects.forEach(obj=>{console.log(`文件 found:${obj.name}`); }); }else{console.log("Bucket 为空"); }console.log("--- 成功 ---"); }catch(e) {console.error("出错:", e); } }listObjects();

## .NET

- 

安装Credentials工具。

若使用加固模式获取临时身份凭证，credentials的版本不低于1.4.2。dotnet add package Aliyun.Credentials

- 

配置ECS实例RAM角色作为访问凭证。

usingAliyun.Credentials.Models;namespacecredentials_demo{classProgram{staticvoidMain(string[] args){varconfig =newConfig(); { Type ="ecs_ram_role",// 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置RoleNameRoleName ="ROLE_NAME",// 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。DisableIMDSv1 =true} } } }

- 

以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。

RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。usingSystem;usingAliyun.OSS;usingAliyun.Credentials.Models;usingAliyun.Credentials;namespaceEcsRoleDemo{classProgram{staticvoidMain(string[] args){stringroleName ="YOUR_ROLE_NAME";stringendpoint ="YOUR_ENDPOINT";stringbucketName ="YOUR_BUCKET_NAME";// 1. 配置 Credentials (ECS 模式)Config credConfig =newConfig { Type ="ecs_ram_role", RoleName = roleName }; Client credClient =newClient(credConfig);try{// 2. 获取凭证 (C# SDK 内部自动处理异步请求)stringak = credClient.GetAccessKeyId();stringsk = credClient.GetAccessKeySecret();stringtoken = credClient.GetSecurityToken();// 3. 初始化 OSS Client// 注意：在实际长驻服务中，建议封装逻辑以定期重新获取 TokenOssClient ossClient =newOssClient(endpoint, ak, sk, token); Console.WriteLine("--- 开始查询 ---");// 4. 查询文件varlistResult = ossClient.ListObjects(bucketName);foreach(varsummaryinlistResult.ObjectSummaries) { Console.WriteLine("文件 found: "+ summary.Key); } Console.WriteLine("--- 成功 ---"); }catch(Exception ex) { Console.WriteLine("失败: "+ ex.Message); } } } }

## PHP

- 

安装Credentials工具。

若使用加固模式获取临时身份凭证，credentials的版本不低于1.2.0。composer require alibabacloud/credentials

- 

配置ECS实例RAM角色作为访问凭证。

<?php use AlibabaCloud\Credentials\Credential; use AlibabaCloud\Credentials\Credential\Config; $credConfig = new Config([ 'type' => 'ecs_ram_role', // 选填，该ECS角色的角色名称，不填会自动获取，但是建议加上以减少请求次数，可以通过环境变量ALIBABA_CLOUD_ECS_METADATA设置role_name 'roleName' => '<RoleName>', // 选填，默认值：false。true：表示强制使用加固模式。false：系统将首先尝试在加固模式下获取凭据。如果失败，则会切换到普通模式进行尝试（IMDSv1）。 'disableIMDSv1' => true, ]);

- 

以查询指定 OSS Bucket 中的文件列表为例，代码实现如下。

RAM角色需要授权AliyunOSSReadOnlyAccess权限策略。require'vendor/autoload.php';useAlibabaCloud\Credentials\Credential;useOSS\OssClient;useOSS\Core\OssException;$roleName='YOUR_ROLE_NAME';$bucketName='YOUR_BUCKET_NAME';$endpoint='YOUR_ENDPOINT';try{// 1. 配置 Credentials (ECS 模式)$credConfig=newAlibabaCloud\Credentials\Credential\Config(['type'=>'ecs_ram_role','roleName'=>$roleName]);$credClient=newCredential($credConfig);// 2. 获取凭证$ak=$credClient->getAccessKeyId();$sk=$credClient->getAccessKeySecret();$token=$credClient->getSecurityToken();// 3. 初始化 OSS Client$ossClient=newOssClient($ak,$sk,$endpoint,false,$token);echo"--- 开始查询 ---\n";// 4. 查询文件$options=array(OssClient::OSS_MAX_KEYS=>10);$listResult=$ossClient->listObjects($bucketName,$options);$objectList=$listResult->getObjectList();foreach($objectListas$objectInfo) {echo"文件 found: ".$objectInfo->getKey() ."\n"; }echo"--- 成功 ---\n"; }catch(Exception$e) {echo"失败: ".$e->getMessage() ."\n"; }

更多详细信息及调用示例，请参见[方式五：使用](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#f05e47ab948lp)[ECS](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#f05e47ab948lp)[实例](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#f05e47ab948lp)[RAM](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#f05e47ab948lp)[角色](https://help.aliyun.com/zh/sdk/developer-reference/v2-manage-node-js-access-credentials#f05e47ab948lp)。

## 管理与维护

### 收回/更改ECS的实例RAM角色

通过控制台收回/更改

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

找到要操作的ECS实例，选择>实例设置>授予/收回RAM角色。

- 

收回实例RAM角色：操作类型选择收回，单击确定。

- 

更改实例RAM角色：操作类型选择授予，选择所需的实例RAM角色，单击确定完成更改。

通过API收回/更改

- 

收回实例RAM角色：调用[DetachInstanceRamRole](products/ecs/documents/api-detachinstanceramrole.md)接口收回实例RAM角色。

- 

更改实例RAM角色：

- 

调用[DetachInstanceRamRole](products/ecs/documents/api-detachinstanceramrole.md)接口收回实例RAM角色。

- 

调用[AttachInstanceRamRole](products/ecs/documents/api-attachinstanceramrole.md)接口重新为实例授予新的RAM角色。

### 手动获取STS临时凭证（用于脚本或调试）

在Shell脚本等非SDK环境中，可手动调用元数据服务接口获取凭证。

方式一：通过Shell命令获取

元数据服务提供HTTP访问地址获取临时访问凭据。

加固模式

- 

Linux实例

#获取元数据服务器的访问凭证用于鉴权TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:元数据服务器访问凭证有效期"`#获取实例RAM角色的临时凭证curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称

- 

Windows实例（Powershell）

# 获取元数据服务器的访问凭证用于鉴权$token=Invoke-RestMethod-Headers@{"X-aliyun-ecs-metadata-token-ttl-seconds"="元数据服务器的访问凭证有效期"} -MethodPUT-Urihttp://100.100.100.200/latest/api/token# 获取实例RAM角色的临时凭证Invoke-RestMethod-Headers@{"X-aliyun-ecs-metadata-token"=$token} -MethodGET-Urihttp://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称

<元数据服务器的访问凭证有效期>：在获取实例RAM角色的临时授权访问凭证之前，先获取元数据服务器的访问凭证并设置其有效期，以加强数据安全。超过有效期后，需要重新获取凭证，否则无法获取实例RAM角色的临时授权访问凭证。取值范围为1~21600，单位为秒。详细说明，请参见[实例元数据](products/ecs/documents/user-guide/view-instance-metadata.md)。

<实例RAM角色名称>：需替换为具体的实例RAM角色名称。例如EcsRamRole。

若使用云助手执行上述命令时，云助手Agent的最低版本要求如下：

| 平台 | 云助手 Agent 版本号 |
| --- | --- |
| windows | 2.1.3.857 |
| linux | 2.2.3.857 |
| linux arm | 2.4.3.857 |
| freebsd | 2.3.3.857 |


普通模式

- 

Linux实例

curl http://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称

- 

Windows实例（Powershell）

Invoke-RestMethodhttp://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称

<实例RAM角色名称>需替换为实际的实例RAM角色名称。例如EcsRamRoleDocumentTesting。

返回示例如下：

{ "AccessKeyId" : "STS.*******6YSE", "AccessKeySecret" : "aj******jDU", "Expiration" : "2017-11-01T05:20:01Z", "SecurityToken" : "CAISng********", "LastUpdated" : "2023-07-18T14:17:28Z", "Code" : "Success" }

- 

AccessKeyId、AccessKeySecret、SecurityToken共同构成了临时访问令牌。

- 

Expiration：临时授权访问凭证的有效期。

方式二：通过阿里云CLI获取

CLI支持通过实例元数据服务获取临时访问凭证STS Token的逻辑，且支持周期性自动刷新。

若使用加固模式获取临时身份凭证，CLI的版本不低于3.0.248。

- 

安装CLI。

- 

[安装](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)[CLI（Linux）](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)

- 

[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows)

- 

[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos)

- 

配置身份凭据。

aliyun configure --profile EcsProfile --mode EcsRamRole

该命令为交互式命令，需要根据提示输入相应信息。更多信息请参见[配置凭证](https://help.aliyun.com/zh/cli/configure-credentials/#4d37882a4dx9h)。交互过程示例：

Configuring profile 'EcsProfile' in 'EcsRamRole' authenticate mode... Ecs Ram Role []:YOUR_ROLE_NAMEDefault Region Id []:YOUR_REGIONDefault Output Format [json]: json (Only support json) Default Language [zh|en] en: en Saving profile[EcsProfile] ...Done.

- 

调用API。例如，使用CLI查询ECS实例列表。

aliyun ecs DescribeInstances

更多关于CLI命令的说明，请参见[命令结构](https://help.aliyun.com/zh/cli/understanding-command-structure)。

## 常见问题

一台ECS实例可以被授予几个RAM角色？

一台ECS实例在同一时刻最多只能被授予一个RAM角色。可通过收回后再授予的方式切换角色。

如何使用RAM用户给实例授予RAM角色？

为RAM用户授予以下权限，其他操作同[操作步骤](products/ecs/documents/user-guide/attach-an-instance-ram-role-to-an-ecs-instance.md)。

- 

管理RAM角色：需要创建RAM角色并授权。

- 

授予/回收RAM角色：需要进入实例详情页对实例做授予/回收RAM角色的操作。

- 

允许传递角色给云产品：给云服务授予角色需要配合ram:PassRole权限。

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:Describe*", "ecs:List*", "ecs:AttachInstanceRamRole", "ecs:DetachInstanceRAMRole" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "ram:Describe*", "ram:List*", "ram:Get*", "ram:CreateRole", "ram:CreatePolicy", "ram:AttachPolicyToRole" ], "Resource": "*" }, { "Effect": "Allow", "Action": "ram:PassRole", "Resource": "*" } ] }

## 相关文档

- 

当自建应用部署在阿里云ECS服务器上，且需要访问KMS服务时，可以[使用](products/kms/documents/key-management-service/use-cases/access-kms-from-an-ecs-instance-in-a-secure-manner.md)[ECS](products/kms/documents/key-management-service/use-cases/access-kms-from-an-ecs-instance-in-a-secure-manner.md)[实例](products/kms/documents/key-management-service/use-cases/access-kms-from-an-ecs-instance-in-a-secure-manner.md)[RAM](products/kms/documents/key-management-service/use-cases/access-kms-from-an-ecs-instance-in-a-secure-manner.md)[角色安全访问](products/kms/documents/key-management-service/use-cases/access-kms-from-an-ecs-instance-in-a-secure-manner.md)[KMS](products/kms/documents/key-management-service/use-cases/access-kms-from-an-ecs-instance-in-a-secure-manner.md)。

- 

当ECS不需要某些资源访问权限时，可以[为](products/ram/documents/remove-permissions-from-a-ram-role.md)[RAM](products/ram/documents/remove-permissions-from-a-ram-role.md)[角色移除权限](products/ram/documents/remove-permissions-from-a-ram-role.md)。

- 

访问阿里云OpenAPI时，如果在代码中硬编码明文AK，容易因代码仓库权限管理不当造成AK泄露，建议通过非AccessKey硬编码的方式编程，[使用访问凭据访问阿里云](products/ram/documents/use-cases/best-practices-for-programmatic-access-to-alibaba-cloud.md)[OpenAPI](products/ram/documents/use-cases/best-practices-for-programmatic-access-to-alibaba-cloud.md)。

[上一篇：RAM角色](products/ecs/documents/user-guide/use-a-ram-role-to-control-access-to-ecs-instances.md)[下一篇：服务关联角色](products/ecs/documents/user-guide/service-linked-roles.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
