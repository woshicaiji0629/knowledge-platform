# 通过存储空间清单获取Bucket内的Object信息-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/bucket-inventory

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

# 使用存储空间清单

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当存储空间（Bucket）中的文件（Object）数量达到数百万甚至上百亿时，通过ListObjects接口逐一列举效率低且成本高。存储空间清单功能通过异步、定期扫描 Bucket，生成包含指定对象元数据（如大小、存储类型等）的清单文件，适用于海量对象的管理场景。

## 适用范围

- 

仅有地域属性的Bucket支持开启存储空间清单功能。

- 

如需使用增量清单功能，请联系[技术支持](https://selfservice.console.aliyun.com/ticket/createIndex)申请。

## 使用场景

OSS 提供全量清单和增量清单。其中，全量清单是指对某一时间点 Bucket 内所有存量文件的快照，增量清单则记录了指定时间段内新增或变动的文件元数据。全量清单和增量清单均可以按照一定周期生成清单文件，并投递到指定的 Bucket 进行转存。可配置按周期生成一次全量清单，并且通常每 10 分钟生成一次增量清单文件。使用全量清单文件和增量清单文件的场景如下：

- 

一次性的数据分析和统计场景：若仅需要对历史文件进行统计，可以配置全量清单生成规则，定期生成一次全量文件元数据清单，用以离线的数据统计、数据分析。

- 

持续性的数据分析和统计场景：不仅需要对历史文件进行统计分析，也需要对后续的增量文件进行统计和分析，可以基于全量元数据清单和增量元数据清单构建统一的元数据表，如将存量和增量元数据均写入到自建的 table 中，通过自己的 spark 集群进行元数据检索、查询、统计和分析。

## 工作原理

- 

全量清单：定期（每天、每周或每月）为存储空间中的对象生成一份完整的快照，其工作流程如下：

- 

获取权限：OSS 通过扮演一个预先授权的 RAM 角色，来获得扫描源Bucket和向目标 Bucket 写入清单报告的权限。

- 

扫描对象：OSS 根据清单规则中定义的筛选条件（如对象前缀、版本状态、创建时间或大小），扫描源 Bucket 中的所有匹配对象。

- 

生成清单报告：OSS 将扫描结果聚合生成清单报告，并以 Gzip 压缩的 CSV 文件格式，写入目标的 Bucket 中。

- 

增量清单：通常以10分钟为周期，捕获并报告该时间窗口内发生的所有对象变更事件（包括创建、元数据更新、删除），其工作流程如下：

- 

获取权限：OSS 通过扮演一个预先授权的 RAM 角色，来获得扫描源Bucket日志和向目标 Bucket 写入清单报告的权限。

- 

扫描对象：OSS 根据规则中定义的筛选条件（如对象前缀），扫描增量日志中所有匹配的记录。

- 

生成清单报告：OSS 将扫描结果，以后端分区聚合的方式，生成清单报告，以CSV格式写入指定的目标Bucket 中。

创建清单规则后，OSS 会周期自动执行清单任务，该任务在后台异步运行，不影响对 Bucket 的正常访问。

## 创建并授权服务角色

OSS 清单服务需要通过扮演 RAM 角色来获得读取源 Bucket和写入目标 Bucket的权限。为确保账户安全，建议遵循最小权限原则，为清单功能创建专用的服务角色。

通过控制台快速配置清单时，系统会引导自动创建名为AliyunOSSRole的角色，可直接使用默认角色，无需自行创建服务角色。但此角色拥有对账户下所有 Bucket 的完全管理权限，不建议在生产环境中使用AliyunOSSRole。

以下是手动创建最小权限角色的步骤：

（可选）为RAM 用户授予配置清单的权限

阿里云账号默认拥有全部权限，可跳过此步骤。

此步骤旨在授权 RAM 用户（例如运维管理员）去配置清单规则，而不是为清单服务本身授权。为遵循安全最佳实践，推荐由阿里云账号或具备高权限的管理员预先创建好清单服务所需的 RAM 角色。然后，普通 RAM 用户在配置清单时，只需被授予使用该角色的权限即可，无需自行创建角色。

如果需要授予 RAM 用户创建和管理清单规则的权限，请[为其授予](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)包含以下权限的自定义策略：

以下策略中的oss:ListBuckets权限仅在通过控制台操作时需要。如果通过 SDK 或 ossutil 等工具访问，则无需此权限。{ "Statement": [ { "Effect": "Allow", "Action": [ "oss:PutBucketInventory", "oss:GetBucketInventory", "oss:DeleteBucketInventory", "oss:ListBuckets", "ram:CreateRole", "ram:AttachPolicyToRole", "ram:GetRole", "ram:ListPoliciesForRole" ], "Resource": "*" } ], "Version": "1" }

提示：如果当前 RAM 用户已拥有AliyunOSSFullAccess系统权限，则仅需为其补充授予角色管理的相关权限即可：

{ "Statement": [ { "Effect": "Allow", "Action": [ "ram:CreateRole", "ram:AttachPolicyToRole", "ram:GetRole", "ram:ListPoliciesForRole" ], "Resource": "*" } ], "Version": "1" }

- 

创建RAM角色：进入[创建](https://ram.console.aliyun.com/roles/create)[RAM](https://ram.console.aliyun.com/roles/create)[角色](https://ram.console.aliyun.com/roles/create)页面。信任主体类型选择云服务，信任主体名称选择对象存储。

- 

为RAM角色授予写入目标 Bucket 的权限：

- 

在[创建权限策略](https://ram.console.aliyun.com/policies/create)页面，单击脚本编辑页签。将以下策略内容粘贴到策略编辑器中，并将dest-bucket替换为实际的源Bucket名称。

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "oss:PutObject", "Resource": [ "acs:oss:*:*:dest-bucket/*" ] } ] }

- 

（可选）配置 KMS 加密权限：如果清单报告需要使用 KMS 密钥加密，还需为该 RAM 角色授予AliyunKMSCryptoUserAccess权限或更精细的 KMS 相关权限。

- 

