# 请求者付费-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/enable-pay-by-requester-1

# 请求者付费
对外共享大量数据时，可开启存储空间（Bucket）的请求者付费模式，将访问数据产生的流量、请求等费用转由数据请求者承担，Bucket拥有者仅支付存储费用等固定成本。为Bucket开启请求者付费模式后，匿名访问将被禁用，所有请求需经过身份验证。
## 适用范围
仅有地域属性的Bucket支持开启请求者付费模式。
## 工作原理
OSS 按以下逻辑处理请求：
请求中携带x-oss-request-payer头，OSS 对请求者进行身份验证，验证通过后，流量和请求等费用由请求者承担。
请求中不携带x-oss-request-payer头：
请求者为 Bucket 拥有者：请求正常处理，所有费用由Bucket拥有者承担。
请求者非 Bucket 拥有者：请求被拒绝。
## Bucket 拥有者配置请求者付费
步骤一：开启请求者付费
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
单击Bucket 列表，然后单击目标Bucket名称。
在左侧导航栏，选择Bucket 配置>请求者付费。
在请求者付费页面，打开请求者付费开关。
在弹出的对话框，单击确定。
步骤二：为请求者授予访问权限
通过 Bucket Policy 为请求者授权访问，否则请求者将无法访问数据。
在[Bucket](https://oss.console.aliyun.com/bucket/)[列表](https://oss.console.aliyun.com/bucket/)，单击目标Bucket名称。
在左侧导航栏，选择权限控制>Bucket 授权策略。
在Bucket 授权策略页面的按图形策略添加页签，单击新增授权。
在新增授权面板，填写授权策略。其中，授权用户选择其他账号，填写请求者的账号ID或RAM角色ARN（格式为arn:sts::{RoleOwnerUid}:assumed-role/{RoleName}/{RoleSessionName}）。
单击确定。
## 请求者发起付费请求
作为请求者，访问已开启请求者付费模式的Bucket时，必须在请求中声明将承担本次请求产生的费用。
## 控制台
登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。
在左侧导航栏，单击我收藏的路径右侧的加号（+）。
在添加收藏路径对话框，按以下说明配置各项参数。
| 参数 | 说明 |
| --- | --- |
| 添加方式 | 选中 从其他已授权 bucket 添加 ，将授权访问的 Bucket 添加到收藏路径。 |
| 地域 | 下拉选择授权访问的 Bucket 所在地域。 |
| Bucket | 添加授权访问的 Bucket 名称。 |
| 请求者付费 | 选中 我已知晓并同意 后，即声明付费意愿。可以正常访问文件路径下的指定资源，访问该 Bucket 产生的流量、请求次数等费用将由您支付。 |
## SDK
以下代码以PutObject、GetObject和DeleteObject为例，用于指定第三方付费访问Object。其他用于指定第三方付费的Object读写操作接口设置方法类似。
第三方操作Object时需在HTTP Header中携带x-oss-request-payer:requester参数，否则会报错。
## Java
import com.aliyun.oss.ClientBuilderConfiguration; import com.aliyun.oss.OSS; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.OSSClientBuilder; import com.aliyun.oss.OSSException; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; import java.io.ByteArrayInputStream; public class Demo { public static void main(String[] args) throws Exception{ // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。关于其他Region对应的Endpoint信息，请参见访问域名和数据中心。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写Object完整路径，例如exampledir/exampleobject.txt。Object完整路径中不能包含Bucket名称。 String objectName = "exampledir/exampleobject.txt"; Payer payer = Payer.Requester; // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // PutObject接口指定付费者。 String content = "hello"; PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, objectName, new ByteArrayInputStream(content.getBytes())); putObjectRequest.setRequestPayer(payer); ossClient.putObject(putObjectRequest); // GetObject接口指定付费者。 GetObjectRequest getObjectRequest = new GetObjectRequest(bucketName, objectName); getObjectRequest.setRequestPayer(payer); OSSObject ossObject = ossClient.getObject(getObjectRequest); ossObject.close(); // DeleteObject接口指定付费者。 GenericRequest genericRequest = new GenericRequest(bucketName, objectName); genericRequest.setRequestPayer(payer); ossClient.deleteObject(genericRequest); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (Throwable ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { // 关闭OSSClient。 if (ossClient != null) { ossClient.shutdown(); } } } }
## Python
# -*- coding: utf-8 -*- import oss2 from oss2.credentials import EnvironmentVariableCredentialsProvider from oss2.headers import OSS_REQUEST_PAYER # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 auth = oss2.ProviderAuthV4(EnvironmentVariableCredentialsProvider()) # 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 endpoint = "https://oss-cn-hangzhou.aliyuncs.com" # 填写Endpoint对应的Region信息，例如cn-hangzhou。注意，v4签名下，必须填写该参数 region = "cn-hangzhou" # yourBucketName填写存储空间名称。 bucket = oss2.Bucket(auth, endpoint, "yourBucketName", region=region) # 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。 object_name = 'exampledir/exampleobject.txt' headers = dict() headers[OSS_REQUEST_PAYER] = "requester" # 上传文件时指定header。 result = bucket.put_object(object_name, 'test-content', headers=headers) # 下载文件时指定header。 result = bucket.get_object(object_name, headers=headers) # 删除文件时指定header。 result = bucket.delete_object(object_name, headers=headers);
## Go
package main import ( "fmt" "io" "os" "strings" "github.com/aliyun/aliyun-oss-go-sdk/oss" ) func main() { // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 provider, err := oss.NewEnvironmentVariableCredentialsProvider() if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 创建OSSClient实例。 // yourEndpoint填写Bucket对应的Endpoint，以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com。其它Region请按实际情况填写。 // yourRegion填写Bucket所在地域，以华东1（杭州）为例，填写为cn-hangzhou。其它Region请按实际情况填写。 clientOptions := []oss.ClientOption{oss.SetCredentialsProvider(&provider)} clientOptions = append(clientOptions, oss.Region("yourRegion")) // 设置签名版本 clientOptions = append(clientOptions, oss.AuthVersion(oss.AuthV4)) payerClient, err := oss.New("yourEndpoint", "", "", clientOptions...) if err != nil { fmt.Println("New Error:", err) os.Exit(-1) } // 填写Bucket名称。 payerBucket, err := payerClient.Bucket("examplebucket") if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 当Bucket拥有者开启请求者付费模式后，外部访问者必须设置oss.RequestPayer(oss.Requester)参数才可以访问授权的内容。 // 当Bucket拥有者没有开启付费模式时，外部访问者可以不用携带oss.RequestPayer(oss.Requester)参数即可访问授权的内容。 // 上传Object。 // 填写Object完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。 key := "exampledir/exampleobject.txt" err = payerBucket.PutObject(key, strings.NewReader("objectValue"), oss.RequestPayer("requester")) if err != nil { fmt.Println("put Error:", err) os.Exit(-1) } // 列举Bucket下的所有Object。 lor, err := payerBucket.ListObjects(oss.RequestPayer(oss.Requester)) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } // 打印Object名称列表。 for _, l := range lor.Objects { fmt.Println("the Key name is :", l.Key) } // 下载Object。 body, err := payerBucket.GetObject(key, oss.RequestPayer(oss.Requester)) if err != nil { fmt.Println("Get Error:", err) os.Exit(-1) } // 数据读取完成后，获取的流必须关闭，否则会造成连接泄漏，导致请求无连接可用，程序无法正常工作。 defer body.Close() // 读取并打印获取的内容。 data, err := io.ReadAll(body) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } fmt.Println("data:", string(data)) // 删除Object。 err = payerBucket.DeleteObject(key, oss.RequestPayer(oss.Requester)) if err != nil { fmt.Println("Error:", err) os.Exit(-1) } }
## Node.js
const OSS = require('ali-oss'); const bucket = 'bucket-name'; const payer = 'Requester'; const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: 'yourregion', // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, authorizationV4: true, // yourBucketName填写Bucket名称。 bucket: 'yourBucketName', }); async function main() { await put(); await get(); await del(); } async function put() { const result = await client.putBucketRequestPayment(bucket, payer); console.log('putBucketRequestPayment:', result); // PutObject接口指定付费者。 const response = await client.put('fileName', path.normalize('D:\\localpath\\examplefile.txt'), { headers: { 'x-oss-request-payer': 'requester' } }); console.log('put:', response); } async function get() { const result = await client.putBucketRequestPayment(bucket, payer); console.log('putBucketRequestPayment:', result); // GetObject接口指定付费者。 const response = await client.get('fileName', { headers: { 'x-oss-request-payer': 'requester' } }); console.log('get:', response); } async function del() { const result = await client.putBucketRequestPayment(bucket, payer); console.log('putBucketRequestPayment:', result); // DeleteObject接口指定付费者。 const response = await client.delete('fileName', { headers: { 'x-oss-request-payer': 'requester' } }); console.log('delete:', response); } main();
## C#
using System; using System.IO; using System.Text; using Aliyun.OSS; using Aliyun.OSS.Common; namespace Samples { public class Program { public static void Main(string[] args) { // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称，例如examplebucket。 var bucketName = "examplebucket"; var objectName = "example.txt"; var objectContent = "More than just cloud."; // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。 const string region = "cn-hangzhou"; // 创建ClientConfiguration实例，按照您的需要修改默认参数。 var conf = new ClientConfiguration(); // 设置v4签名。 conf.SignatureVersion = SignatureVersion.V4; // 创建OssClient实例。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf); try { byte[] binaryData = Encoding.ASCII.GetBytes(objectContent); MemoryStream requestContent = new MemoryStream(binaryData); // PutObject接口指定付费者。 var putRequest = new PutObjectRequest(bucketName, objectName, requestContent); putRequest.RequestPayer = RequestPayer.Requester; var result = client.PutObject(putRequest); // GetObject接口指定付费者。 var getRequest = new GetObjectRequest(bucketName, objectName); getRequest.RequestPayer = RequestPayer.Requester; var getResult = client.GetObject(getRequest); // DeleteObject接口指定付费者。 var delRequest = new DeleteObjectRequest(bucketName, objectName); delRequest.RequestPayer = RequestPayer.Requester; client.DeleteObject(delRequest); } catch (OssException ex) { Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}", ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId); } catch (Exception ex) { Console.WriteLine("Failed with error info: {0}", ex.Message); } } } }
## PHP
<?php if (is_file(__DIR__ . '/../autoload.php')) { require_once __DIR__ . '/../autoload.php'; } if (is_file(__DIR__ . '/../vendor/autoload.php')) { require_once __DIR__ . '/../vendor/autoload.php'; } use OSS\Credentials\EnvironmentVariableCredentialsProvider; use OSS\OssClient; use OSS\Core\OssException; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 $provider = new EnvironmentVariableCredentialsProvider(); // Endpoint以杭州为例，其它Region请按实际情况填写。 $endpoint = "http://oss-cn-hangzhou.aliyuncs.com"; // 填写Bucket名称，例如examplebucket。 $bucket= "examplebucket"; // 填写Object的完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。 $object = "exampledir/exampleobject.txt"; // 指定为请求者付费模式。 $options = array( OssClient::OSS_HEADERS => array( OssClient::OSS_REQUEST_PAYER => 'requester', )); try { $config = array( "provider" => $provider, "endpoint" => $endpoint, "signatureVersion" => OssClient::OSS_SIGNATURE_VERSION_V4, "region"=> "cn-hangzhou" ); $ossClient = new OssClient($config); // PutObject接口指定付费者。 $content = "hello"; $ossClient->putObject($bucket, $object, $content, $options); // GetObject接口指定付费者。 $ossClient->getObject($bucket, $object, $options); // DeleteObject接口指定付费者。 $ossClient->deleteObject($bucket, $object, $options); } catch (OssException $e) { printf(__FUNCTION__ . ": FAILED\n"); printf($e->getMessage() . "\n"); return; } print(__FUNCTION__ . ": OK" . "\n");
## C++
#include <alibabacloud/oss/OssClient.h> #include <fstream> using namespace AlibabaCloud::OSS; int main(void) { /*初始化OSS账号信息。*/ /*yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; / *yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn - hangzhou。 * / std::string Region = "yourRegion"; /*填写请求者访问的Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /*填写请求者访问的Object的完整路径，完整路径中不能包含Bucket名称，例如exampledir/exampleobject.txt。*/ std::string ObjectName = "exampleobject.txt"; /* 初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; conf.signatureVersion = SignatureVersionType::V4; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已通过环境变量设置请求者的OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); client.SetRegion(Region); /* 上传文件时设置请求者付费模式。*/ std::shared_ptr<std::iostream> content = std::make_shared<std::stringstream>(); *content << "test cpp sdk"; PutObjectRequest putrequest(BucketName, ObjectName, content); putrequest.setRequestPayer(RequestPayer::Requester); auto putoutcome = client.PutObject(putrequest); /* 下载文件到本地内存时设置请求者付费模式。*/ GetObjectRequest getrequest(BucketName, ObjectName); getrequest.setRequestPayer(RequestPayer::Requester); auto getoutcome = client.GetObject(getrequest); /* 删除文件时设置请求者付费模式。*/ DeleteObjectRequest delrequest(BucketName, ObjectName); delrequest.setRequestPayer(RequestPayer::Requester); auto deloutcome = client.DeleteObject(delrequest); /* 释放网络等资源。*/ ShutdownSdk(); return 0; }
## ossutil
使用命令行工具ossutil前，请先[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以使用 cp 命令下载对象为例，请指定--request-payer=requester参数
ossutil cp oss://examplebucket/examplefile.txt /localpath --request-payer=requester
## API
可直接发起REST API请求，需在请求头中加入x-oss-request-payer: requester，并确保此请求头包含在签名计算中，签名的计算方法见[在](../developer-reference/recommend-to-use-signature-version-4.md)[Header](../developer-reference/recommend-to-use-signature-version-4.md)[中包含签名](../developer-reference/recommend-to-use-signature-version-4.md)。
GET /oss.jpg HTTP/1.1 Host: oss-example.oss-cn-hangzhou.aliyuncs.com Date: Fri, 24 Feb 2012 06:38:30 GMT Authorization: OSS4-HMAC-SHA256 Credential=LTAI********************/20250417/cn-hangzhou/oss/aliyun_v4_request,Signature=a7c3554c729d71929e0b84489addee6b2e8d5cb48595adfc51868c299c0c218e
## 应用于生产环境
RAM 角色访问的计费归属：当请求者通过扮演阿里云RAM角色来访问数据时，该角色所属的账户将为此请求付费。
错误做法：让请求者扮演Bucket 拥有者账号下的 RAM 角色来获取访问数据的权限。此场景下，所有请求是以 Bucket 拥有者的身份执行，产生的请求和流量费用仍将由 Bucket 拥有者支付，无法实现成本转移。
正确做法：通过Bucket Policy 直接为请求者授予访问数据的权限。
预签名 URL 陷阱：
错误做法：由 Bucket 拥有者使用身份凭证（AccessKey 或 STS 临时凭证）生成预签名 URL 并对外分享，此时请求是以Bucket 拥有者身份发起，相关费用由Bucket 拥有者承担。
正确做法：由请求方使用身份凭证（AccessKey 或 STS 临时凭证）来生成预签名 URL，并在生成时包含x-oss-request-payer=requester参数，签名的计算方法见[在](../developer-reference/add-signatures-to-urls.md)[URL](../developer-reference/add-signatures-to-urls.md)[中包含签名](../developer-reference/add-signatures-to-urls.md)。请求方将此 URL 对外分享使用时，费用由请求方承担。
兼容性风险：开启请求者付费会影响静态网站托管依赖的匿名访问机制，导致网站无法正常工作，建议将网站前端资源（HTML/CSS/JS）与需要请求者付费的数据分别部署在不同的Bucket中。
## 计费说明
Bucket开启请求者付费前，所有费用均由Bucket拥有者支付。开启请求者付费后，以下付费项由请求者的账号支付，其余计费项还是由Bucket拥有者的账号支付，完整计费项参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。
| 费用 | 计费项 |
| --- | --- |
| [流量费用](../traffic-fees.md) | 外网流出流量 |
| CDN 回源流出流量 |  |
| [请求费用](../api-operation-calling-fees.md) | Put 类型请求 |
| Get 类型请求 |  |
| [数据处理](../data-processing-fees.md) | 图片处理 |
| 视频截帧 |  |
| 低频访问数据取回容量 |  |
| 归档存储数据取回容量 |  |
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
