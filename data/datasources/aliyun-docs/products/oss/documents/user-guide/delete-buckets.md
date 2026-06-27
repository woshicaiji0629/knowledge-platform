# 删除Bucket以停止计费-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/delete-buckets

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

# 删除存储空间以停止计费

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您不再需要某个存储空间（Bucket）时，可以通过删除 Bucket 来彻底停止其计费。由于OSS的费用主要来源于Bucket内部资源，而删除Bucket前系统强制要求清空所有内部资源，因此删除Bucket是确保您不会遗漏任何计费资源而产生意外费用的最可靠方式。请注意，删除后数据无法恢复，且Bucket名称释放后存在被他人占用的风险。如果要完全停用整个OSS服务，您必须删除账号下的全部 Bucket。

## 删除前风险评估

- 

数据不可恢复风险

删除将永久清除所有文件（含历史版本/碎片）。操作不可逆，请务必提前[备份](products/oss/documents/user-guide/configure-scheduled-backup.md)。

- 

业务中断风险

删除将导致依赖此 Bucket 的网站、App 或 CDN立即中断。请确保无业务正在访问。

- 

Bucket 名称抢占风险

删除后名称需 4-8 小时冷却释放。如需保留名称，建议仅清空文件，不要删除 Bucket。

- 

同步删除风险

若开启了跨/同区域复制，删除操作可能会同步清除目标 Bucket 的数据，请检查配置。

- 

成本与时间预估

清理大量文件可能产生 API 请求费用，且需要数小时或更长时间（视文件量而定）。

## 检查必须删除的资源

如果Bucket中残留文件、碎片、接入点、加速器或RTMP推流地址等一种或多种必须删除的资源没有清理，在删除 Bucket 时将出现“存储空间不为空”的报错。建议使用 OSS 控制台删除向导，可自动扫描并列出所有待清理项。

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击目标Bucket名称。

- 

下滑左侧导航栏至底部，单击删除Bucket。

- 

在删除Bucket页面，可以看到检测出的待清理项。

## 清理必须删除的资源

删除 Bucket 的前提是清空其内部的所有资源，请根据[系统检测出的剩余资源](products/oss/documents/user-guide/delete-buckets.md)进行清理。文件量较大时，推荐[使用生命周期规则](products/oss/documents/user-guide/delete-buckets.md)自动处理。

## 清理文件

若文件资源的状态列提示已开启 HDFS 功能，请先清理HDFS 文件。若已开启版本控制，OSS文件列表会同时显示当前版本与历史版本，因此执行全选删除时会一并删除所有版本文件。

## OSS文件

## 使用OSS控制台

- 

在删除Bucket页面的清空任务区域，找到文件资源项，单击前往删除。

- 

选中所有Object，单击下方的彻底删除。

- 

在弹出的对话框中，单击确定。

## 使用ossutil

删除该bucket下所有文件（包括当前版本和历史版本）

ossutil rm oss://examplebucket/ -r

更多示例，请参见[rm（删除）](products/oss/documents/developer-reference/rm-deleted.md)。

## HDFS文件

通过OSS控制台的方式

- 

在文件资源的状态列单击立即暂停，停止HDFS后台任务。

- 

单击前往删除，进入HDFS页签。

- 

逐个单击彻底删除，直至清空所有HDFS文件。

通过HDFS Shell命令的方式hdfs dfs -rm -r -skipTrash oss://examplebucket.cn-hangzhou.oss-dls.aliyuncs.com/*

更多信息，请参见[通过](products/oss/documents/user-guide/connect-non-emr-clusters-to-oss-hdfs.md)[HDFS Shell](products/oss/documents/user-guide/connect-non-emr-clusters-to-oss-hdfs.md)[命令执行](products/oss/documents/user-guide/connect-non-emr-clusters-to-oss-hdfs.md)[OSS-HDFS](products/oss/documents/user-guide/connect-non-emr-clusters-to-oss-hdfs.md)[服务快速入门常见操作。](products/oss/documents/user-guide/connect-non-emr-clusters-to-oss-hdfs.md)

## 清理碎片

## 使用OSS控制台

- 

在删除Bucket页面的清空任务区域，找到碎片资源项，单击前往删除。

- 

在文件列表页面，单击碎片管理。

- 

在碎片管理（Multipart）面板，单击删除所有。

- 

在弹出的对话框中，单击确定。

## 使用ossutil

删除未完成或未取消上传的所有分片碎片。

ossutil rm oss://examplebucket -m -r -f

更多信息，请参见[rm（删除）](products/oss/documents/developer-reference/rm-deleted.md)。

## 清理接入点

- 

