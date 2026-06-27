# 对象恢复至任意时刻历史版本-版本控制-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/overview-78

# 开启版本控制实现数据恢复和版本管理
版本控制是针对存储空间（Bucket）级别的数据保护功能。开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或删除对象（Object）后，能够将存储在Bucket中的Object恢复至任意时刻的历史版本。
## 使用场景
建议您在以下场景中使用版本控制，为您的数据安全提供更好的保障。
数据误删除
当前OSS不提供回收站功能。您删除OSS数据后想要找回时，可使用版本控制功能，恢复已删除的数据。
文件被覆盖
对于网盘、在线协作类产品，文件会被频繁修改，针对文件的编辑会产生大量的临时版本。您可以使用版本控制功能找回某个时间点的版本。
## 注意事项
费用说明
版本控制功能本身不收取任何费用，但对当前版本和所有历史版本的文件都会收取存储费用。为避免不必要的存储费用，请通过生命周期及时删除不需要的历史版本文件。具体操作，请参见[生命周期](overview-54.md)。此外，若您对历史版本文件进行下载或恢复等操作，还会产生相应的请求费用、流量费用等。计费详情，请参见[计量项与计费项](../billing-overview.md)。
权限说明
只有Bucket的拥有者及授予了PutBucketVersioning权限的RAM用户才能配置版本控制。
功能互斥
如果Bucket版本控制状态为开启或暂停：
禁止覆盖规则将不生效。更多信息，请参见[禁止文件覆盖写](prevent-file-overwrite.md)。
上传文件时附加的覆盖同名文件请求头x-oss-forbid-overwrite将不生效。更多信息，请参见[PutObject](../developer-reference/putobject.md)。
版本控制与OSS-HDFS服务
同一Bucket禁止同时开通OSS-HDFS服务和版本控制，否则可能导致OSS-HDFS服务异常。为确保服务稳定性，请尽快暂停版本控制，并配置生命周期规则清理删除标记。
## 版本控制状态
Bucket包含三种版本控制状态，分别为未开启、开启或者暂停。
默认情况下，Bucket版本控制状态为“未开启”。如果Bucket处于“开启”版本状态，将无法返回至“未开启”状态。但是，您可以暂停Bucket的版本控制状态。
当Bucket版本控制处于“开启”状态时，OSS将为新上传的Object生成全局唯一的随机字符串版本ID。关于启用版本控制状态下Object的具体操作，请参见[开启版本控制下](manage-objects-in-a-versioning-enabled-bucket.md)[Object](manage-objects-in-a-versioning-enabled-bucket.md)[的操作](manage-objects-in-a-versioning-enabled-bucket.md)。
当Bucket版本控制处于“暂停”状态时，OSS将为新上传的Object生成特殊字符串为“null”的版本ID。关于暂停版本控制状态下Object的具体操作，请参见[暂停版本控制下](manage-objects-in-a-versioning-suspended-bucket.md)[Object](manage-objects-in-a-versioning-suspended-bucket.md)[的操作](manage-objects-in-a-versioning-suspended-bucket.md)。
说明
当Bucket版本控制处于“开启”状态时，由于Object的每个版本都被保存下来，每个版本都会占用存储空间，OSS会对Object的所有版本收取存储费用。建议结合您的使用场景通过生命周期规则，将当前版本或历史版本Object转换为低频访问或归档存储类型以及删除不再需要的历史版本，以降低您的存储费用，更多信息请参见[使用最后一次修改时间的生命周期规则结合版本控制降低存储成本](configure-lifecycle-rules-to-manage-object-versions.md)。
## 数据保护
以下表格详细阐述了不同版本控制状态下，OSS对覆盖和删除Object的处理逻辑，帮助您了解版本控制状态下的数据保护机制。
| 版本控制状态 | 覆盖 Object | 删除 Object |
| --- | --- | --- |
| 未开启 | 已有 Object 被直接覆盖，且无法恢复，只能获取最新版本 Object。 | 直接删除，无法再获取此 Object。 |
| 开启 | 为此 Object 添加新的版本 ID，历史版本不受影响。 | 为此 Object 添加删除标记（Delete Marker），删除标记将携带一个全局唯一的版本 ID，历史版本不受影响。 |
| 暂停 | 为此 Object 产生版本 ID 为“null”的新版本。 如果历史版本中已存在版本号为“null”的 Object 或删除标记，则将会被新的“null”版本 Object 覆盖，其他非“null”版本的 Object 或删除标记不受影响。 | 为此 Object 产生版本 ID 为“null”的删除标记。 如果历史版本中已存在版本号为“null”的 Object 或删除标记，则将会被新的删除标记覆盖，其他非“null”版本的 Object 或删除标记不受影响。 |
以下以图示的方法说明在Bucket版本控制状态处于“开启”和“暂停”时，上传同名Object或删除Object时OSS的处理行为。图示中的版本号均以简短版本号代替。
开启版本控制下的Object覆盖操作
在开启版本控制的Bucket中连续执行上传Object操作，Object虽然被多次覆盖，但每次覆盖操作均会产生一个独立的版本ID。
开启版本控制下的Object删除操作
在开启版本控制下的Bucket中删除Object时，历史版本Object不会被真正删除，而是产生一个删除标记来标识Object的当前版本是删除状态。如果再重复上传同名Object，将产生新的版本ID。
暂停版本控制下的Object覆盖操作
在暂停版本控制状态Bucket中上传Object时，历史版本数据继续保留，新上传的Object版本号为“null”。如果再重复上传同名Object，将产生新的“null”版本，并自动把前一次的“null”版本覆盖。
暂停版本控制下的Object删除操作
在暂停版本控制下的Bucket中删除Object时，历史版本Object不会被真正删除，而是产生一个删除标记来标识Object的当前版本是删除状态。
从上述信息得知，当您的Bucket处于版本控制状态时，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或者删除Object后，能够将Bucket中存储的Object恢复至任意时刻的历史版本。
## 开启版本控制
使用OSS控制台
开启版本控制后，OSS会为Bucket中所有Object的每个版本指定唯一的versionId。
新建Bucket时开启版本控制。
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击创建 Bucket。
在创建 Bucket页面配置各项参数。
其中，在版本控制区域单击版本控制开关按钮切换到已开通状态，默认状态为未开通。其他参数的配置详情，请参见[创建存储空间](../manage-buckets-create-buckets.md)。
单击确定。
对已创建的Bucket开启版本控制。
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏，选择数据安全>版本控制。
在版本控制页面，单击开启。
在弹出的对话框，单击确定。
开启版本控制后，您可以在文件列表页面单击历史版本右侧的显示，查看所有版本的文件。如果仅需查看文件的当前版本，请单击历史版本右侧的隐藏。隐藏历史版本并不能提升列举文件的性能，如果列举文件时页面响应过慢，请参见[响应速度下降](faq-4.md)排查并解决。
使用阿里云SDK
以下仅列举常见SDK的开启版本控制的代码示例。关于其他SDK的开启版本控制的代码示例，请参见[SDK](../developer-reference/overview-21.md)[简介](../developer-reference/overview-21.md)。
Java
import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Endpoint对应的Region信息，例如cn-hangzhou。 String region = "cn-hangzhou"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); // 显式声明使用 V4 签名算法 clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 开启版本控制。 BucketVersioningConfiguration configuration = new BucketVersioningConfiguration(); configuration.setStatus(BucketVersioningConfiguration.ENABLED); SetBucketVersioningRequest request = new SetBucketVersioningRequest(bucketName, configuration); ossClient.setBucketVersioning(request); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }
PHP
<?php if (is_file(__DIR__ . '/../autoload.php')) { require_once __DIR__ . '/../autoload.php'; } if (is_file(__DIR__ . '/../vendor/autoload.php')) { require_once __DIR__ . '/../vendor/autoload.php'; } use OSS\OssClient; use OSS\Core\OssException; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 $accessKeyId = getenv("OSS_ACCESS_KEY_ID"); $accessKeySecret = getenv("OSS_ACCESS_KEY_SECRET"); // Endpoint以杭州为例，其它Region请按实际情况填写。 $endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; $bucket= "yourBucketName"; $ossClient = new OssClient($accessKeyId, $accessKeySecret, $endpoint); try { // 开启版本控制。 $ossClient->putBucketVersioning($bucket, "Enabled"); } catch (OssException $e) { printf(__FUNCTION__ . ": FAILED\n"); printf($e->getMessage() . "\n"); return; } print(__FUNCTION__ . ": OK" . "\n");
Node.js
const OSS = require("ali-oss"); const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: "oss-cn-hangzhou", // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, // 填写存储空间名称，例如examplebucket。 bucket: "examplebucket", }); async function putBucketVersioning() { // 开启版本控制。 const status = "Enabled"; const result = await client.putBucketVersioning("examplebucket", status); console.log(result); } putBucketVersioning();
Python
# -*- coding: utf-8 -*- import oss2 from oss2.credentials import EnvironmentVariableCredentialsProvider from oss2.models import BucketVersioningConfig # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider()) # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 # yourBucketName填写存储空间名称。 bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'yourBucketName') # 创建bucket版本控制配置。 config = BucketVersioningConfig() # 开启版本控制。 config.status = oss2.BUCKET_VERSIONING_ENABLE result = bucket.put_bucket_versioning(config) # 查看http返回码。 print('http response code:', result.status)
C#
using Aliyun.OSS; using Aliyun.OSS.Common; // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "yourEndpoint"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称，例如examplebucket。 var bucketName = "examplebucket"; // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。 const string region = "cn-hangzhou"; // 创建ClientConfiguration实例，按照您的需要修改默认参数。 var conf = new ClientConfiguration(); // 设置v4签名。 conf.SignatureVersion = SignatureVersion.V4; // 创建OssClient实例。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf); client.SetRegion(region); try { // 设置存储空间版本控制状态为Enabled。 client.SetBucketVersioning(new SetBucketVersioningRequest(bucketName, VersioningStatus.Enabled)); Console.WriteLine("Create bucket Version succeeded"); } catch (Exception ex) { Console.WriteLine("Create bucket Version failed. {0}", ex.Message); }
Go
package main import ( "fmt" "os" "github.com/aliyun/aliyun-oss-go-sdk/oss" ) func main() { /// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 provider, err := oss.NewEnvironmentVariableCredentialsProvider() if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 创建OSSClient实例。 // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。 client, err := oss.New("yourEndpoint", "", "", oss.SetCredentialsProvider(&provider)) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 创建一个存储空间。 // yourBucketName填写存储空间名称。 err = client.CreateBucket("yourBucketName") if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 此处以设置存储空间版本状态为Enabled为例。 config := oss.VersioningConfig{Status: "Enabled"} err = client.SetBucketVersioning("yourBucketName", config) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } }
C++
#include <alibabacloud/oss/OssClient.h> using namespace AlibabaCloud::OSS; int main(void) { /* 初始化OSS账号信息。*/ /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; /* 填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /* 初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); /* 创建Bucket版本配置，状态设置为Enabled。*/ SetBucketVersioningRequest setrequest(BucketName, VersioningStatus::Enabled); auto outcome = client.SetBucketVersioning(setrequest); if (!outcome.isSuccess()) { /* 异常处理。*/ std::cout << "SetBucketVersioning fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /* 释放网络等资源。*/ ShutdownSdk(); return 0; }
使用命令行工具ossutil
您可以使用命令行工具ossutil来设置指定存储空间的版本控制状态，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于启用指定存储空间的版本控制功能。
ossutil api put-bucket-versioning --bucket examplebucket --versioning-configuration "{\"Status\":\"Enabled\"}"
关于该命令的更多信息，请参见[put-bucket-versioning](../developer-reference/put-bucket-versioning.md)。
## 暂停版本控制
如果Bucket已开启保留策略，版本控制状态从"开启"转为"暂停"将被禁止。但从"暂停"转为"开启"是允许的。
使用OSS控制台
开启版本控制后，您还可以随时暂停版本控制以停止在Bucket中继续累积同一Object的新版本。暂停版本控制后，OSS将为新生成的Object添加versionId为null的版本，已有的历史版本Object将继续保留。
暂停Bucket版本控制的操作步骤如下：
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏，选择数据安全>版本控制。
在版本控制页面，单击暂停。
在弹出的对话框，单击确定。
使用阿里云SDK
以下仅列举常见SDK的开启版本控制的代码示例。关于其他SDK的开启版本控制的代码示例，请参见[SDK](../developer-reference/overview-21.md)[简介](../developer-reference/overview-21.md)。
Java
import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Endpoint对应的Region信息，例如cn-hangzhou。 String region = "cn-hangzhou"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); // 显式声明使用 V4 签名算法 clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 暂停版本控制。 BucketVersioningConfiguration configuration = new BucketVersioningConfiguration(); configuration.setStatus(BucketVersioningConfiguration.SUSPENDED); SetBucketVersioningRequest request = new SetBucketVersioningRequest(bucketName, configuration); ossClient.setBucketVersioning(request); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }
PHP
<?php if (is_file(__DIR__ . '/../autoload.php')) { require_once __DIR__ . '/../autoload.php'; } if (is_file(__DIR__ . '/../vendor/autoload.php')) { require_once __DIR__ . '/../vendor/autoload.php'; } use OSS\OssClient; use OSS\Core\OssException; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 $accessKeyId = getenv("OSS_ACCESS_KEY_ID"); $accessKeySecret = getenv("OSS_ACCESS_KEY_SECRET"); // Endpoint以杭州为例，其它Region请按实际情况填写。 $endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; $bucket= "yourBucketName"; $ossClient = new OssClient($accessKeyId, $accessKeySecret, $endpoint); try { // 暂停版本控制。 $ossClient->putBucketVersioning($bucket, "Suspended"); } catch (OssException $e) { printf(__FUNCTION__ . ": FAILED\n"); printf($e->getMessage() . "\n"); return; } print(__FUNCTION__ . ": OK" . "\n");
Node.js
const OSS = require("ali-oss"); const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: "oss-cn-hangzhou", // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, // 填写存储空间名称，例如examplebucket。 bucket: "examplebucket", }); async function putBucketVersioning() { // 暂停版本控制。 const status = "Suspended"; const result = await client.putBucketVersioning("examplebucket", status); console.log(result); } putBucketVersioning();
Python
# -*- coding: utf-8 -*- import oss2 from oss2.credentials import EnvironmentVariableCredentialsProvider from oss2.models import BucketVersioningConfig # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 auth = oss2.ProviderAuth(EnvironmentVariableCredentialsProvider()) # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 # yourBucketName填写存储空间名称。 bucket = oss2.Bucket(auth, 'https://oss-cn-hangzhou.aliyuncs.com', 'yourBucketName') # 创建bucket版本控制配置。 config = BucketVersioningConfig() # 暂停版本控制。 config.status = oss2.BUCKET_VERSIONING_SUSPEND result = bucket.put_bucket_versioning(config) # 查看http返回码。 print('http response code:', result.status)
C#
using Aliyun.OSS; // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "yourEndpoint"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称，例如examplebucket。 var bucketName = "examplebucket"; // 初始化OSSClient。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret); try { // 设置存储空间版本控制状态为Suspended。 client.SetBucketVersioning(new SetBucketVersioningRequest(bucketName, VersioningStatus.Suspended)); Console.WriteLine("Create bucket Version succeeded"); } catch (Exception ex) { Console.WriteLine("Create bucket Version failed. {0}", ex.Message); }
Go
package main import ( "fmt" "os" "github.com/aliyun/aliyun-oss-go-sdk/oss" ) func main() { /// 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 provider, err := oss.NewEnvironmentVariableCredentialsProvider() if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 创建OSSClient实例。 // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。 client, err := oss.New("yourEndpoint", "", "", oss.SetCredentialsProvider(&provider)) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 创建一个存储空间。 // yourBucketName填写存储空间名称。 err = client.CreateBucket("yourBucketName") if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 暂停版本控制。 config := oss.VersioningConfig{Status: "Suspended"} err = client.SetBucketVersioning("yourBucketName", config) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } }
C++
#include <alibabacloud/oss/OssClient.h> using namespace AlibabaCloud::OSS; int main(void) { /* 初始化OSS账号信息。*/ /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; /* 填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /* 初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); /* 创建Bucket版本配置，状态设置为Suspended。*/ SetBucketVersioningRequest setrequest(BucketName, VersioningStatus::Suspended); auto outcome = client.SetBucketVersioning(setrequest); if (!outcome.isSuccess()) { /* 异常处理。*/ std::cout << "SetBucketVersioning fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /* 释放网络等资源。*/ ShutdownSdk(); return 0; }
使用命令行工具ossutil
您可以使用命令行工具ossutil来设置指定存储空间的版本控制状态，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于暂停指定存储空间的版本控制功能。
ossutil api put-bucket-versioning --bucket examplebucket --versioning-configuration "{\"Status\":\"Suspended\"}"
关于该命令的更多信息，请参见[put-bucket-versioning](../developer-reference/put-bucket-versioning.md)。
## 查看版本
您可以使用命令行工具ossutil来查看某个Object的所有版本，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于列举存储空间examplebucket中所有Object的版本信息。
ossutil api list-object-versions --bucket examplebucket
关于该命令的更多信息，请参见[list-object-versions](../developer-reference/list-object-versions.md)。
## 恢复版本
使用OSS控制台
在开启版本控制的Bucket中删除Object时，历史版本Object不会被真正删除，而是产生一个删除标记来标识Object的当前版本是删除状态。此时您可以在控制台恢复版本。
单击Bucket 列表，然后单击目标Bucket名称。
选择文件管理>文件列表。
单击历史版本右侧的显示。
选中待恢复文件，然后单击页面下方的恢复。
在弹出的对话框，单击确定。
使用命令行工具ossutil
您可以使用命令行工具ossutil来恢复已删除文件的历史版本，ossutil的安装请参见[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以下命令用于对存储空间examplebucket里的example.txt对象恢复到版本号为123的状态。
ossutil revert oss://examplebucket/example.txt 123
关于该命令的更多信息，请参见[revert（恢复版本）](../developer-reference/revert-recovery-version.md)。
## 相关API
以上操作方式底层基于API实现，如果您的程序自定义要求较高，您可以直接发起REST API请求。直接发起REST API请求需要手动编写代码计算签名。更多信息，请参见[PutBucketVersioning](../developer-reference/putbucketversioning.md)。
## 与保留策略协同工作
在为Veeam等备份系统提供数据版本保护、追溯电路设计图等资产的修改记录，或满足金融行业合规归档要求的场景中，通常需要允许数据持续更新，同时确保其所有历史版本都不可篡改或删除。为实现这一目标，可为 Bucket同时开启版本控制并创建保留策略。版本控制确保对象在被覆盖或删除时，其旧版本会作为历史版本保留，而非物理删除。而保留策略则为Bucket内所有对象版本设定保护期，在此期间内，任何版本都无法被删除或修改。
版本控制功能与保留策略功能可同时配置，协同工作遵循以下原则：
功能开启顺序：版本控制与保留策略功能的开启顺序无约束要求，可根据业务需求灵活配置。
允许的配置组合：
保留策略 + 版本控制Disable
保留策略 + 版本控制Enable
限制规则：
版本控制处于Suspend状态的Bucket，无法开启保留策略
已开启保留策略后，版本控制状态存在以下限制：
不允许从Enable转为Suspend
不允许从Disable转为Suspend
对象版本保护机制：
保留策略对Object的所有版本提供保护，在保护期内不允许删除或篡改任何版本。
允许上传同名Object产生新版本，但新版本同样受保留策略保护。
保留策略不作用于删除标记，删除标记的清理不受保留策略限制。
数据复制协同：
源Bucket与目标Bucket均支持独立的版本控制和保留策略配置。
复制过程中的版本信息正常传输，目标Bucket根据自身配置进行版本管理。
目标Bucket上文件在保留周期内，删除报错；不在保留周期内，删除成功。
## 后续参考
[开启版本控制下](manage-objects-in-a-versioning-enabled-bucket.md)[Object](manage-objects-in-a-versioning-enabled-bucket.md)[的操作](manage-objects-in-a-versioning-enabled-bucket.md)
[暂停版本控制下](manage-objects-in-a-versioning-suspended-bucket.md)[Object](manage-objects-in-a-versioning-suspended-bucket.md)[的操作](manage-objects-in-a-versioning-suspended-bucket.md)
[删除标记](delete-marker.md)
[常见问题](faq-4.md)
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
