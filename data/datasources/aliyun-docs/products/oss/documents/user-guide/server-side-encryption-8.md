# 服务端加密-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/server-side-encryption-8

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/oss/documents/user-guide.md)

- [开发参考](products/oss/documents/developer-reference.md)

- [产品计费](products/oss/documents/billing.md)

- [常见问题](products/oss/documents/oss-faq.md)

- [动态与公告](products/oss/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 服务端加密

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您在设置了服务端加密的存储空间（Bucket）中上传文件（Object）时，OSS对收到的文件进行加密，再将得到的加密文件持久化保存。当您通过GetObject请求下载文件时，OSS自动将加密文件解密后返回给用户，并在响应头中返回x-oss-server-side-encryption，用于声明该文件进行了服务端加密。

说明

关于响应头中x-oss-server-side-encryption的更多信息，请参见[GetObject](products/oss/documents/developer-reference/getobject.md)。

## 使用场景

OSS通过服务端加密机制，提供静态数据保护。适合于对文件存储有高安全性或者合规性要求的应用场景。例如，深度学习样本文件的存储、在线协作类文档数据的存储。

## 加密方式

OSS针对不同使用场景提供了两种服务端加密方式，您可以根据实际使用场景选用。

- 

- 

- 

- 

| 加密方式 | 功能描述 | 使用场景 | 注意事项 | 费用说明 |
| --- | --- | --- | --- | --- |
| 使用 KMS 托管密钥进行加解密（SSE-KMS） | 使用 KMS 托管的默认 CMK（Customer Master Key）或指定 CMK 进行加解密操作。数据无需通过网络发送到 KMS 服务端进行加解密。 | 因安全合规的要求，需要使用自管理、可指定的密钥。 | 用于加密 Object 的密钥也会被加密，并写入 Object 的元数据中。 KMS 托管密钥的服务端加密方式仅加密 Object 数据，不加密 Object 的元数据。 | 使用 OSS 控制台默认创建的 KMS 密钥 免费。 使用自选的 KMS 密钥，会在 KMS 侧产生费用。费用详情，请参见 [KMS](products/kms/documents/key-management-service/product-overview/kms-billing.md) [计费标准](products/kms/documents/key-management-service/product-overview/kms-billing.md) 。 |
| 使用 OSS 完全托管密钥进行加解密（SSE-OSS） | 使用 OSS 完全托管的密钥加密每个 Object。为了提升安全性，OSS 还会使用主密钥对加密密钥本身进行加密。 | 仅需要基础的加密能力，对密钥无自管理需求。 | 无。 | 免费。 |


## 注意事项

- 

在开启了SSE-KMS加密的Bucket中请求上传、下载、访问文件，需确保对指定的CMK ID拥有使用权限，且请求类型不是匿名请求，否则请求失败，并返回This request is forbidden by kms。

- 

镜像回源至Bucket中的文件默认不加密。

- 

开启或修改Bucket加密方式不影响Bucket中已有文件的加密配置。

- 

同一个Object在同一时间内仅可以使用一种服务端加密方式。

- 

如果配置了存储空间加密，仍然可以在上传或拷贝Object时单独对Object配置加密方式，且以Object配置的加密方式为准。更多信息，请参见[PutObject](products/oss/documents/developer-reference/putobject.md)。

## 权限说明

RAM用户在不同场景中使用服务端加解密的权限说明如下：

说明

关于为RAM用户授权的具体操作，请参见[为](products/oss/documents/common-examples-of-ram-policies.md)[RAM](products/oss/documents/common-examples-of-ram-policies.md)[用户授予自定义的权限策略](products/oss/documents/common-examples-of-ram-policies.md)。

- 

设置Bucket加密方式

- 

具有对目标Bucket的管理权限。

- 

具有PutBucketEncryption和GetBucketEncryption权限。

- 

如果设置加密方式为SSE-KMS，且指定了CMK ID，还需要ListKeys、Listalias、ListAliasesByKeyId以及DescribeKey权限。此场景下的RAM Policy授权策略如下：

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:List*", "kms:DescribeKey" ], "Resource": [ "acs:kms:*:141661496593****:*" //表示允许调用该阿里云账号ID下所有的KMS密钥，如果仅允许使用某个CMK，此处可输入对应的CMK ID。 ] } ] }

- 

上传文件至设置了加密方式的Bucket

- 

具有目标Bucket的上传文件权限。

- 

如果设置加密方式为KMS，并指定了CMK ID，还需要ListKeys、ListAliases、ListAliasesByKeyId、DescribeKey、GenerateDataKey以及Decrypt权限。此场景下的RAM Policy授权策略如下：

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:List*", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ], "Resource": [ "acs:kms:*:141661496593****:*"//表示允许调用该阿里云账号ID下所有的KMS密钥，如果仅允许使用某个CMK，此处可输入对应的CMK ID。 ] } ] }

- 

从设置了加密方式的Bucket中下载文件

- 

具有目标Bucket的文件访问权限。

- 

如果设置加密方式为KMS，并指定了CMK ID，还需要Decrypt权限。此场景下的RAM Policy授权策略如下：

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "kms:Decrypt" ], "Resource": [ "acs:kms:*:141661496593****:*"//表示具有该阿里云账号ID下所有KMS的解密权限。若要针对某个KMS密钥进行解密，此处可输入对应的CMK ID。 ] } ] }

## 操作方式

重要

- 

如果您购买了KMS密钥轮转的增值服务，则服务端加密将支持对KMS密钥进行[密钥轮转](products/kms/documents/key-management-service/user-guide/configure-key-rotation.md)。开启密钥轮转后，新密钥只对新写入的Object生效，密钥轮转前的存量Object的加密密钥保持不变。

- 

如果您通过OSS更新KMS加密密钥，则新密钥仅适用于新写入的文件加密。更新密钥前写入的存量文件仍使用旧密钥加密。因此，更新密钥后不能删除旧密钥，否则会影响存量文件的正常访问。

### 使用OSS控制台

方式一：为Bucket开启服务端加密

创建Bucket时开启服务端加密功能

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击创建 Bucket。

- 

在创建 Bucket面板，按以下说明填写各项参数。

其中，服务端加密方式区域配置参数说明如下：

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 服务端加密方式 | 选择 Object 的加密方式。取值范围如下： 无 ：不启用服务端加密。 OSS 完全托管 ：使用 OSS 托管的密钥进行加密。OSS 会为每个 Object 使用不同的密钥进行加密，作为额外的保护，OSS 会使用主密钥对加密密钥本身进行加密。 KMS ：使用 KMS 默认托管的 CMK 或指定 CMK ID 进行加解密操作。 使用 KMS 加密方式前，需要开通 KMS 服务。具体操作，请参见 [购买专属](products/kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) [KMS](products/kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) [实例](products/kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) 。 |
| 加密算法 | 可选择 AES256 或 SM4 加密算法。 |
| 加密密钥 | 仅当服务端加密方式选择 KMS 时，需要配置该选项。 选择加密密钥。密钥格式为 <alias>(CMK ID) 。其中 <alias> 为用户主密钥的别名，CMK ID 为用户主密钥 ID。取值范围如下： alias/acs/oss(CMK ID) ：选择该选项后，OSS 会使用默认的服务密钥加密 Bucket 内的数据，并在下载 Bucket 内的 Object 时自动进行解密处理。 alias/<cmkname>(CMK ID ) ：选择该选项后，OSS 会使用指定的服务密钥加密 Bucket 内的数据，并将加密 Object 的 CMK ID 记录到 Object 的元数据中，具有解密权限的用户下载 Object 时会自动解密。其中 <cmkname> 为创建密钥时配置的主密钥可选标识。 使用指定的 CMK ID 前，您需要在 KMS 管理控制台创建一个与 Bucket 处于相同地域的普通密钥或外部密钥。具体操作，请参见 [创建密钥](products/kms/documents/key-management-service/support/create-a-cmk-1.md) 。 |


其他参数配置详情，请参见[创建存储空间](products/oss/documents/user-guide/create-a-bucket-4.md)。

- 

单击确定。

为已创建的Bucket开启服务端加密

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击目标Bucket名称。

- 

在左侧导航栏，选择数据安全>服务器端加密。

- 

在服务器端加密页面，单击设置，按以下说明配置各项参数。

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 服务端加密方式 | 选择 Object 的加密方式。取值范围如下： 无 ：不启用服务端加密。 OSS 完全托管 ：使用 OSS 托管的密钥进行加密。OSS 会为每个 Object 使用不同的密钥进行加密，作为额外的保护，OSS 会使用主密钥对加密密钥本身进行加密。 KMS ：使用 KMS 默认托管的 CMK 或指定 CMK ID 进行加解密操作。 使用 KMS 加密方式前，需要开通 KMS 服务。具体操作，请参见 [购买专属](products/kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) [KMS](products/kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) [实例](products/kms/documents/key-management-service/support/purchase-a-dedicated-kms-instance.md) 。 |
| 加密算法 | 可选择 AES256 或 SM4 加密算法。 |
| 加密密钥 | 仅当 服务端加密方式 选择 KMS 时，需要配置该选项。 选择加密密钥。密钥格式为 <alias>(CMK ID) 。其中 <alias> 为用户主密钥的别名，CMK ID 为用户主密钥 ID。取值范围如下： OSS 默认为您创建服务密钥 ：选择该选项后，OSS 会生成一个默认的服务密钥用于该 Bucket 的数据加密，并在下载 Bucket 内的 Object 时自动进行解密处理。OSS 默认创建的服务密钥格式为 alias/acs/oss (CMK ID) ，您可以通过 KMS 管理控制台查看这一服务密钥。 说明 通过 KMS 管理控制台查看这一服务密钥前，您需要向目标 Bucket 上传至少一个文件，确保相应的加密密钥被实际创建并关联到您的 OSS 服务。 alias/<cmkname>(CMK ID ) ：选择该选项后，OSS 会使用指定的服务密钥加密 Bucket 内的数据，并将加密 Object 的 CMK ID 记录到 Object 的元数据中，具有解密权限的用户下载 Object 时会自动解密。其中 <cmkname> 为创建密钥时配置的主密钥可选标识。 使用指定的 CMK ID 前，您需要在 KMS 管理控制台创建一个与 Bucket 处于相同地域的普通密钥或外部密钥。具体操作，请参见 [创建密钥](products/kms/documents/key-management-service/support/create-a-cmk-1.md) 。 |


- 

单击保存。

方式二：上传文件时设置服务端加密

具体操作，请参见[简单上传](products/oss/documents/user-guide/simple-upload.md)。

### 使用阿里云SDK

方式一：为Bucket开启服务端加密

SDK支持为已创建的Bucket开启服务端加密，不支持在创建Bucket时开启服务端加密。以下仅列举常见SDK为已创建的Bucket开启服务端加密的代码示例。关于其他SDK为已创建的Bucket开启服务端加密的代码示例，请参见[SDK](products/oss/documents/developer-reference/overview-21.md)[简介](products/oss/documents/developer-reference/overview-21.md)。

Java

import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; public class Demo { public static void main(String[] args) throws Throwable { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 以设置Bucket加密方式为SM4为例。如果是AES256加密，请替换为SSEAlgorithm.AES256。 ServerSideEncryptionByDefault applyServerSideEncryptionByDefault = new ServerSideEncryptionByDefault(SSEAlgorithm.SM4); ServerSideEncryptionConfiguration sseConfig = new ServerSideEncryptionConfiguration(); sseConfig.setApplyServerSideEncryptionByDefault(applyServerSideEncryptionByDefault); SetBucketEncryptionRequest request = new SetBucketEncryptionRequest(bucketName, sseConfig); ossClient.setBucketEncryption(request); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }

PHP

<?php // 引入自动加载文件 加载依赖库 require_once __DIR__ . '/../vendor/autoload.php'; use AlibabaCloud\Oss\V2 as Oss; // 定义命令行参数描述 $optsdesc = [ "region" => ['help' => 'The region in which the bucket is located', 'required' => True], // 区域是必填项 存储空间所在的区域 "endpoint" => ['help' => 'The domain names that other services can use to access OSS', 'required' => False], // 终端节点是可选项 其他服务可以用来访问OSS的域名 "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项 ]; // 生成长选项列表 用于解析命令行参数 $longopts = \array_map(function ($key) { return "$key:"; // 每个参数后面加冒号 表示需要值 }, array_keys($optsdesc)); // 解析命令行参数 $options = getopt("", $longopts); // 检查必填参数是否缺失 foreach ($optsdesc as $key => $value) { if ($value['required'] === True && empty($options[$key])) { $help = $value['help']; echo "Error: the following arguments are required: --$key, $help"; // 提示用户缺少必填参数 exit(1); } } // 获取命令行参数值 $region = $options["region"]; // 存储空间所在区域 $bucket = $options["bucket"]; // 存储空间名称 // 使用环境变量加载凭证信息 AccessKeyId 和 AccessKeySecret $credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // 使用SDK的默认配置 $cfg = Oss\Config::loadDefault(); // 设置凭证提供者 $cfg->setCredentialsProvider($credentialsProvider); // 设置区域 $cfg->setRegion($region); // 如果提供了终端节点 则设置终端节点 if (isset($options["endpoint"])) { $cfg->setEndpoint($options["endpoint"]); } // 创建OSS客户端实例 $client = new Oss\Client($cfg); // 创建设置存储空间加密配置的请求对象 使用KMS加密算法并指定数据加密方式为SM4 $request = new Oss\Models\PutBucketEncryptionRequest( bucket: $bucket, serverSideEncryptionRule: new Oss\Models\ServerSideEncryptionRule( applyServerSideEncryptionByDefault: new Oss\Models\ApplyServerSideEncryptionByDefault( sseAlgorithm: 'KMS', // 使用KMS加密算法 kmsDataEncryption: 'SM4' // 数据加密方式为SM4 )) ); // 调用putBucketEncryption方法设置存储空间的加密配置 $result = $client->putBucketEncryption($request); // 打印返回结果 printf( 'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码 'request id:' . $result->requestId // 请求的唯一标识 );

Node.js

const OSS = require("ali-oss"); const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: 'yourregion', // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, authorizationV4: true, // yourbucketname填写存储空间名称。 bucket: 'yourbucketname' }); async function putBucketEncryption() { try { // 配置Bucket加密方式。 const result = await client.putBucketEncryption("bucket-name", { SSEAlgorithm: "AES256", // 此处以设置AES256加密为例。若使用KMS加密，需添加KMSMasterKeyID属性。 // KMSMasterKeyID：“yourKMSMasterKeyId”,设置KMS密钥ID，加密方式为KMS可设置此项。当SSEAlgorithm值为KMS，且使用指定的密钥加密时，需输入密钥ID。其他情况下，必须为空。 }); console.log(result); } catch (e) { console.log(e); } } putBucketEncryption();

C#

using Aliyun.OSS; using Aliyun.OSS.Common; // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "yourEndpoint"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称，例如examplebucket。 var bucketName = "examplebucket"; // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。 const string region = "cn-hangzhou"; // 创建ClientConfiguration实例，按照您的需要修改默认参数。 var conf = new ClientConfiguration(); // 设置v4签名。 conf.SignatureVersion = SignatureVersion.V4; // 创建OssClient实例。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf); client.SetRegion(region); try { // 配置Bucket加密。 var request = new SetBucketEncryptionRequest(bucketName, "KMS", null); client.SetBucketEncryption(request); Console.WriteLine("Set bucket:{0} Encryption succeeded ", bucketName); } catch (OssException ex) { Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}", ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId); } catch (Exception ex) { Console.WriteLine("Failed with error info: {0}", ex.Message); }

Go

package main import ( "log" "github.com/aliyun/aliyun-oss-go-sdk/oss" ) func main() { // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 provider, err := oss.NewEnvironmentVariableCredentialsProvider() if err != nil { log.Fatalf("Error creating credentials provider: %v", err) } // 创建OSSClient实例。 // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。 // yourRegion填写Bucket所在地域，以华东1（杭州）为例，填写为cn-hangzhou。其它Region请按实际情况填写。 clientOptions := []oss.ClientOption{oss.SetCredentialsProvider(&provider)} clientOptions = append(clientOptions, oss.Region("yourRegion")) // 设置签名版本 clientOptions = append(clientOptions, oss.AuthVersion(oss.AuthV4)) client, err := oss.New("yourEndpoint", "", "", clientOptions...) if err != nil { log.Fatalf("Error creating OSS client: %v", err) } // 初始化一个加密规则，加密方式以AES256为例。 config := oss.ServerEncryptionRule{ SSEDefault: oss.SSEDefaultRule{ SSEAlgorithm: "AES256", }, } // 设置Bucket的加密规则。 err = client.SetBucketEncryption("yourBucketName", config) if err != nil { log.Fatalf("Error setting bucket encryption: %v", err) } log.Println("Bucket encryption set successfully") }

C++

#include <alibabacloud/oss/OssClient.h> using namespace AlibabaCloud::OSS; int main(void) { /* 初始化OSS账号信息。*/ /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/ std::string Region = "yourRegion"; /* 填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /* 初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; conf.signatureVersion = SignatureVersionType::V4; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); client.SetRegion(Region); SetBucketEncryptionRequest setrequest(BucketName); setrequest.setSSEAlgorithm(SSEAlgorithm::KMS); /* 设置KMS服务端加密。*/ auto outcome = client.SetBucketEncryption(setrequest); if (!outcome.isSuccess()) { /* 异常处理。*/ std::cout << "SetBucketEncryption fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /* 释放网络等资源。*/ ShutdownSdk(); return 0; }

方式二：上传文件时设置服务端加密

以下仅列举常见SDK上传文件时设置服务端加密的代码示例。关于其他SDK上传文件时设置服务端加密的代码示例，请参见[SDK](products/oss/documents/developer-reference/overview-21.md)[简介](products/oss/documents/developer-reference/overview-21.md)。

Javaimport com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.internal.OSSHeaders; import com.aliyun.oss.model.PutObjectRequest; import com.aliyun.oss.model.PutObjectResult; import com.aliyun.oss.model.ObjectMetadata; import java.io.File; public class Put { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Endpoint对应的Region信息，例如cn-hangzhou。 String region = "cn-hangzhou"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。 String objectName = "exampledir/exampleobject.txt"; // 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。 // 如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。 String filePath= "D:\\localpath\\examplefile.txt"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); // 显式声明使用 V4 签名算法 clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 创建ObjectMetadata对象，并设置服务端加密方式为AES256。 ObjectMetadata metadata = new ObjectMetadata(); metadata.setHeader(OSSHeaders.OSS_SERVER_SIDE_ENCRYPTION, "AES256"); // 创建PutObjectRequest对象。 PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, objectName, new File(filePath)); putObjectRequest.setMetadata(metadata); // 上传文件。 PutObjectResult result = ossClient.putObject(putObjectRequest); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }

PHP<?php if (is_file(__DIR__ . '/../autoload.php')) { require_once __DIR__ . '/../autoload.php'; } if (is_file(__DIR__ . '/../vendor/autoload.php')) { require_once __DIR__ . '/../vendor/autoload.php'; } use OSS\Credentials\EnvironmentVariableCredentialsProvider; use OSS\OssClient; use OSS\Core\OssException; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 $provider = new EnvironmentVariableCredentialsProvider(); // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 $endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Bucket名称，例如examplebucket。 $bucket= "examplebucket"; // 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。 $object = "exampledir/exampleobject.txt"; // 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。 $filePath = "D:\\localpath\\examplefile.txt"; try{ $config = array( "provider" => $provider, "endpoint" => $endpoint, ); $ossClient = new OssClient($config); $options[OssClient::OSS_HEADERS] = array( // 设置服务端加密方式为AES256。 "x-oss-server-side-encryption"=>"AES256", ); // 调用uploadFile方法上传文件，并传入UploadOptions对象。 $ossClient->uploadFile($bucket, $object, $filePath, $options); } catch(OssException $e) { printf(__FUNCTION__ . ": FAILED\n"); printf($e->getMessage() . "\n"); return; } print(__FUNCTION__ . "OK" . "\n");

Node.jsconst OSS = require("ali-oss"); const path = require("path"); const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: "oss-cn-hangzhou", // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, // 填写Bucket名称。 bucket: "examplebucket", }); const headers = { // 设置服务端加密方式为AES256。 "x-oss-server-side-encryption": "AES256", }; async function put() { try {。 const result = await client.put( // 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。 "exampledir/exampleobject.txt", // 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。 path.normalize("D:\\examplefile.jpg"), { headers } ); console.log(result); } catch (e) { console.log(e); } } put();

Python# -*- coding: utf-8 -*- import oss2 import os from oss2.credentials import EnvironmentVariableCredentialsProvider # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider()) # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 endpoint = 'https://oss-cn-hangzhou.aliyuncs.com' # 填写Bucket名称。 bucket_name = 'examplebucket0703' bucket = oss2.Bucket(auth, endpoint, bucket_name) # 必须以二进制的方式打开文件。 # 填写本地文件的完整路径。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。 local_file_path = 'D:\\examplefile.jpg' with open(local_file_path, 'rb') as fileobj: # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。 fileobj.seek(1000, os.SEEK_SET) # Tell方法用于返回当前位置。 current = fileobj.tell() # 设置服务端加密方式为AES256。 headers = { 'x-oss-server-side-encryption': 'AES256', } # 填写Object完整路径。Object完整路径中不能包含Bucket名称。 object_key = 'exampledir/object1.jpg' bucket.put_object(object_key, fileobj, headers=headers)

Gopackage main import ( "fmt" "github.com/aliyun/aliyun-oss-go-sdk/oss" "os" ) func main() { // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 provider, err := oss.NewEnvironmentVariableCredentialsProvider() if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 创建OSSClient实例。 // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。 client, err := oss.New("https://oss-cn-hangzhou.aliyuncs.com", "", "", oss.SetCredentialsProvider(&provider)) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 填写存储空间名称，例如examplebucket。 bucket, err := client.Bucket("examplebucket") if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。 // 填写本地文件的完整路径，例如D:\\localpath\\examplefile.txt。如果未指定本地路径，则默认从示例程序所属项目对应本地路径中上传文件。 // 设置服务端加密方式为AES256。 err = bucket.PutObjectFromFile("D:\\localpath\\examplefile.txt", "D:\\examplefile.jpg", oss.ServerSideEncryption("AES256")) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } }

### 使用命令行工具ossutil

方式一：为Bucket开启服务端加密

您可以使用命令行工具ossutil来为Bucket开启服务端加密，ossutil的安装请参见[安装](products/oss/documents/install-ossutil2.md)[ossutil](products/oss/documents/install-ossutil2.md)。

以下示例展示了如何为已创建的存储空间examplebucket设置服务端加密方式为AES256。

ossutil api put-bucket-encryption --bucket examplebucket --server-side-encryption-rule "{\"ApplyServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"AES256\"}}"

如果您想了解该命令的更多信息，请参见[put-bucket-encryption](products/oss/documents/developer-reference/put-bucket-encryption.md)。

方式二：上传文件时设置服务端加密

ossutil支持在上传文件时指定文件的服务端加密方式，ossutil的安装请参见[安装](products/oss/documents/install-ossutil2.md)[ossutil](products/oss/documents/install-ossutil2.md)。以下示例展示了如何在上传文件时设定服务端加密方式为AES256。

ossutil cp examplefile.txt oss://examplebucket --metadata=x-oss-server-side-encryption:AES256

如果您想了解该命令的更多信息，请参见[cp（上传文件）](products/oss/documents/developer-reference/cp-upload-file.md)。

## 使用KMS托管密钥进行加解密

使用KMS托管的用户主密钥CMK生成加密密钥加密数据，通过信封加密机制，可进一步防止未经授权的数据访问。借助KMS，您可以专注于数据加解密、电子签名验签等业务功能，无需花费大量成本来保障密钥的保密性、完整性和可用性。

SSE-KMS加密方式的逻辑示意图如下。

使用SSE-KMS加密方式时，可使用如下密钥：

- 

使用OSS默认托管的KMS密钥

OSS使用默认托管的KMS CMK生成不同的密钥来加密不同的Object，并且在Object被下载时自动解密。首次使用时，OSS会在KMS平台创建一个OSS托管的CMK。

配置方式如下：

- 

配置Bucket加密方式

配置Bucket加密方式为KMS，指定加密算法为AES256或SM4，但不指定具体的CMK ID。此后，所有上传至此Bucket的Object都会被加密。

- 

为目标Object配置加密方式

上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为KMS。此时，OSS将使用默认托管的KMS CMK，并通过AES256加密算法加密Object。如需修改加密算法为SM4，您还需增加x-oss-server-side-data-encryption参数，并设置参数值为SM4。更多信息，请参见[PutObject](products/oss/documents/developer-reference/putobject.md)。

- 

使用自带密钥BYOK（Bring Your Own Key）

您在KMS控制台使用BYOK材料生成CMK后，OSS可使用指定的KMS CMK生成不同的密钥来加密不同的Object，并将加密Object的CMK ID记录到Object的元数据中，只有具有解密权限的用户下载Object时才会自动解密。

BYOK材料来源有两种：

- 

由阿里云提供的BYOK材料：在KMS平台创建密钥时，选择密钥材料来源为阿里云KMS。

- 

使用用户自有的BYOK材料：在KMS平台创建密钥时，选择密钥材料来源为外部，并按照要求导入外部密钥材料。关于导入外部密钥的具体操作，请参见[导入密钥材料](products/kms/documents/key-management-service/support/import-key-material.md)。

配置方式如下：

- 

配置Bucket加密方式

配置Bucket加密方式为KMS，指定加密算法为AES256或SM4，并指定具体的CMK ID。此后，所有上传至此Bucket的Object都会被加密。

- 

为目标Object配置加密方式

上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为KMS；携带x-oss-server-side-encryption-key-id参数，并设置参数值为指定CMK ID。此时，OSS将使用指定的KMS CMK，并通过AES256加密算法加密Object。如需修改加密算法，您还需增加x-oss-server-side-data-encryption参数，并设置参数值为SM4。更多信息，请参见[PutObject](products/oss/documents/developer-reference/putobject.md)。

## 使用OSS完全托管密钥进行加解密

OSS负责生成和管理数据加密密钥，并采用高强度、多因素的安全措施进行保护。数据加密的算法采用行业标准的AES256（即256位高级加密标准）和国密SM4算法。

配置方式如下：

- 

配置Bucket加密方式

配置Bucket加密方式为OSS完全托管，并指定加密算法为AES256或SM4。此后，所有上传至此Bucket的Object都会默认被加密。

- 

为目标Object配置加密方式

上传Object或修改Object的meta信息时，在请求中携带x-oss-server-side-encryption参数，并设置参数值为AES256或SM4。此时，OSS将使用OSS完全托管的密钥加密Object。更多信息，请参见[PutObject](products/oss/documents/developer-reference/putobject.md)。

## 相关API

以上操作方式底层基于API实现，如果您的程序自定义要求较高，您可以直接发起REST API请求。直接发起REST API请求需要手动编写代码计算签名。更多信息，请参见[PutBucketEncryption](products/oss/documents/developer-reference/putbucketencryption.md)。

## 常见问题

配置Bucket加密方式后，OSS会对历史文件进行加密吗？

OSS只对服务端加密配置生效后上传的Object进行加密，不会加密历史文件。如果您需要加密历史文件，可通过CopyObject覆写历史文件。

[上一篇：客户端加密](products/oss/documents/user-guide/client-side-encryption.md)[下一篇：设置TLS版本](products/oss/documents/user-guide/set-tls-version.md)

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