在删除Bucket页面的清空任务区域，找到接入点资源项，单击前往删除。

- 

逐个单击删除接入点。

- 

按指引删除对应访问策略。

- 

删除访问策略后，回到接入点列表。按页面引导输入接入点名称，单击确定完成删除。

## 清理加速器

请注意，删除加速器仅会清除加速器内缓存的数据，存储在OSS桶中的数据不会受到影响。

- 

在删除Bucket页面的清空任务区域，找到加速器资源项，单击前往删除。

- 

在OSS加速器列表操作列单击删除按钮。

- 

按页面引导输入加速器名称，单击确定完成删除。

## 清理RTMP推流地址

Bucket的LiveChannel查看和删除暂不支持通过工具和控制台操作，可以使用接口或者是SDK来实现操作，请参见[DeleteLiveChannel](products/oss/documents/developer-reference/deletelivechannel.md)，删除指定的LiveChannel。示例代码如下：

import com.aliyun.oss.ClientBuilderConfiguration; import com.aliyun.oss.OSS; import com.aliyun.oss.OSSClientBuilder; import com.aliyun.oss.OSSException; import com.aliyun.oss.common.auth.CredentialsProviderFactory; import com.aliyun.oss.common.auth.EnvironmentVariableCredentialsProvider; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.LiveChannelGenericRequest; /** * 删除指定的LiveChannel示例代码 * 该程序演示如何删除阿里云OSS中的LiveChannel */ public class Demo { public static void main(String[] args) throws Exception { // OSS服务地址，根据实际地域选择对应的Endpoint，此处以杭州地域为例。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写LiveChannel名称。 String liveChannelName = "yourLiveChannelName"; // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 创建删除LiveChannel的请求 LiveChannelGenericRequest request = new LiveChannelGenericRequest(bucketName, liveChannelName); // 执行删除操作 ossClient.deleteLiveChannel(request); } catch (OSSException oe) { // 处理OSS服务端返回的异常 oe.printStackTrace(); System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (Exception e) { System.out.println("Caught an unexpected exception:"); e.printStackTrace(); } finally { if (ossClient != null) { // 释放OSSClient资源 ossClient.shutdown(); } } } }

## 删除Bucket

在确认Bucket 内所有资源均已清理完毕后，您可以执行删除操作。

## 使用OSS控制台

- 

返回目标 Bucket 的删除 Bucket页面。

- 

单击立即删除，按页面引导输入Bucket名称，单击确定完成删除。

## ossutil

以下命令用于删除存储空间examplebucket。

ossutil api delete-bucket --bucket examplebucket

更多信息，请参见[delete-bucket](products/oss/documents/developer-reference/delete-bucket.md)。

## OSS SDK

以下仅列举常见SDK的删除Bucket的代码示例。关于其他SDK的删除Bucket的代码示例，请参见[SDK](products/oss/documents/developer-reference/overview-21.md)[简介](products/oss/documents/developer-reference/overview-21.md)。

### Java

import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 删除存储空间。 ossClient.deleteBucket(bucketName); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }

## Python

import argparse import alibabacloud_oss_v2 as oss # 创建命令行参数解析器，描述此脚本用于删除指定的OSS Bucket。 parser = argparse.ArgumentParser(description="Delete a specified OSS bucket.") # 添加命令行参数 --region，表示存储空间所在的区域，必需参数 parser.add_argument('--region', help='The region in which the bucket is located.', required=True) # 添加命令行参数 --bucket，表示存储空间的名称，必需参数 parser.add_argument('--bucket', help='The name of the bucket to delete.', required=True) # 添加命令行参数 --endpoint，表示其他服务可用来访问OSS的域名，非必需参数 parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS.') def main(): """ 主函数，用于解析命令行参数并执行删除指定Bucket的操作。 """ args = parser.parse_args() # 解析命令行参数 # 从环境变量中加载凭证信息，用于身份验证 credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider() # 使用SDK的默认配置，并设置凭证提供者和区域信息 cfg = oss.config.load_default() cfg.credentials_provider = credentials_provider cfg.region = args.region # 如果提供了endpoint参数，则设置配置中的endpoint if args.endpoint is not None: cfg.endpoint = args.endpoint # 使用配置好的信息创建OSS客户端 client = oss.Client(cfg) # 构造请求以删除指定的Bucket request = oss.DeleteBucketRequest(bucket=args.bucket) try: # 发送请求并获取响应结果 result = client.delete_bucket(request) # 打印响应结果的状态码和请求ID print(f'status code: {result.status_code},' f' request id: {result.request_id}') except oss.exceptions.OssError as e: # 捕获并打印可能发生的异常 print(f"Failed to delete bucket: {e}") if __name__ == "__main__": main() # 脚本入口，当文件被直接运行时调用main函数

## Go

package main import ( "context" "flag" "log" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials" ) var ( region string bucketName string ) func init() { // 定义命令行参数，用于指定区域和存储空间名称 flag.StringVar(&region, "region", "", "The region in which the bucket is located.") flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.") } func main() { // 解析命令行参数 flag.Parse() // 检查存储空间名称参数是否为空 if len(bucketName) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, bucket name required") } // 检查区域参数是否为空 if len(region) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, region required") } // 加载默认配置并设置凭证提供者和区域 cfg := oss.LoadDefaultConfig(). WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()). WithRegion(region) // 创建OSS客户端 client := oss.NewClient(cfg) // 创建删除存储空间请求对象 request := &oss.DeleteBucketRequest{ Bucket: oss.Ptr(bucketName), } // 调用DeleteBucket方法删除存储空间 result, err := client.DeleteBucket(context.TODO(), request) if err != nil { log.Fatalf("failed to delete bucket %v", err) } // 打印删除结果 log.Printf("delete bucket result:%#v\n", result) }

## PHP

<?php require_once __DIR__ . '/../vendor/autoload.php'; // 引入自动加载文件，加载依赖库 use AlibabaCloud\Oss\V2 as Oss; // 定义命令行参数描述 $optsdesc = [ "region" => ['help' => 'The region in which the bucket is located.', 'required' => True], // 区域是必填项，存储空间所在的区域，例如 oss-cn-hangzhou。 "endpoint" => ['help' => 'The domain names that other services can use to access OSS.', 'required' => False], // 终端节点是可选项，其他服务可以用来访问OSS的域名。 "bucket" => ['help' => 'The name of the bucket', 'required' => True], // 存储空间名称是必填项。 ]; $longopts = \array_map(function ($key) { return "$key:"; // 每个参数后面加冒号，表示需要值 }, array_keys($optsdesc)); // 解析命令行参数 $options = getopt("", $longopts); // 检查必填参数是否缺失 foreach ($optsdesc as $key => $value) { if ($value['required'] === True && empty($options[$key])) { $help = $value['help']; echo "Error: the following arguments are required: --$key, $help"; // 提示用户缺少必填参数 exit(1); } } // 获取命令行参数值 $region = $options["region"]; // 存储空间所在区域。 $bucket = $options["bucket"]; // 存储空间名称。 // 使用环境变量加载凭证信息（AccessKeyId 和 AccessKeySecret） $credentialsProvider = new Oss\Credentials\EnvironmentVariableCredentialsProvider(); // 使用SDK的默认配置 $cfg = Oss\Config::loadDefault(); // 加载SDK的默认配置。 $cfg->setCredentialsProvider($credentialsProvider); // 设置凭证提供者。 $cfg->setRegion($region); // 设置区域。 if (isset($options["endpoint"])) { $cfg->setEndpoint($options["endpoint"]); // 如果提供了终端节点，则设置终端节点。 } // 创建OSS客户端实例 $client = new Oss\Client($cfg); // 创建删除存储空间的请求对象 $request = new Oss\Models\DeleteBucketRequest($bucket); // 调用deleteBucket方法删除存储空间 $result = $client->deleteBucket($request); // 打印返回结果 printf( 'status code:' . $result->statusCode . PHP_EOL . // HTTP响应状态码。 'request id:' . $result->requestId // 请求的唯一标识。 );

### Node.js

const OSS = require('ali-oss'); const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: 'yourregion', // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, authorizationV4: true, // yourBucketName填写Bucket名称。 bucket: 'yourBucketName', }); async function deleteBucket() { try { // 指定存储空间名称。 const result = await client.deleteBucket('yourbucketname'); console.log(result); } catch (err) { console.log(err); } } deleteBucket();

### .NET

using System; using Aliyun.OSS; using Aliyun.OSS.Common; namespace Samples { public class Program { public static void Main(string[] args) { // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称，例如examplebucket。 var bucketName = "examplebucket314"; // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。 const string region = "cn-hangzhou"; // 创建ClientConfiguration实例，按照您的需要修改默认参数。 var conf = new ClientConfiguration(); // 设置v4签名。 conf.SignatureVersion = SignatureVersion.V4; // 创建OssClient实例。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf); client.SetRegion(region); try { client.DeleteBucket(bucketName); Console.WriteLine("Delete bucket succeeded"); } catch (Exception ex) { Console.WriteLine("Delete bucket failed. {0}", ex.Message); } } } }

### Android

DeleteBucketRequest deleteBucketRequest = new DeleteBucketRequest("bucketName"); // 异步删除存储空间。 OSSAsyncTask deleteBucketTask = oss.asyncDeleteBucket(deleteBucketRequest, new OSSCompletedCallback<DeleteBucketRequest, DeleteBucketResult>() { @Override public void onSuccess(DeleteBucketRequest request, DeleteBucketResult result) { Log.d("asyncDeleteBucket", "Success!"); } @Override public void onFailure(DeleteBucketRequest request, ClientException clientException, ServiceException serviceException) { // 请求异常。 if (clientException != null) { // 本地异常，如网络异常等。 clientException.printStackTrace(); } if (serviceException != null) { // 服务异常。 Log.e("ErrorCode", serviceException.getErrorCode()); Log.e("RequestId", serviceException.getRequestId()); Log.e("HostId", serviceException.getHostId()); Log.e("RawMessage", serviceException.getRawMessage()); } } });

### iOS

OSSDeleteBucketRequest * delete = [OSSDeleteBucketRequest new]; // 填写存储空间名称，例如examplebucket。 delete.bucketName = @"examplebucket"; OSSTask * deleteTask = [client deleteBucket:delete]; [deleteTask continueWithBlock:^id(OSSTask *task) { if (!task.error) { NSLog(@"delete bucket success!"); } else { NSLog(@"delete bucket failed, error: %@", task.error); } return nil; }]; // 实现同步阻塞等待任务完成。 // [getdeleteTask waitUntilFinished];

### C++

#include <alibabacloud/oss/OssClient.h> using namespace AlibabaCloud::OSS; int main(void) { /*初始化OSS账号信息。*/ /*yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; / *yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn - hangzhou。 * / std::string Region = "yourRegion"; /*填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /*初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; conf.signatureVersion = SignatureVersionType::V4; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); client.SetRegion(Region); /*删除Bucket。*/ DeleteBucketRequest request(BucketName); auto outcome = client.DeleteBucket(request); if (outcome.isSuccess()) { std::cout << "Delete bucket successfully." << std::endl; } else { std::cout << "Failed to delete bucket. Error code: " << outcome.error().Code() << ", Message: " << outcome.error().Message() << ", RequestId: " << outcome.error().RequestId() << std::endl; } /*释放网络等资源。*/ ShutdownSdk(); return 0; }

### C

#include "oss_api.h" #include "aos_http_io.h" /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ const char *endpoint = "yourEndpoint"; /* 填写Bucket名称，例如examplebucket。*/ const char *bucket_name = "examplebucket"; /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/ const char *region = "yourRegion"; void init_options(oss_request_options_t *options) { options->config = oss_config_create(options->pool); /* 用char*类型的字符串初始化aos_string_t类型。*/ aos_str_set(&options->config->endpoint, endpoint); /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ aos_str_set(&options->config->access_key_id, getenv("OSS_ACCESS_KEY_ID")); aos_str_set(&options->config->access_key_secret, getenv("OSS_ACCESS_KEY_SECRET")); //需要额外配置以下两个参数 aos_str_set(&options->config->region, region); options->config->signature_version = 4; /* 是否使用CNAME域名访问OSS服务。0表示不使用。*/ options->config->is_cname = 0; /* 设置网络相关参数，比如超时时间等。*/ options->ctl = aos_http_controller_create(options->pool, 0); } int main(int argc, char *argv[]) { /* 在程序入口调用aos_http_io_initialize方法来初始化网络、内存等全局资源。*/ if (aos_http_io_initialize(NULL, 0) != AOSE_OK) { exit(1); } /* 用于内存管理的内存池（pool），等价于apr_pool_t。其实现代码在apr库中。*/ aos_pool_t *pool; /* 重新创建一个内存池，第二个参数是NULL，表示没有继承其它内存池。*/ aos_pool_create(&pool, NULL); /* 创建并初始化options，该参数包括endpoint、access_key_id、acces_key_secret、is_cname、curl等全局配置信息。*/ oss_request_options_t *oss_client_options; /* 在内存池中分配内存给options。*/ oss_client_options = oss_request_options_create(pool); /* 初始化Client的选项oss_client_options。*/ init_options(oss_client_options); /* 初始化参数。*/ aos_string_t bucket; aos_table_t *resp_headers = NULL; aos_status_t *resp_status = NULL; /* 将char*类型数据赋值给aos_string_t类型的存储空间。*/ aos_str_set(&bucket, bucket_name); /* 删除存储空间。*/ resp_status = oss_delete_bucket (oss_client_options, &bucket, &resp_headers); if (aos_status_is_ok(resp_status)) { printf("delete bucket succeeded\n"); } else { printf("delete bucket failed\n"); } /* 释放内存池，相当于释放了请求过程中各资源分配的内存。*/ aos_pool_destroy(pool); /* 释放之前分配的全局资源。*/ aos_http_io_deinitialize(); return 0; }

### Ruby

require 'aliyun/oss' client = Aliyun::OSS::Client.new( # Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 endpoint: 'https://oss-cn-hangzhou.aliyuncs.com', # 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 access_key_id: ENV['OSS_ACCESS_KEY_ID'], access_key_secret: ENV['OSS_ACCESS_KEY_SECRET'] ) # 填写Bucket名称，例如examplebucket。 client.delete_bucket('examplebucket')

## 自动清理海量文件和碎片

当 Bucket 内文件数量巨大（例如百万级以上）时，配置生命周期规则是最高效、经济的清理方式。该方案通过设置一条“过期即删”的规则，让系统在指定时间后自动删除 Bucket 内的所有数据。如对生命周期规则不熟悉，建议先在测试Bucket中进行验证。

请注意，文件删除操作不可逆，操作前务必谨慎。

Bucket未开启版本控制

对于未开启版本控制的Bucket，只需要配置一条生命周期规则，即可自动快速清理所有文件和碎片（Multipart Upload产生的未合并碎片）。

- 

登录OSS管理控制台的[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，找到目标Bucket。

- 

在左侧导航栏，选择数据安全>版本控制，确认Bucket未开启版本控制。

- 

在左侧导航栏，选择数据管理>生命周期，设置生命周期规则，指定Bucket内所有文件在最后一次修改后1天自动删除，同时对生成时间早于1天的文件碎片，自动执行清理操作。

Bucket已开启版本控制

Bucket开启版本控制后，会产生当前版本文件、历史版本文件、碎片文件和删除标记。只需要配置一条生命周期规则，即可自动快速清理这些文件。

- 

登录OSS管理控制台的[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，找到目标Bucket。

- 

在左侧导航栏，选择数据安全>版本控制，确认Bucket已开启版本控制。

- 

在左侧导航栏，选择数据管理>生命周期，设置生命周期规则，指定Bucket内所有当前版本、历史版本文件在最后一次修改后1天自动删除，同时对生成时间早于1天的文件碎片，自动执行清理操作。该规则会同步清理删除标记。

## 常见问题

### 删除时提示“Bucket不为空”怎么办？

Bucket内还有资源未清理。建议通过OSS控制台查看当前剩余资源，然后参照[清理必须删除的资源](products/oss/documents/user-guide/delete-buckets.md)进行清理，清理完毕后重试删除Bucket。

### 删除后为何无法立即创建同名Bucket？

删除Bucket后，Bucket名称在删除后有4-8小时的冷却期，在此期间，任何用户都无法使用该名称创建新 Bucket。如果业务紧急，请使用新的Bucket名称。

冷却期结束后，该名称将对所有用户开放。如果未及时重新创建，存在被其他用户抢先注册的风险。

### 如何批量删除多个Bucket？

警告

批量删除是一项高风险操作，可能导致大量数据永久丢失。执行前，请务必再三确认待删除的Bucket列表，并完成所有必要的数据备份。

OSS控制台不提供批量删除功能，但您可以通过编写脚本结合ossutil实现。

核心实现原理如下：

- 

准备清单：创建一个准确无误的、包含所有待删除Bucket名称的文本文件或列表。

- 

循环执行：您的脚本需要遍历这个清单，对每一个Bucket名称执行以下两个关键步骤。

- 

清空资源：为当前Bucket调用ossutil的清空命令。

- 

删除空Bucket：在确认上一步成功后，再调用ossutil的删除Bucket命令。

### 删除时提示“权限不足”怎么办？

删除Bucket前需先清理内部资源，清理过程中涉及列举（list）和删除（delete）等多项权限，建议联系管理员一次性为您的RAM身份授予[AliyunOSSFullAccess](https://ram.console.aliyun.com/policies/detail?policyType=System&policyName=AliyunOSSFullAccess)权限，避免因权限点遗漏导致删除失败。

### 如何彻底停止OSS计费？

要彻底停止对象存储 OSS 服务产生的所有费用，您必须删除您账号下的全部 Bucket。只要账号下还存在任何 Bucket（即使是空的），或有未结清的账单，都可能与 OSS 计费相关。

### 误删Bucket后能否恢复？

不能。 删除操作不可逆，请务必先备份再删除。

[上一篇：列举存储空间](products/oss/documents/user-guide/list-buckets-11.md)[下一篇：存储空间地域属性](products/oss/documents/user-guide/region-attribute-of-buckets.md)

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