在[授权](https://ram.console.aliyun.com/permissions)页面，单击新增授权，授权主体选择创建的RAM角色，权限策略选择刚创建的策略，然后单击确认新增授权。

- 

记录角色ARN：在[角色](https://ram.console.aliyun.com/roles)页面找到创建RAM角色，进入基本信息页面，复制角色的ARN用于创建清单规则。格式为acs:ram::{源账号UID}:role/{角色名}。

## 全量清单

全量清单会定期扫描并导出Bucket中所有（或指定前缀下所有）对象的完整列表。请注意：

- 

报告快照：清单报告反映的是扫描任务启动时的对象状态。扫描过程需要时间，此期间的对象变更（如新增、删除）不保证会包含在本次报告中。

- 

首份清单会在配置后立即执行，后续按设置的每日、每周或每月的周期在北京时间凌晨批量执行，导出延迟受对象数量与任务队列影响。

### 配置清单规则

## 控制台

- 

登录[OSS 管理控制台](https://oss.console.aliyun.com/)。

- 

进入需要生成清单的源 Bucket，在左侧导航栏选择数据管理>Bucket 清单。

- 

在Bucket 清单页面，单击创建清单。

- 

在设置清单报告规则面板，配置以下参数：

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 状态 | 设置清单任务的状态，选择 启动 。 |
| 规则名称 | 设置清单任务的名称。只能包含小写字母、数字、短划线（-），且不能以短划线（-）开头或结尾。 |
| 清单报告存储至 | 设置清单报告的存储路径。配置清单的 Bucket 与存放清单 Bucket 必须同账号、同地域。 若需将报告保存到存储空间 examplebucket 的 exampledir1 路径，请填写 exampledir1/ ，指定路径在 Bucket 中不存在时，OSS 会自动创建该路径。 若留空，报告将保存在根目录。 重要 为避免影响 OSS-HDFS 服务的正常使用或者引发数据污染的风险，在开通了 OSS-HDFS 服务的 Bucket 设置清单报告规则时，禁止将清单报告目录填写为 .dlsdata/ 。 |
| 清单文件扫描范围 | 扫描整个 Bucket ：扫描整个 Bucket 的所有文件。 按前缀匹配 ：用于仅扫描指定前缀下的文件，例如 exampledir1/ 。 |
| 清单报告加密选项 | 选择是否加密清单文件。 无 ：不加密。 AES256 ：使用 AES256 加密算法加密清单文件。 KMS ：使用 KMS 密钥加密清单文件，可以选择使用 OSS 托管的 KMS 密钥或在 KMS 平台 [创建一个与目标](products/kms/documents/key-management-service/support/create-a-cmk-1.md) [Bucket](products/kms/documents/key-management-service/support/create-a-cmk-1.md) [相同地域的](products/kms/documents/key-management-service/support/create-a-cmk-1.md) [KMS](products/kms/documents/key-management-service/support/create-a-cmk-1.md) [密钥](products/kms/documents/key-management-service/support/create-a-cmk-1.md) 。 说明 使用 KMS 密钥功能时会产生少量的 KMS 密钥 API 调用费用，费用详情请参考 [KMS 1.0](products/kms/documents/key-management-service/support/billing-of-kms.md) [计费说明](products/kms/documents/key-management-service/support/billing-of-kms.md) 。 |
| 清单报告导出周期 | 设置清单报告的生成周期。可选择 每周、每天、每月、单次导出。 文件数超百亿时，建议选择 每周 以降低成本和扫描压力。 重要 每月 调度周期暂不支持以下地域：华北 3（张家口）、西北 1（中卫）、美国（弗吉尼亚）、美国（硅谷）、墨西哥、法国（巴黎）、 华北 2 金融云、华东 2 金融云、华南 1 金融云、华北 2 阿里政务云 1 |
| 指定日期 | 当导出周期选择 每月 时，可以指定每月第几天启动清单任务。取值范围为 1~31 的正整数。 如果选择 不指定日期 ，默认按 30 天固定频率导出清单。首次启动扫描日期为规则配置当日，此后每隔 30 天导出一次。 指定 1~28 日时，每月在指定日期启动清单任务。 指定 29~31 日时，若当月存在该日期，则在该日期启动；若当月不存在该日期，则在当月最后一天启动。例如，指定每月 31 日，则 4 月在 30 日启动清单任务。 说明 所设置的日期为清单任务启动时间，并非最终的清单文件投递时间。清单生成为异步任务，所需时间取决于 Bucket 内的文件数量，最终的投递时间会晚于所设日期。 |
| 清单内容 | 选择希望导出的文件信息： 系统元数据 ： Object 大小 、 存储类型 、 最后更新日期 、 ETag 、 TransitionTime 、 分片上传状态 、 加密状态 、 文件 ACL 、 文件类型 、 CRC64 、 最后访问时间 、 最后访问时间戳 。 说明 最后访问时间 和 最后访问时间戳 仅在 Bucket 开启 [访问跟踪](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-access-time.md) 的情况下才支持导出。如果关闭访问跟踪后，这两个字段的值不再有含义，通常显示为 null。 自定义元数据 ： 标签个数 |
| 配置高级筛选功能 | 重要 仅华北 1（青岛）、华北 5（呼和浩特）和德国（法兰克福）地域支持配置以下过滤选项。 如果需要根据文件大小、存储类型等条件过滤导出的文件，需要打开 配置高级筛选功能 开关。 支持的过滤选项说明如下： 时间范围 ：设置待导出文件最后一次修改的起始日期和结束日期，时间精确到秒。 文件大小范围 ：设置待导出文件的文件大小最小值和最大值。 重要 设置文件大小范围时，确保文件大小的最小值以及最大值均大于 0 B，且最大值不能超过 48.8 TB。 存储类型 ：设置待导出哪些存储类型的文件。可以选择导出标准存储、低频访问、归档存储、冷归档存储以及深度冷归档存储的文件。 |
| 对象版本 | 若 Bucket 开启了 [版本控制](products/oss/documents/user-guide/overview-78.md) ，可选择导出 当前版本 或 所有版本 。 |


- 

选中我知晓并同意授予阿里云 OSS 服务访问 Bucket 资源的权限，然后单击确定。

涉及Object较多时，生成清单文件需要一定的时间。可以通过两种方式判断是否已生成清单文件，详情请参见[如何判断是否已生成清单文件？](products/oss/documents/how-to-determine-whether-inventory-lists-are-generated.md)。

## SDK

Java

import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; import java.util.ArrayList; import java.util.List; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 填写存放清单结果的Bucket名称。 String destBucketName ="yourDestinationBucketName"; // 填写Bucket所有者授予的账户ID。 String accountId ="yourDestinationBucketAccountId"; // 填写具有读取源Bucket所有文件和向目标Bucket写入文件权限的角色名称。 String roleArn ="yourDestinationBucketRoleArn"; // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .clientConfiguration(clientBuilderConfiguration) .region(region) .build(); try { // 创建清单配置。 InventoryConfiguration inventoryConfiguration = new InventoryConfiguration(); // 设置清单规则名称。 String inventoryId = "testid"; inventoryConfiguration.setInventoryId(inventoryId); // 设置清单中包含的Object属性。 List<String> fields = new ArrayList<String>(); fields.add(InventoryOptionalFields.Size); fields.add(InventoryOptionalFields.LastModifiedDate); fields.add(InventoryOptionalFields.IsMultipartUploaded); fields.add(InventoryOptionalFields.StorageClass); fields.add(InventoryOptionalFields.ETag); fields.add(InventoryOptionalFields.EncryptionStatus); inventoryConfiguration.setOptionalFields(fields); // 设置清单的生成计划，以下示例为每周一次。其中，Weekly表示每周一次，Daily表示每天一次。 inventoryConfiguration.setSchedule(new InventorySchedule().withFrequency(InventoryFrequency.Weekly)); // 设置清单中包含的Object的版本为当前版本。如果设置为InventoryIncludedObjectVersions.All则表示Object的所有版本在版本控制状态下生效。 inventoryConfiguration.setIncludedObjectVersions(InventoryIncludedObjectVersions.Current); // 清单配置是否启用的标识，取值为true或者false，设置为true表示启用清单配置，设置为false表示关闭清单配置。 inventoryConfiguration.setEnabled(true); // 设置清单筛选规则，指定筛选Object的前缀。 InventoryFilter inventoryFilter = new InventoryFilter().withPrefix("obj-prefix"); inventoryConfiguration.setInventoryFilter(inventoryFilter); // 创建存放清单结果的目标Bucket配置。 InventoryOSSBucketDestination ossInvDest = new InventoryOSSBucketDestination(); // 设置存放清单结果的存储路径前缀。 ossInvDest.setPrefix("destination-prefix"); // 设置清单格式。 ossInvDest.setFormat(InventoryFormat.CSV); // 设置目标Bucket的用户accountId。 ossInvDest.setAccountId(accountId); // 设置目标Bucket的roleArn。 ossInvDest.setRoleArn(roleArn); // 设置目标Bucket的名称。 ossInvDest.setBucket(destBucketName); // 如果需要使用KMS加密清单，请参考如下设置。 // InventoryEncryption inventoryEncryption = new InventoryEncryption(); // InventoryServerSideEncryptionKMS serverSideKmsEncryption = new InventoryServerSideEncryptionKMS().withKeyId("test-kms-id"); // inventoryEncryption.setServerSideKmsEncryption(serverSideKmsEncryption); // ossInvDest.setEncryption(inventoryEncryption); // 如果需要使用OSS服务端加密清单，请参考如下设置。 // InventoryEncryption inventoryEncryption = new InventoryEncryption(); // inventoryEncryption.setServerSideOssEncryption(new InventoryServerSideEncryptionOSS()); // ossInvDest.setEncryption(inventoryEncryption); // 设置清单的目的地。 InventoryDestination destination = new InventoryDestination(); destination.setOssBucketDestination(ossInvDest); inventoryConfiguration.setDestination(destination); // 上传清单配置。 ossClient.setBucketInventoryConfiguration(bucketName, inventoryConfiguration); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }

Node.js

const OSS = require('ali-oss'); const client = new OSS({ // yourregion填写Bucket所在地域。以华东1（杭州）为例，Region填写为oss-cn-hangzhou。 region: 'yourregion', // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 accessKeyId: process.env.OSS_ACCESS_KEY_ID, accessKeySecret: process.env.OSS_ACCESS_KEY_SECRET, // 填写存储空间名称。 bucket: 'yourbucketname' }); const inventory = { // 设置清单配置ID。 id: 'default', // 清单配置是否启用的标识，取值为true或false。 isEnabled: false, //（可选）设置清单筛选规则，指定筛选object的前缀。 prefix: 'ttt', OSSBucketDestination: { // 设置清单格式。 format: 'CSV', // 目标Bucket拥有者的账号ID。 accountId: '<Your AccountId>', // 目标Bucket的角色名称。 rolename: 'AliyunOSSRole', // 目标Bucket的名称。 bucket: '<Your BucketName>', //（可选）清单结果的存储路径前缀。 prefix: '<Your Prefix>', // 如果需要使用SSE-OSS加密清单，请参考以下代码。 //encryption: {'SSE-OSS': ''}, // 如果需要使用SSE-KMS加密清单，请参考以下代码。 /* encryption: { 'SSE-KMS': { keyId: 'test-kms-id', };, */ }, // 设置清单的生成计划，WEEKLY对应每周一次，DAILY对应每天一次。 frequency: 'Daily', // 设置清单结果中包含了Object的所有版本, 如果设置为Current，则表示仅包含Object的当前版本。 includedObjectVersions: 'All', optionalFields: { //（可选）设置清单中包含的Object属性。 field: ["Size", "LastModifiedDate", "ETag", "StorageClass", "IsMultipartUploaded", "EncryptionStatus"] }, } async function putInventory(){ // 需要添加清单配置的Bucket名称。 const bucket = '<Your BucketName>'; try { await client.putBucketInventory(bucket, inventory); console.log('清单配置添加成功') } catch(err) { console.log('清单配置添加失败: ', err); } } putInventory()

Python

import argparse import alibabacloud_oss_v2 as oss # 创建命令行参数解析器，并描述脚本用途：设置存储空间清单（Inventory） parser = argparse.ArgumentParser(description="put bucket inventory sample") # 定义命令行参数，包括必需的区域、存储空间名称、endpoint、用户ID、角色ARN以及清单名称 parser.add_argument('--region', help='The region in which the bucket is located.', required=True) parser.add_argument('--bucket', help='The name of the bucket.', required=True) parser.add_argument('--endpoint', help='The domain names that other services can use to access OSS') parser.add_argument('--user_id', help='User account ID.', required=True) parser.add_argument('--arn', help='The Alibaba Cloud Resource Name (ARN) of the role that has the permissions to read all objects from the source bucket and write objects to the destination bucket. Format: `acs:ram::uid:role/rolename`.', required=True) parser.add_argument('--inventory_id', help='The name of the inventory.', required=True) def main(): # 解析命令行参数，获取用户输入的值 args = parser.parse_args() # 从环境变量中加载访问凭证信息，用于身份验证 credentials_provider = oss.credentials.EnvironmentVariableCredentialsProvider() # 使用SDK默认配置创建配置对象，并设置认证提供者 cfg = oss.config.load_default() cfg.credentials_provider = credentials_provider # 设置配置对象的区域属性，根据用户提供的命令行参数 cfg.region = args.region # 如果提供了自定义endpoint，则更新配置对象中的endpoint属性 if args.endpoint is not None: cfg.endpoint = args.endpoint # 使用上述配置初始化OSS客户端，准备与OSS交互 client = oss.Client(cfg) # 发送请求以配置指定存储空间的清单设置 result = client.put_bucket_inventory(oss.PutBucketInventoryRequest( bucket=args.bucket, # 存储空间名 inventory_id=args.inventory_id, # 存储空间清单ID inventory_configuration=oss.InventoryConfiguration( included_object_versions='All', # 包含所有版本的对象 optional_fields=oss.OptionalFields( fields=[ # 可选字段，如大小和最后修改日期 oss.InventoryOptionalFieldType.SIZE, oss.InventoryOptionalFieldType.LAST_MODIFIED_DATE, ], ), id=args.inventory_id, # 存储空间清单ID is_enabled=True, # 启用存储空间清单 destination=oss.InventoryDestination( oss_bucket_destination=oss.InventoryOSSBucketDestination( format=oss.InventoryFormatType.CSV, # 输出格式为CSV account_id=args.user_id, # 用户账户ID role_arn=args.arn, # 角色ARN，具有读取源存储空间和写入目标存储空间的权限 bucket=f'acs:oss:::{args.bucket}', # 目标存储空间 prefix='aaa', # 清单文件前缀 ), ), schedule=oss.InventorySchedule( frequency=oss.InventoryFrequencyType.DAILY, # 清单频率，这里设置为每天 ), filter=oss.InventoryFilter( lower_size_bound=1024, # 对象大小下限（字节） upper_size_bound=1048576, # 对象大小上限（字节） storage_class='ColdArchive', # 存储类别筛选条件 prefix='aaa', # 对象前缀筛选条件 last_modify_begin_time_stamp=1637883649, # 最后修改时间戳开始范围 last_modify_end_time_stamp=1638347592, # 最后修改时间戳结束范围 ), ), )) # 打印操作结果的状态码和请求ID，以便确认请求状态 print(f'status code: {result.status_code},' f' request id: {result.request_id},' ) # 当此脚本被直接执行时，调用main函数开始处理逻辑 if __name__ == "__main__": main() # 脚本入口点，控制程序流程从这里开始

C#

using Aliyun.OSS; using Aliyun.OSS.Common; // yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。 var endpoint = "yourEndpoint"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 var accessKeyId = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_ID"); var accessKeySecret = Environment.GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET"); // 填写Bucket名称。 var bucketName = "examplebucket"; // 填写Bucket所有者授予的账户ID。 var accountId ="yourDestinationBucketAccountId"; // 填写具有读取源Bucket所有文件和向目标Bucket写入文件权限的角色名称。 var roleArn ="yourDestinationBucketRoleArn"; // 填写存放清单结果的Bucket名称。 var destBucketName ="yourDestinationBucketName"; // 填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。 const string region = "cn-hangzhou"; // 创建ClientConfiguration实例，按照您的需要修改默认参数。 var conf = new ClientConfiguration(); // 设置v4签名。 conf.SignatureVersion = SignatureVersion.V4; // 创建OssClient实例。 var client = new OssClient(endpoint, accessKeyId, accessKeySecret, conf); client.SetRegion(region); try { // 添加Bucket清单。 var config = new InventoryConfiguration(); // 设置清单规则名称。 config.Id = "report1"; // 清单配置是否启用的标识，取值为true或false。设置为true，表示启用清单配置。 config.IsEnabled = true; // 设置清单筛选规则，指定筛选Object的前缀。 config.Filter = new InventoryFilter("filterPrefix"); // 创建清单的bucket目的地配置。 config.Destination = new InventoryDestination(); config.Destination.OSSBucketDestination = new InventoryOSSBucketDestination(); // 设置清单格式。 config.Destination.OSSBucketDestination.Format = InventoryFormat.CSV; // 存放清单结果的目标Bucket的用户accountId。 config.Destination.OSSBucketDestination.AccountId = accountId; // 存放清单结果的目标Bucket的roleArn。 config.Destination.OSSBucketDestination.RoleArn = roleArn; // 存放清单结果的目标Bucket名称。 config.Destination.OSSBucketDestination.Bucket = destBucketName; // 设置存放清单结果的存储路径前缀。 config.Destination.OSSBucketDestination.Prefix = "prefix1"; // 设置清单的生成计划，以下示例为每周一次。其中，Weekly对应每周一次，Daily对应每天一次。 config.Schedule = new InventorySchedule(InventoryFrequency.Daily); // 设置清单中包含的object的版本为当前版本。如果设置为InventoryIncludedObjectVersions.All则表示object的所有版本，在版本控制状态下生效。 config.IncludedObjectVersions = InventoryIncludedObjectVersions.All; // 设置清单中包含的Object属性。 config.OptionalFields.Add(InventoryOptionalField.Size); config.OptionalFields.Add(InventoryOptionalField.LastModifiedDate); config.OptionalFields.Add(InventoryOptionalField.StorageClass); config.OptionalFields.Add(InventoryOptionalField.IsMultipartUploaded); config.OptionalFields.Add(InventoryOptionalField.EncryptionStatus); config.OptionalFields.Add(InventoryOptionalField.ETag); var req = new SetBucketInventoryConfigurationRequest(bucketName, config); client.SetBucketInventoryConfiguration(req); Console.WriteLine("Set bucket:{0} InventoryConfiguration succeeded", bucketName); } catch (OssException ex) { Console.WriteLine("Failed with error code: {0}; Error info: {1}. \nRequestID:{2}\tHostID:{3}", ex.ErrorCode, ex.Message, ex.RequestId, ex.HostId); }

C++

#include <alibabacloud/oss/OssClient.h> using namespace AlibabaCloud::OSS; int main(void) { /* 初始化OSS账号信息。*/ /* yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。*/ std::string Endpoint = "yourEndpoint"; /* yourRegion填写Bucket所在地域对应的Region。以华东1（杭州）为例，Region填写为cn-hangzhou。*/ std::string Region = "yourRegion"; /* 填写Bucket名称，例如examplebucket。*/ std::string BucketName = "examplebucket"; /* 初始化网络等资源。*/ InitializeSdk(); ClientConfiguration conf; conf.signatureVersion = SignatureVersionType::V4; /* 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。*/ auto credentialsProvider = std::make_shared<EnvironmentVariableCredentialsProvider>(); OssClient client(Endpoint, credentialsProvider, conf); client.SetRegion(Region); InventoryConfiguration inventoryConf; /* 指定清单规则名称，该名称在当前Bucket下必须全局唯一。*/ inventoryConf.setId("inventoryId"); /* 清单配置是否启用的标识，可选值为true或false。*/ inventoryConf.setIsEnabled(true); /* (可选)清单筛选的前缀。指定前缀后，清单将筛选出符合前缀的Object。*/ inventoryConf.setFilter(InventoryFilter("objectPrefix")); InventoryOSSBucketDestination dest; /* 导出清单文件的文件格式。*/ dest.setFormat(InventoryFormat::CSV); /* 存储空间拥有者的账户UID。*/ dest.setAccountId("10988548********"); /* 指定角色名称，该角色需要拥有读取源存储空间所有文件以及向目标存储空间写入文件的权限，格式为acs:ram::uid:role/rolename。*/ dest.setRoleArn("acs:ram::10988548********:role/inventory-test"); /* 存放导出的清单文件的存储空间。*/ dest.setBucket("yourDstBucketName"); /* 清单文件的存储路径前缀。*/ dest.setPrefix("yourPrefix"); /* (可选)清单文件的加密方式, 可选SSEOSS或者SSEKMS方式加密。*/ //dest.setEncryption(InventoryEncryption(InventorySSEOSS())); //dest.setEncryption(InventoryEncryption(InventorySSEKMS("yourKmskeyId"))); inventoryConf.setDestination(dest); /* 清单文件导出的周期, 可选为Daily或者Weekly。*/ inventoryConf.setSchedule(InventoryFrequency::Daily); /* 是否在清单中包含Object版本信息, 可选为All或者Current。*/ inventoryConf.setIncludedObjectVersions(InventoryIncludedObjectVersions::All); /* (可选)设置清单结果中应包含的配置项, 请按需配置。*/ InventoryOptionalFields field { InventoryOptionalField::Size, InventoryOptionalField::LastModifiedDate, InventoryOptionalField::ETag, InventoryOptionalField::StorageClass, InventoryOptionalField::IsMultipartUploaded, InventoryOptionalField::EncryptionStatus }; inventoryConf.setOptionalFields(field); /* 设置清单配置。*/ auto outcome = client.SetBucketInventoryConfiguration( SetBucketInventoryConfigurationRequest(BucketName, inventoryConf)); if (!outcome.isSuccess()) { /* 异常处理。*/ std::cout << "Set Bucket Inventory fail" << ",code:" << outcome.error().Code() << ",message:" << outcome.error().Message() << ",requestId:" << outcome.error().RequestId() << std::endl; return -1; } /* 释放网络等资源。*/ ShutdownSdk(); return 0; }

package main import ( "context" "flag" "log" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss" "github.com/aliyun/alibabacloud-oss-go-sdk-v2/oss/credentials" ) // 定义全局变量 var ( region string // 存储区域 bucketName string // 存储空间名称 ) // init函数用于初始化命令行参数 func init() { flag.StringVar(&region, "region", "", "The region in which the bucket is located.") flag.StringVar(&bucketName, "bucket", "", "The name of the bucket.") } func main() { // 解析命令行参数 flag.Parse() var ( accountId = "account id of the bucket" // 存储空间所有者授予的账户ID，例如109885487000**** inventoryId = "inventory id" // 由用户指定的清单名称，清单名称在当前Bucket下必须全局唯一 ) // 检查bucket名称是否为空 if len(bucketName) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, bucket name required") } // 检查region是否为空 if len(region) == 0 { flag.PrintDefaults() log.Fatalf("invalid parameters, region required") } // 加载默认配置并设置凭证提供者和区域 cfg := oss.LoadDefaultConfig(). WithCredentialsProvider(credentials.NewEnvironmentVariableCredentialsProvider()). WithRegion(region) // 创建OSS客户端 client := oss.NewClient(cfg) // 创建设置存储空间清单的请求 putRequest := &oss.PutBucketInventoryRequest{ Bucket: oss.Ptr(bucketName), // 存储空间名称 InventoryId: oss.Ptr(inventoryId), // 由用户指定的清单名称 InventoryConfiguration: &oss.InventoryConfiguration{ Id: oss.Ptr(inventoryId), // 由用户指定的清单名称 IsEnabled: oss.Ptr(true), // 启用清单配置 Filter: &oss.InventoryFilter{ Prefix: oss.Ptr("filterPrefix"), // 设置清单筛选规则，指定筛选Object的前缀 LastModifyBeginTimeStamp: oss.Ptr(int64(1637883649)), // 最后修改开始时间戳 LastModifyEndTimeStamp: oss.Ptr(int64(1638347592)), // 最后修改结束时间戳 LowerSizeBound: oss.Ptr(int64(1024)), // 文件大小下限（字节） UpperSizeBound: oss.Ptr(int64(1048576)), // 文件大小上限（字节） StorageClass: oss.Ptr("Standard,IA"), // 存储类型 }, Destination: &oss.InventoryDestination{ OSSBucketDestination: &oss.InventoryOSSBucketDestination{ Format: oss.InventoryFormatCSV, // 导出清单文件的文件格式 AccountId: oss.Ptr(accountId), // 存储空间所有者授予的账户ID，例如109885487000**** RoleArn: oss.Ptr("acs:ram::" + accountId + ":role/AliyunOSSRole"), // 存储空间所有者授予操作权限的角色名，比如acs:ram::109885487000****:role/ram-test Bucket: oss.Ptr("acs:oss:::" + bucketName), // 存放导出的清单结果的Bucket名称 Prefix: oss.Ptr("export/"), // 存放清单结果的存储路径前缀 }, }, Schedule: &oss.InventorySchedule{ Frequency: oss.InventoryFrequencyDaily, // 清单文件导出的周期（每天） }, IncludedObjectVersions: oss.Ptr("All"), // 是否在清单中包含Object的所有版本信息 }, } // 执行设置存储空间清单的请求 putResult, err := client.PutBucketInventory(context.TODO(), putRequest) if err != nil { log.Fatalf("failed to put bucket inventory %v", err) } // 打印设置存储空间清单的结果 log.Printf("put bucket inventory result:%#v\n", putResult) }

## ossutil

创建一个名为inventory-configuration.xml的文件，内容如下：

<?xml version="1.0" encoding="UTF-8"?> <InventoryConfiguration> <Id>report1</Id> <IsEnabled>true</IsEnabled> <Destination> <OSSBucketDestination> <Format>CSV</Format> <AccountId>100000000000000</AccountId> <RoleArn>acs:ram::100000000000000:role/AliyunOSSRole</RoleArn> <Bucket>acs:oss:::destbucket</Bucket> <Prefix>prefix1/</Prefix> <Encryption> <SSE-KMS> <KeyId>keyId</KeyId> </SSE-KMS> </Encryption> </OSSBucketDestination> </Destination> <Schedule> <Frequency>Daily</Frequency> </Schedule> <IncludedObjectVersions>All</IncludedObjectVersions> <OptionalFields> <Field>Size</Field> <Field>LastModifiedDate</Field> <Field>ETag</Field> <Field>StorageClass</Field> <Field>IsMultipartUploaded</Field> <Field>EncryptionStatus</Field> </OptionalFields> </InventoryConfiguration>

执行以下命令：

ossutil api put-bucket-inventory --bucket examplebucket --inventory-id report1 --inventory-configuration file://inventory-configuration.xml

注意：关于put-bucket-inventory命令的详细用法，请参考[put-bucket-inventory](products/oss/documents/developer-reference/put-bucket-inventory.md)。

## API

可直接调用[PutBucketInventory](products/oss/documents/developer-reference/putbucketinventory.md)来配置或修改清单规则。需要手动构造 HTTP 请求并计算签名，适用于对流程有高度自定义需求的场景。

### 解析清单报告

清单任务以异步方式执行。清单报告的所有文件都存储在一个以扫描启动时间命名的文件夹中。核心文件包括manifest.json和data/目录下的.csv.gz数据文件。要确认任务是否完成，可以检查目标是否已生成manifest.json文件。

- 

读取manifest.json文件：解析manifest.json文件以获取正确的列顺序和数据文件信息，重点关注以下两个字段：

- 

fileSchema：字符串类型，定义了 CSV 文件中各列的名称和确切顺序。

- 

files：数组类型，列出了本次报告生成的所有.csv.gz数据文件的详细信息，包括：

- 

key：文件路径

- 

size：文件大小

- 

MD5checksum：MD5 校验值

- 

根据fileSchema解析 CSV 数据文件

- 

获取并解压数据文件：从manifest.json的files数组中获取每个数据文件的key（即文件路径）。根据该路径下载对应的.csv.gz压缩包。解压文件，得到 CSV 格式的数据。

- 

按序解析数据：

以fileSchema字段中定义的顺序作为 CSV 文件的列标题。逐行读取解压后的 CSV 文件。每一行代表一个对象（文件）的完整记录，每一列则对应fileSchema中指定的一个字段。

CSV 内容示例：如果fileSchema为"Bucket,Key,Size,StorageClass,LastModifiedDate"，解压后的 CSV 内容格式如下：

source-bucket,"dir%2Fbody.xml","102400","Standard","2025-04-14T07-06-00Z" source-bucket,"dest.png","312049","Standard","2025-04-14T07-05-59Z"Key 使用URL编码，可按需解码。

### 全量清单文件

清单任务配置完成后，OSS会按清单规则指定的导出周期生成清单文件。清单文件的目录结构如下：

<dest-bucket-name>/ └── <dest-prefix>/ └── <source-bucket-name>/ └── <inventory-id>/ ├── YYYY-MM-DDTHH-MMZ/ (扫描开始的UTC时间) │ ├── manifest.json (清单任务的元数据文件) │ └── manifest.checksum (manifest.json 文件的 MD5 校验和) └── data/ └── <uuid>.csv.gz (多份GZIP 压缩的清单数据文件)

- 

- 

| 目录结构 | 说明 |
| --- | --- |
| dest-prefix | 该目录根据设置的清单报告名前缀生成，如果清单报告名前缀设置为空，将省略该目录。 |
| source-bucket-name | 该目录根据配置清单报告的源 Bucket 名生成。 |
| inventory_id | 该目录根据清单任务的规则名称生成。 |
| YYYY-MM-DDTHH-MMZ | 该目录是标准的格林威治时间戳，表示开始扫描 Bucket 的时间，例如 2025-05-17T16-00Z。该目录下包含了 manifest.json 和 manifest.checksum 文件。 |
| data | 该目录下存放了包含源 Bucket 中的对象列表以及每个对象的元数据的清单文件，清单文件格式为使用 GZIP 压缩的 CSV 文件。 重要 当导出的源 Bucket 中 Object 数量较多时，为方便用户下载和处理数据，程序会自动将清单文件切分成多个 CSV 压缩文件。CSV 压缩文件按照 uuid.csv.gz 、 uuid-1.csv.gz 、 uuid-2.csv.gz 的顺序依次递增。可以从 manifest.json 文件中获取 CSV 文件列表，然后按照以上顺序依次解压 CSV 文件并读取清单数据。 Object 的单条记录信息仅出现在一个清单文件内，不会分布到不同的清单文件。 |


manifest文件

manifest文件包含manifest.json和manifest.checksum，详细说明如下：

- 

manifest.json：提供了有关清单的元数据和其他基本信息。

{ "creationTimestamp": "1642994594", "destinationBucket": "dest-bucket-name", "fileFormat": "CSV", "fileSchema": "Bucket, Key, VersionId, IsLatest, IsDeleteMarker, Size, StorageClass, LastModifiedDate, ETag, IsMultipartUploaded, EncryptionStatus, ObjectAcl, TaggingCount, ObjectType, CRC64", "files": [{ "MD5checksum": "F77449179760C3B13F1E76110F07****", "key": "dest-prefix/source-bucket-name/inventory-id/data/a1574226-b5e5-40ee-91df-356845777c04.csv.gz", "size": 2046}], "sourceBucket": "source-bucket-name", "version": "2019-09-01" }

各字段详细说明如下：

- 

- 

| 字段名称 | 说明 |
| --- | --- |
| creationTimestamp | 时间戳，显示开始扫描源 Bucket 的时间。 |
| destinationBucket | 存放清单文件的目标 Bucket。 |
| fileFormat | 清单文件的格式。 |
| fileSchema | 清单文件包含的字段，分为固定字段和可选字段。其中，固定字段的顺序是固定的，可选字段的排列顺序取决于配置清单规则时清单内容字段的排列顺序（控制台配置时以字段的勾选先后顺序为准）。 因此，建议以 fileSchema 中的字段顺序去解析 csv.gz 中的数据列，避免出现列和属性对应错误的情况。 配置清单规则时如果对象版本选择了当前版本，则 fileSchema 中，先排列固定字段 Bucket, Key ，后续为可选字段。 配置清单规则时如果对象版本选择了所有版本，则 fileSchema 中，先排列固定字段 Bucket, Key, VersionId, IsLatest, IsDeleteMarker ，后续为可选字段。 |
| files | 包含清单文件的 MD5 值、文件名完整路径及文件大小。 |
| sourceBucket | 配置清单规则的源 Bucket。 |
| version | 清单版本号。 |


- 

manifest.checksum：manifest.checksum文件包含了manifest.json文件的 MD5 哈希值，可用于校验manifest.json文件的完整性，例如F77449179760C3B13F1E76110F07****。

全量清单报告

清单报告存储在data/目录中，包含清单功能导出的文件信息。清单报告示例如下：

- 

- 

- 

- 

- 

- 

- 

- 

| 字段名称 | 说明 |
| --- | --- |
| Bucket | 执行清单任务的源 Bucket 名称。 |
| Key | Bucket 中 Object 的名称。 Object 名称使用 URL 编码，可按需解码。 |
| VersionId | Object 的版本 ID。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段显示为空。 如果配置清单规则的 Bucket 已开启版本控制，则该字段显示为 Object 的 VersionId。 |
| IsLatest | Object 版本是否为最新版本。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段显示为 true 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为最新版本时，则该字段显示为 true 。如果 Object 为历史版本，则该字段显示为 false。 |
| IsDeleteMarker | Object 版本是否为删除标记。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段默认显示为 false 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为删除标记时，则该字段显示为 true 。如果 Object 不是删除标记，则该字段显示为 false 。 |
| Size | Object 大小。 |
| StorageClass | Object 的存储类型。 |
| LastModifiedDate | Object 的最后修改时间，格式是格林威治时间，与北京时间相差 8 小时。 |
| TransistionTime | Object 通过生命周期规则转储为冷归档或者深度冷归档存储类型的时间。 |
| ETag | Object 的 ETag。 Object 生成时会创建相应的 ETag，用于标识一个 Object 的内容。 通过 [PutObject](products/oss/documents/developer-reference/putobject.md) 接口创建的 Object，ETag 值是其内容的 MD5 值。 通过其他方式创建的 Object，ETag 值是基于一定计算规则生成的唯一值，但不是其内容的 MD5 值。 |
| IsMultipartUploaded | Object 是否通过分片上传生成。如果是，则该字段值为 true ，否则为 false 。 |
| EncryptionStatus | Object 是否已加密。若 Object 已加密，则该字段值为 true ，否则为 false 。 |
| ObjectAcl | Object 的读写权限。更多信息，请参见 [Object ACL](products/oss/documents/user-guide/object-acl.md) 。 |
| TaggingCount | Object 的标签个数。 |
| ObjectType | Object 类型。更多信息，请参见 [Object](products/oss/documents/user-guide/object-overview.md) [类型](products/oss/documents/user-guide/object-overview.md) 。 |
| Crc64 | Object 的 CRC64。 |
| LastAccessDate | Object 的最后访问时间，格式是格林威治时间，与北京时间相差 8 小时。 说明 仅在 Bucket 开启 [访问跟踪](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-access-time.md) 的情况下才支持导出。如果关闭访问跟踪后，该字段的值不再有含义，通常显示为 null。 |
| LastAccessTimestamp | Object 的最后访问时间戳（Unix 时间戳）。 说明 仅在 Bucket 开启 [访问跟踪](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-access-time.md) 的情况下才支持导出。如果关闭访问跟踪后，该字段的值不再有含义，通常显示为 null。 |


## 增量清单

增量清单通常以10分钟为周期，捕获并报告该时间窗口内发生的所有对象变更事件（包括创建、元数据更新、删除）。

### 配置清单规则

## 控制台

- 

登录[OSS 管理控制台](https://oss.console.aliyun.com/)。

- 

进入需要生成清单的源 Bucket，在左侧导航栏选择数据管理>Bucket 清单。

- 

在Bucket 清单页面，单击创建清单。

- 

在设置清单报告规则面板。

- 

配置基础设置参数：

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 状态 | 设置增量清单任务的状态，选择 启动 。 |
| 规则名称 | 设置清单任务的名称。只能包含小写字母、数字、短划线（-），且不能以短划线（-）开头或结尾。 |
| 清单报告存储至 | 设置清单报告的存储路径。配置清单的 Bucket 与存放清单 Bucket 必须同账号、同地域。 若需将报告保存到存储空间 examplebucket 的 exampledir1 路径，请填写 exampledir1/ ，指定路径在 Bucket 中不存在时，OSS 会自动创建该路径。目标路径前缀的长度不能超过 128 个字符。 若留空，报告将保存在根目录。 重要 为避免影响 OSS-HDFS 服务的正常使用或者引发数据污染的风险，在开通了 OSS-HDFS 服务的 Bucket 设置清单报告规则时，禁止将清单报告目录填写为 .dlsdata/ 。 |
| 清单文件扫描范围 | 扫描整个 Bucket ：扫描整个 Bucket 的所有文件。 按前缀匹配 ：用于仅扫描指定前缀下的文件，例如 exampledir1/ 。 |


- 

在追踪并生成增量元数据更新区域，开启获取增量元数据更新，并根据需要选择希望导出的元数据字段。

- 

- 

| 参数 | 说明 |
| --- | --- |
| 元数据字段 | 选择希望导出的文件信息。 事件元数据 ： 序列号 、 事件类型 、 时间戳 、 用户 ID 、 请求 ID 、 请求源 IP 。 系统元数据 ： Object 大小 、 存储类型 、 最后更新日期 、 ETag 、 分片上传状态 、 文件类型、文件 ACL 、 CRC64 、 加密状态 。 |


- 

选中我知晓并同意授予阿里云 OSS 服务访问 Bucket 资源的权限，然后单击确定。

## ossutil

创建一个名为incremental-inventory.xml的文件。与全量清单配置相比，关键在于增加了<IncrementalInventory>节。

<?xml version="1.0" encoding="UTF-8"?> <InventoryConfiguration> <Id>Report-1</Id> <IsEnabled>true</IsEnabled> <Filter> <Prefix>test</Prefix> </Filter> <Destination> <OSSBucketDestination> <Format>CSV</Format> <AccountId>12xxxxxx29</AccountId> <RoleArn>acs:ram::12xxxxxx29:role/AliyunOSSRole</RoleArn> <Bucket>acs:oss:::test-inc-bi-bj</Bucket> <Prefix>Report-1</Prefix> </OSSBucketDestination> </Destination> <Schedule> <Frequency>Weekly</Frequency> </Schedule> <IncludedObjectVersions>All</IncludedObjectVersions> <OptionalFields> <Field>Size</Field> <Field>LastModifiedDate</Field> <Field>ETag</Field> <Field>StorageClass</Field> </OptionalFields> <IncrementalInventory> <IsEnabled>true</IsEnabled> <Schedule> <Frequency>600</Frequency> </Schedule> <OptionalFields> <Field>SequenceNumber</Field> <Field>RecordType</Field> <Field>RecordTimestamp</Field> <Field>Requester</Field> <Field>RequestId</Field> <Field>SourceIp</Field> <Field>Size</Field> <Field>StorageClass</Field> <Field>LastModifiedDate</Field> <Field>ETag</Field> <Field>IsMultipartUploaded</Field> <Field>ObjectType</Field> <Field>ObjectAcl</Field> <Field>Crc64</Field> <Field>EncryptionStatus</Field> </OptionalFields> </IncrementalInventory> </InventoryConfiguration>

执行以下命令：

ossutil api put-bucket-inventory --bucket examplebucket --inventory-id report1 --inventory-configuration file://inventory-configuration.xml注意：关于put-bucket-inventory命令的详细用法，请参考[put-bucket-inventory](products/oss/documents/developer-reference/put-bucket-inventory.md)。

## API

可直接调用[PutBucketInventory](products/oss/documents/developer-reference/putbucketinventory.md)来配置或修改清单规则。这需要手动构造 HTTP 请求并计算签名，适用于对流程有高度自定义需求的场景。

### 解析清单报告

清单任务完成后，会在目标 Bucket 的指定路径下生成报告文件，核心包括：

- 

manifest.json文件

- 

data/目录下的.csv数据文件

判断任务是否已完成，可以检查目标 Bucket 中是否生成了manifest.json文件。

解析步骤如下：

- 

读取manifest.json文件：清单报告的列顺序是动态的，取决于配置清单规则时所勾选的字段。需要先解析manifest.json中的fileSchema字段，该字段定义了 CSV 文件中各列的名称及其顺序。

- 

根据fileSchema解析 CSV 数据文件

- 

以fileSchema中定义的顺序作为 CSV 文件的列标题。

- 

按行读取 CSV 文件：每一行代表一个对象（文件）的完整记录，每一列对应fileSchema中声明的一个字段。

### 增量清单文件

清单任务配置完成后，OSS会按清单规则指定的导出周期生成清单文件。清单文件的目录结构如下：

<dest-bucket-name>/ └── <dest-prefix>/ └── <source-bucket-name>/ └── <inventory-id>/ └── incremental_inventory/ └── YYYY-MM-DDTHH-MMSSZ/ ├── manifest.json └── data/ ├── uuid1_0.csv └── ......

| 目录结构 | 说明 |
| --- | --- |
| dest-prefix | 该目录根据设置的清单报告名前缀生成，如果清单报告名前缀设置为空，将省略该目录。 |
| source-bucket-name | 该目录根据配置清单报告的源 Bucket 名生成。 |
| inventory_id | 该目录根据清单任务的规则名称生成。 |
| incremental_inventory | 增量清单的固定前缀（区分全量导出结果）。 |
| YYYY-MM-DDTHH-MMSSZ | 该目录是标准的格林威治时间戳，表示开始扫描 Bucket 的时间，例如 2020-05-17T16-0000Z。 |
| data | 该目录下存放的是在指定时间周期内，源 Bucket 中发生修改的对象及其元数据的清单文件，清单文件格式为 CSV 文件。 |


manifest文件{ "startTimestamp": "1759320000", "endTimestamp": "1759320600", "destinationBucket": "destbucket", "fileFormat": "CSV", "fileSchema": "Bucket, Key, VersionId, IsDeleteMarker, SequenceNumber, RecordType, RecordTimestamp, Requester, RequestId, SourceIp, Size, StorageClass, LastModifiedDate, ETag, IsMultipartUploaded, ObjectType, ObjectAcl, CRC64, EncryptionStatus", "files": [{ "MD5checksum": "60463A9A34019CF448A730EB2CB3****", "key": "dest-prefix/source-bucket-name/inventory-id/incremental_inventory/2025-09-28T07-4000Z/data/5b7c6cf0db490db906c60e87b917b148_5550506986a37a62abce56a83db6736d_0.csv", "size": 2046}], "sourceBucket": "srcbucket", "version": "2025-09-30" }

各字段详细说明如下：

- 

- 

| 字段名称 | 说明 |
| --- | --- |
| startTimestamp | 时间戳，增量清单统计开始时间。 |
| endTimestamp | 时间戳，增量清单统计结束时间。 |
| destinationBucket | 存放清单文件的目标 Bucket。 |
| fileFormat | 清单文件的格式。 |
| fileSchema | 清单文件包含的字段，分为固定字段和可选字段。其中，固定字段的顺序是固定的，可选字段的排列顺序取决于配置清单规则时清单内容字段的排列顺序（控制台配置时以字段的勾选先后顺序为准）。 因此，建议以 fileSchema 中的字段顺序去解析 csv.gz 中的数据列，避免出现列和属性对应错误的情况。 配置清单规则时如果对象版本选择了当前版本，则 fileSchema 中，先排列固定字段 Bucket, Key ，后续为可选字段。 配置清单规则时如果对象版本选择了所有版本，则 fileSchema 中，先排列固定字段 Bucket, Key, VersionId, IsDeleteMarker ，后续为可选字段。 |
| files | 包含清单文件的 MD5 值、文件名完整路径及文件大小。 |
| sourceBucket | 配置清单规则的源 Bucket。 |
| version | 清单版本号。 |


增量清单报告字段

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 元数据类型 | 字段名称 | 说明 |
| --- | --- | --- |
| System Metadata | Bucket | 执行清单任务的源 Bucket 名称。 |
| Event Metadata | SequenceNumber | 序列号，每条记录的 SequenceNumber 唯一，同 Bucket 同 Object 下的记录，可按照 SequenceNumber 排序，通常保证排序后的记录遵循时间逻辑顺序。 |
| RecordType | 事件类型：CREATE、UPDATE_METADATA、DELETE CREATE：所选前缀下发生的所有上传方式，如 Put/Post/Append/MultipartUpload/Copy UPDATE_METADATA：所选前缀下所有元数据的更新都记录在该类型中 DELETE：所选前缀下的文件的所有删除方式，如 DeleteObject/DeleteMultipleObjects、开启多版本后生成 DeleteMarker、生命周期删除。删除有 DeleteMarker 和永久删除，其中，永久删除记录仅保留 Bucket 、 Key 、 SequenceNumber 、 RecordType 、 RecordTimestamp 和 VersionId 核心字段，其余列均为空（null）。 |  |
| RecordTimestamp | 时间戳 ( 示例："2024-08-25 18:08:01.024")，采用格林威治时区，精度到毫秒。 |  |
| Requester | 请求者的阿里云 ID 或者 Principal ID。 |  |
| RequestId | 请求的唯一标识。 |  |
| SourceIp | 请求者源 IP。 |  |
| System Metadata | Key | Bucket 中 Object 的名称，采用 URL 编码。 |
| VersionId | Object 的版本 ID。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段显示为空。 如果配置清单规则的 Bucket 已开启版本控制，则该字段显示为 Object 的 VersionId。 |  |
| IsDeleteMarker | Object 版本是否为删除标记。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段默认显示为 false 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为删除标记时，则该字段显示为 true 。如果 Object 不是删除标记，则该字段显示为 false 。 |  |
| Size | Object 大小。 |  |
| StorageClass | Object 的存储类型。 |  |
| LastModifiedDate | Object 的最后修改时间，格式是格林威治时间，与北京时间相差 8 小时。 |  |
| ETag | Object 的 ETag。Object 生成时会创建相应的 ETag，用于标识一个 Object 的内容。 通过 [PutObject](products/oss/documents/developer-reference/putobject.md) 接口创建的 Object，ETag 值是其内容的 MD5 值。 通过其他方式创建的 Object，ETag 值是基于一定计算规则生成的唯一值，但不是其内容的 MD5 值。 |  |
| IsMultipartUploaded | Object 是否通过分片上传生成。如果是，则该字段值为 true ，否则为 false 。 |  |
| EncryptionStatus | Object 是否已加密。若 Object 已加密，则该字段值为 true ，否则为 false 。 |  |
| ObjectAcl | Object 的读写权限。更多信息，请参见 [Object ACL](products/oss/documents/user-guide/object-acl.md) 。 |  |
| ObjectType | Object 类型。更多信息，请参见 [Object](products/oss/documents/user-guide/object-overview.md) [类型](products/oss/documents/user-guide/object-overview.md) 。 |  |
| Crc64 | Object 的 CRC64。 |  |


## 配额与限制

单个 Bucket 最多支持 1000 条清单规则（通过 API/SDK）或 10 条（通过控制台）。

## 计费说明

存储空间清单暂不收取功能使用费，但会产生以下关联费用：

- 

API 请求费：配置和获取清单规则时产生Put请求费用和Get请求费用。OSS 写入清单报告到目标 Bucket 时会产生 PUT 请求费用。下载和读取清单报告时，会产生 GET 请求费用。

- 

存储费用：生成的清单报告（manifest文件和csv.gz、csv文件）会占用目标 Bucket 的存储空间，按标准存储费用计费。

- 

外网流出费用：使用外网 Endpoint 下载和读取清单报告时，会产生外网流出流量费用。

- 

为避免不必要的开销，请及时删除不再需要的清单规则，并使用生命周期规则自动清理过期的清单报告文件。

## 应用于生产环境

### 最佳实践

- 

最小权限：始终使用专用的、具备最小权限的 RAM 角色，切勿在生产环境中使用AliyunOSSRole。

- 

性能建议：对于高流量的源 Bucket，应将清单报告存储到另一个专用的 Bucket，避免因写入报告而产生的带宽竞争影响线上业务。

- 

成本优化：存储空间清单支持按天、按周和按月导出清单文件。对于超过百亿文件的 Bucket，建议使用每周清单。同时，在目标 Bucket 上配置生命周期规则，自动删除超过 N 天（例如 30 天）的清单报告以节省存储成本。

- 

- 

| Bucket 内的文件数量 | 导出建议 |
| --- | --- |
| ＜100 亿 | 按需配置按天、按周导出 |
| 100 亿~500 亿 | 按周导出 |
| ≥500 亿 | 按前缀匹配分批导出 通过 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 提升导出限制 |


- 

前缀分区：对于超大规模（如千亿级）的 Bucket，可按业务前缀创建多条清单规则，分而治之地生成报告，便于管理和处理。

### 风险防范

- 

数据审计：导出清单文件的过程中，由于Object的创建、删除或覆盖等操作，可能会导致最终输出的清单列表中不一定包含所有的Object。最后修改时间早于manifest.json文件中createTimeStamp字段显示时间的Object会出现在清单文件中；最后修改时间晚于createTimeStamp字段显示时间的Object可能不会出现在清单文件中。建议在对清单列表中的Object进行操作之前，先使用[HeadObject](products/oss/documents/developer-reference/headobject.md)接口检查Object的属性。

- 

监控告警：监控目标 Bucket 的存储用量，防止清单文件无限制增长导致成本失控。监控PutBucketInventory等 API 的调用，以便追踪配置变更。

- 

变更管理：清单规则的变更（如修改前缀、频率）会影响下游的数据分析流程。所有变更应纳入版本控制和评审流程。

## 常见问题

- 

[为什么清单规则创建失败？](products/oss/documents/the-reason-why-you-fail-to-create-inventories.md)

- 

[为什么很长时间没有产生清单结果？](products/oss/documents/inventory-lists-are-not-generated-for-an-extended-period-of-time.md)

- 

[如何判断是否已生成清单文件？](products/oss/documents/how-to-determine-whether-inventory-lists-are-generated.md)

- 

[哪些因素会影响清单导出速度？](products/oss/documents/factors-affect-the-export-speed-of-inventory.md)

- 

[为什么找不到指定日期的清单导出结果文件？](products/oss/documents/the-reason-why-you-unable-to-find-the-exported-inventory-list-of-the-specified-date.md)

- 

[配置的清单规则何时生效？](products/oss/documents/when-inventories-take-effect.md)

- 

[为什么会出现相同日期的两份按天导出的清单结果文件？](products/oss/documents/why-do-daily-exported-inventory-results-files-of-the-same-date-exist.md)

[上一篇：AI内容感知](products/oss/documents/user-guide/ai-content-awareness.md)[下一篇：查询文件](products/oss/documents/user-guide/query-objects.md)

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
