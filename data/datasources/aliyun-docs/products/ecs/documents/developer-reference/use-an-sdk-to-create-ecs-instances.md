# 使用Java SDK完成ECS实例的创建运维与释放-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/developer-reference/use-an-sdk-to-create-ecs-instances

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

# 通过SDK创建并使用ECS实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云ECS提供多种API和SDK，让您可以通过编程创建和管理ECS实例，提高业务效率，实现系统自动化。本文介绍了如何利用V2.0 Java SDK创建ECS实例，借助云助手API执行脚本以及释放资源等操作。

## 准备工作

- 

由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用满足最小化权限需求的RAM用户的AccessKey。获取方法请参见[创建](products/ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md)。

- 

给RAM用户授予操作云服务器ECS和专有网络VPC相关资源的权限。本文提供的示例代码需要创建实例、VPC、交换机等资源，建议授予以下权限：

| 云产品 | 授予权限 |
| --- | --- |
| 专有网络 VPC | 本示例选择系统策略：AliyunVPCFullAccess |
| 云服务器 ECS | 本示例选择系统策略：AliyunECSFullAccess |


- 

本文示例代码会在系统环境变量中读取AccessKey作为访问云服务的凭证，具体操作步骤请参见[在](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Linux、macOS](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[和](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Windows](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[系统配置环境变量](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)。

- 

获取ECS SDK和VPC SDK，本文通过添加Maven依赖的方式来安装。更多安装方式，请参见[安装](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-tea&tab=primer-doc)[ECS Java SDK](https://next.api.aliyun.com/api-tools/sdk/Ecs?version=2014-05-26&language=java-tea&tab=primer-doc)和[安装](https://next.api.aliyun.com/api-tools/sdk/Vpc?version=2016-04-28&language=java-tea)[VPC Java SDK](https://next.api.aliyun.com/api-tools/sdk/Vpc?version=2016-04-28&language=java-tea)。

添加Maven依赖的示例如下：

<dependencies> <dependency> <groupId>com.aliyun</groupId> <artifactId>ecs20140526</artifactId> <version>5.3.0</version> </dependency> <dependency> <groupId>com.aliyun</groupId> <artifactId>vpc20160428</artifactId> <version>7.12.0</version> </dependency> </dependencies>

## 创建ECS实例

创建ECS实例时有很多必填参数，包括交换机ID、安全组、镜像等。您可以传入已经准备好的资源ID，或者调用以下OpenAPI创建对应资源。

- 

创建VPC

VPC是一种专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateVpc](products/vpc/documents/api-createvpc.md) | RegionId | 地域： cn-hangzhou |
| CidrBlock | VPC 网段： 192.168.0.0/16 |  |


- 

查询VPC信息

在调用CreateVpc之后，VPC需要一段配置时间，您可以调用该OpenAPI查询VPC的状态。当VPC的状态处于Available（可用）时，请再调用后续OpenAPI。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DescribeVpcs](products/vpc/documents/api-describevpcs.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC 的 ID： vpc-bp1aag0sb9s4i92i3**** |  |


- 

创建交换机

交换机是一种在虚拟化环境中使用的网络交换设备，它模拟了物理交换机的功能，使虚拟机（VMs）之间以及虚拟机与物理网络之间可以进行通信。

| API | 参数 | 示例取值 |
| --- | --- | --- |
|  | RegionId | 地域： cn-hangzhou |
| [CreateVSwitch](products/vpc/documents/api-createvswitch.md) | ZoneId | 可用区： cn-hangzhou-i |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3**** |  |
| CidrBlock | 交换机网段： 192.168.0.0/24 |  |


- 

创建安全组

安全组是一种虚拟防火墙，能够控制ECS实例的出入方向流量。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateSecurityGroup](products/ecs/documents/api-createsecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |


- 

给安全组添加防护规则

- 

- 

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [AuthorizeSecurityGroup](products/ecs/documents/api-authorizesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| IpProtocol | 协议： tcp |  |
| SourceCidrIp | 源 CIDR： 0.0.0.0/0 |  |
| PortRange | 端口范围： Linux 实例： 22/22 Windows 实例： 3389/3389 |  |


- 

创建SSH密钥对

阿里云SSH密钥对是一种安全便捷的登录认证方式，用于在SSH协议中进行身份验证和加密通信。通过SSH密钥对，您可以实现免密码远程登录。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateKeyPair](products/ecs/documents/api-createkeypair.md) | RegionId | 地域： cn-hangzhou |
| KeyPairName | 密钥对名称： sdk-key-pair |  |


- 

创建ECS实例

使用ECS您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [RunInstances](products/ecs/documents/api-runinstances.md) | RegionId | 地域： cn-hangzhou |
| ImageId | 镜像：推荐使用 Alibaba Cloud Linux 镜像 aliyun_3_x64_20G_scc_alibase_20220225.vhd 。 |  |
| InstanceType | 实例规格： ecs.e-c1m2.xlarge 。 |  |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |
| InstanceName | 实例名称： sdk-test |  |
| InstanceChargeType | 付费方式：实例按照按量付费的方式 PostPaid 说明 您需要确保账号余额能够完成支付。 |  |
| KeyPairName | 密钥对名称： sdk-key-pair |  |
| SystemDisk.Category | 系统盘的云盘种类： cloud_essd |  |


- 

查询ECS实例状态

在调用RunInstances后，ECS实例需要一定的启动时间。仅当ECS实例状态达到Running时，才能通过远程连接等方式登录到实例，以进行各种操作和应用程序的部署。您可以调用该OpenAPI查询ECS实例的状态。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DescribeInstanceStatus](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstancestatus.md) | RegionId | 地域： cn-hangzhou |
| InstanceId | 实例 ID 集合： ["i-bp17f3kzgtzzj91r****"] |  |


完整的示例代码如下：

import com.aliyun.ecs20140526.models.*; import com.aliyun.teaopenapi.models.Config; import com.aliyun.vpc20160428.models.CreateVSwitchRequest; import com.aliyun.vpc20160428.models.CreateVSwitchResponse; import com.aliyun.vpc20160428.models.CreateVpcRequest; import com.aliyun.vpc20160428.models.CreateVpcResponse; import com.aliyun.vpc20160428.models.DescribeVpcsRequest; import java.util.ArrayList; import java.util.List; public class EcsDemo { public static void main(String[] args) { String vpcId = null; String vSwitchId = null; String securityGroupId = null; String instanceId = null; com.aliyun.vpc20160428.Client vpcClient = null; com.aliyun.ecs20140526.Client ecsClient = null; try { vpcClient = createVpcClient(); ecsClient = createEcsClient(); // 创建VPC vpcId = createVpc(vpcClient); System.out.println("VPC create success, vpcId :" + vpcId); // 当VPC的状态为Available时，继续后续步骤 while (true) { String status = describeVpc(vpcId, vpcClient); if ("Available".equals(status)) { break; } } // 创建交换机 vSwitchId = CreateVSwitch(vpcId, vpcClient); System.out.println("VSwitch create success, vSwitchId :" + vSwitchId); // 创建安全组 securityGroupId = createSecurityGroup(vpcId, ecsClient); System.out.println("SecurityGroup create success, securityGroupId :" + securityGroupId); // 添加安全组入方向规则 authorizeSecurityGroup(securityGroupId, ecsClient); // 创建密钥对。注意：保存密钥对的信息，用于登录ECS CreateKeyPairResponse keyPair = createKeyPair(ecsClient); System.out.println("KeyPair create success, keyPairName :" + keyPair.body.keyPairName); // 创建实例，当ECS实例状态为Running时，表示ECS已经处于运行中 instanceId = createInstance(ecsClient, vSwitchId, securityGroupId); System.out.println("ECS create success, instanceId :" + instanceId); while (true) { List<String> instanceIds = new ArrayList<>(); instanceIds.add(instanceId); DescribeInstanceStatusResponse describeInstanceStatus = describeInstanceStatus(instanceIds, ecsClient); List<DescribeInstanceStatusResponseBody.DescribeInstanceStatusResponseBodyInstanceStatusesInstanceStatus> instanceStatusList = describeInstanceStatus.body.instanceStatuses.instanceStatus; if (instanceStatusList != null && !instanceStatusList.isEmpty()) { String status = instanceStatusList.get(0).status; if ("Running".equals(status)) { break; } } } } catch (Exception e) { // 当面对部分资源创建成功而其他资源创建失败的情况时，需要增加合理的处理机制，例如记录日志、回滚机制、补偿机制等。 System.out.println(e.getMessage()); } } public static class Constants { // 名称 public static final String NAME = "sdk-test"; // 地域 public static final String REGION_ID = "cn-hangzhou"; // 可用区 public static final String ZONE_ID = "cn-hangzhou-i"; // 创建的VPC网络和交换机网段 public static final String CIDR_BLOCK_VPC = "192.168.0.0/16"; public static final String CIDR_BLOCK_VSWITCH = "192.168.0.0/24"; // 镜像 public static final String IMAGE_ID = "aliyun_3_x64_20G_scc_alibase_20220225.vhd"; // 实例规格 public static final String INSTANCE_TYPE = "ecs.e-c1m2.xlarge"; // 磁盘类型 public static final String SYSTEM_DISK_CATEGORY = "cloud_essd"; // 密钥对名称 public static final String KEY_PAIR_NAME = "sdk-key-pair"; // 服务接入点 public static final class ENDPOINT { public static final String VPC = "vpc.cn-hangzhou.aliyuncs.com"; public static final String ECS = "ecs.cn-hangzhou.aliyuncs.com"; } // 付费类型 public static final class INSTANCE_CHARGE_TYPE { // 包年包月 public static final String PRE_PAID = "PrePaid"; // 按量付费 public static final String POST_PAID = "PostPaid"; } } public static com.aliyun.vpc20160428.Client createVpcClient() throws Exception { Config config = new Config(); config.setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")); config.setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); config.endpoint = Constants.ENDPOINT.VPC; return new com.aliyun.vpc20160428.Client(config); } public static com.aliyun.ecs20140526.Client createEcsClient() throws Exception { Config config = new Config(); config.setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")); config.setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); config.endpoint = Constants.ENDPOINT.ECS; return new com.aliyun.ecs20140526.Client(config); } /** * 创建VPC（虚拟私有云）网络 * 该方法通过调用阿里云VPC服务的API来创建一个VPC网络，并返回新创建VPC的ID * * @param vpcClient VPC客户端 * @return 返回新创建的VPC的ID */ public static String createVpc(com.aliyun.vpc20160428.Client vpcClient) { try { CreateVpcRequest createVpcRequest = new CreateVpcRequest() .setRegionId(Constants.REGION_ID) .setCidrBlock(Constants.CIDR_BLOCK_VPC) .setVpcName(Constants.NAME); CreateVpcResponse vpc = vpcClient.createVpc(createVpcRequest); return vpc.body.vpcId; } catch (Exception e) { throw new RuntimeException("createVpc failed: " + e.getMessage()); } } /** * 创建VSwitch（虚拟交换机）. * 该方法负责通过阿里云VPC客户端创建一个新的VSwitch. 它配置了必要的请求参数，如区域ID、可用区ID、 * CIDR段、VPC ID和VSwitch名称，然后发送请求并返回新创建VSwitch的ID. * * @param vpcId VPC的ID，标识要在其中创建VSwitch的VPC * @param vpcClient VPC客户端 * @return 返回新创建的VSwitch的ID */ public static String CreateVSwitch(String vpcId, com.aliyun.vpc20160428.Client vpcClient) { try { CreateVSwitchRequest createVSwitchRequest = new CreateVSwitchRequest() .setRegionId(Constants.REGION_ID) .setZoneId(Constants.ZONE_ID) .setCidrBlock(Constants.CIDR_BLOCK_VSWITCH) .setVpcId(vpcId) .setVSwitchName(Constants.NAME); CreateVSwitchResponse vSwitch = vpcClient.createVSwitch(createVSwitchRequest); return vSwitch.body.vSwitchId; } catch (Exception e) { throw new RuntimeException("CreateVSwitch failed: " + e.getMessage()); } } /** * 创建安全组 * * @param vpcId 专有网络的ID * @param ecsClient ECS客户端 * @return 创建的安全组的ID */ public static String createSecurityGroup(String vpcId, com.aliyun.ecs20140526.Client ecsClient) { try { CreateSecurityGroupRequest createSecurityGroupRequest = new CreateSecurityGroupRequest() .setRegionId(Constants.REGION_ID) .setVpcId(vpcId) .setSecurityGroupName(Constants.NAME); CreateSecurityGroupResponse securityGroup = ecsClient.createSecurityGroup(createSecurityGroupRequest); return securityGroup.body.securityGroupId; } catch (Exception e) { throw new RuntimeException("createSecurityGroup failed: " + e.getMessage()); } } /** * 授权安全组规则，以允许特定的入站流量 * 例如：允许TCP协议的22端口（SSH）从任何IP地址（0.0.0.0/0）访问。 * * @param securityGroupId 安全组的ID，用于标识哪个安全组的规则需要被授权。 * @param ecsClient ECS客户端 */ public static void authorizeSecurityGroup(String securityGroupId, com.aliyun.ecs20140526.Client ecsClient) { try { AuthorizeSecurityGroupRequest.AuthorizeSecurityGroupRequestPermissions permission = new AuthorizeSecurityGroupRequest.AuthorizeSecurityGroupRequestPermissions() .setIpProtocol("tcp") .setPortRange("22/22") .setSourceCidrIp("0.0.0.0/0"); List<AuthorizeSecurityGroupRequest.AuthorizeSecurityGroupRequestPermissions> permissions = new ArrayList<>(); permissions.add(permission); AuthorizeSecurityGroupRequest authorizeSecurityGroupRequest = new AuthorizeSecurityGroupRequest() .setRegionId(Constants.REGION_ID) .setSecurityGroupId(securityGroupId) .setPermissions(permissions); ecsClient.authorizeSecurityGroup(authorizeSecurityGroupRequest); } catch (Exception e) { throw new RuntimeException("authorizeSecurityGroup failed: " + e.getMessage()); } } /** * 创建ECS实例 * * @param ecsClient ECS客户端 * @param vSwitchId 交换机ID * @param securityGroupId 安全组ID * @return 新创建的ECS实例的ID */ public static String createInstance(com.aliyun.ecs20140526.Client ecsClient, String vSwitchId, String securityGroupId) { try { RunInstancesRequest.RunInstancesRequestSystemDisk systemDisk = new RunInstancesRequest.RunInstancesRequestSystemDisk() .setCategory(Constants.SYSTEM_DISK_CATEGORY); RunInstancesRequest runInstancesRequest = new RunInstancesRequest() .setRegionId(Constants.REGION_ID) .setImageId(Constants.IMAGE_ID) .setInstanceType(Constants.INSTANCE_TYPE) .setSecurityGroupId(securityGroupId) .setVSwitchId(vSwitchId) .setInstanceChargeType(Constants.INSTANCE_CHARGE_TYPE.POST_PAID) .setInstanceName(Constants.NAME) .setInternetMaxBandwidthOut(1) .setSystemDisk(systemDisk) .setKeyPairName(Constants.KEY_PAIR_NAME); RunInstancesResponse resp = ecsClient.runInstances(runInstancesRequest); return resp.body.getInstanceIdSets().getInstanceIdSet().get(0); } catch (Exception e) { throw new RuntimeException("createInstance failed: " + e.getMessage()); } } /** * 使用指定的安全组ID创建密钥对 * * @param ecsClient ECS客户端 * @return 返回创建密钥对的响应对象 */ public static CreateKeyPairResponse createKeyPair(com.aliyun.ecs20140526.Client ecsClient) { try { // 创建一个创建密钥对的请求对象，并设置区域ID、密钥对名称和资源组ID CreateKeyPairRequest createKeyPairRequest = new CreateKeyPairRequest() .setRegionId(Constants.REGION_ID) .setKeyPairName(Constants.KEY_PAIR_NAME); // 通过ECS客户端发送创建密钥对的请求，并返回响应对象 return ecsClient.createKeyPair(createKeyPairRequest); } catch (Exception e) { // 如果创建密钥对失败，则抛出运行时异常，包含错误信息 throw new RuntimeException("createKeyPair failed: " + e.getMessage()); } } /** * 查询VPC状态 * * @param vpcId VPC的ID * @param vpcClient VPC客户端 * @return 返回VPC的状态信息 */ public static String describeVpc(String vpcId, com.aliyun.vpc20160428.Client vpcClient) { try { DescribeVpcsRequest request = new DescribeVpcsRequest() .setRegionId(Constants.REGION_ID) .setVpcId(vpcId); return vpcClient.describeVpcs(request).body.vpcs.getVpc().get(0).status; } catch (Exception e) { // 如果发生异常，抛出自定义异常 throw new RuntimeException("describeVpc failed: " + e.getMessage()); } } /** * 根据实例ID列表查询ECS实例信息 * * @param instanceIds 实例ID列表 * @param ecsClient ECS客户端 * @return 返回查询到的实例状态信息响应对象 */ public static DescribeInstanceStatusResponse describeInstanceStatus(List<String> instanceIds, com.aliyun.ecs20140526.Client ecsClient) { try { DescribeInstanceStatusRequest request = new DescribeInstanceStatusRequest() .setRegionId(Constants.REGION_ID) .setInstanceId(instanceIds); return ecsClient.describeInstanceStatus(request); } catch (Exception e) { throw new RuntimeException("describeInstanceStatus failed: " + e.getMessage()); } } }

## 免登录运维

您可以通过云服务器ECS提供的原生自动化运维工具云助手，免密码、免登录，且无需使用跳板机，即可批量执行命令（Shell、PowerShell、Bat等），从而实现自动化运维脚本的执行、进程的轮询、软件的安装与卸载、服务的启动或停止，以及补丁或安全更新的安装等任务。更多详细信息，请参见[云助手概述](products/ecs/documents/user-guide/overview-10.md)。

例如在ECS中安装Java和Tomcat，您可以调用RunCommand接口执行命令：

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [RunCommand](products/ecs/documents/api-runcommand.md) | RegionId | 地域： cn-hangzhou |
| Type | 运维命令的语言类型： RunShellScript |  |
| CommandContent | 命令内容： #!/bin/bash if cat /etc/issue|grep -i Ubuntu ; then sudo apt-get update sudo apt-get install -y default-jdk sudo apt-get install -y tomcat9 else yum install -y java yum install -y tomcat fi |  |
| Timeout | 可选，执行命令的超时时间，单位：秒。 示例： 60 |  |
| InstanceId | ECS 实例 ID 集合： ["i-bp17f3kzgtzzj91r****"] |  |


完整的示例代码如下

import com.aliyun.ecs20140526.Client; import com.aliyun.ecs20140526.models.RunCommandRequest; import com.aliyun.ecs20140526.models.RunCommandResponse; import com.aliyun.teaopenapi.models.Config; import com.google.gson.Gson; import java.util.ArrayList; import java.util.List; public class CloudAssistant { public static void main(String[] args) throws Exception { Client ecsClient = createEcsClient(); List<String> instanceIds = new ArrayList<>(); instanceIds.add("i-bp17f3kzgtzzj91r****"); String commandContent = "#!/bin/bash\n" + "if cat /etc/issue|grep -i Ubuntu ; then\n" + "\tsudo apt-get update\n" + "\tsudo apt-get install -y default-jdk\n" + "\tsudo apt-get install -y tomcat9\n" + "else\n" + " yum install -y java\n" + "\tyum install -y tomcat\n" + "fi"; System.out.println("commandContent：" + commandContent); runCommand(commandContent, instanceIds, ecsClient); } public static class Constants { // 地域 public static final String REGION_ID = "cn-hangzhou"; // 服务接入点 public static final class ENDPOINT { public static final String VPC = "vpc.cn-hangzhou.aliyuncs.com"; public static final String ECS = "ecs.cn-hangzhou.aliyuncs.com"; } // 命令类型 public static final class COMMAND_TYPE { // 适用于Linux实例的Shell命令。 public static final String RUN_SHELL_SCRIPT = "RunShellScript"; // 适用于Windows实例的Bat命令。 public static final String RUN_BAT_SCRIPT = "RunBatScript"; // 适用于Windows实例的PowerShell命令。 public static final String RUN_POWERSHELL_SCRIPT = "RunPowerShellScript"; } } public static com.aliyun.ecs20140526.Client createEcsClient() throws Exception { Config config = new Config(); config.setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")); config.setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); config.endpoint = Constants.ENDPOINT.ECS; return new com.aliyun.ecs20140526.Client(config); } public static void runCommand(String commandContent, List<String> instanceIds, com.aliyun.ecs20140526.Client ecsClient) { try { RunCommandRequest request = new RunCommandRequest(); request.setRegionId(Constants.REGION_ID); // RunShellScript适用于Linux实例的Shell命令。 request.setType(Constants.COMMAND_TYPE.RUN_SHELL_SCRIPT); request.setCommandContent(commandContent); request.setInstanceId(instanceIds); request.setTimeout(60L); RunCommandResponse runCommandResponse = ecsClient.runCommand(request); System.out.println(new Gson().toJson(runCommandResponse)); } catch (Exception e) { throw new RuntimeException("runCommand failed:" + e); } } }

## 释放资源

当您不再需要所创建的资源时，可以调用以下OpenAPI接口以释放该资源。

说明

根据您的实际需求，选择相应的OpenAPI释放资源 。本示例释放上述步骤创建的所有资源。

- 

释放ECS实例

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteInstances](products/ecs/documents/api-deleteinstances.md) | RegionId | 地域： cn-hangzhou |
| InstanceId | 实例 ID： i-bp17f3kzgtzzj91r**** |  |


- 

删除SSH密钥对

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteKeyPairs](products/ecs/documents/api-deletekeypairs.md) | RegionId | 地域： cn-hangzhou |
| KeyPairNames | SSH 密钥对名称： ["sdk-key-pair"] |  |


- 

删除安全组

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteSecurityGroup](products/ecs/documents/developer-reference/api-ecs-2014-05-26-deletesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |


- 

删除交换机

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteVSwitch](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deletevswitch.md) | RegionId | 地域： cn-hangzhou |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |


- 

删除VPC

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteVpc](products/vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |


示例代码如下：

import com.aliyun.ecs20140526.Client; import com.aliyun.ecs20140526.models.*; import com.aliyun.teaopenapi.models.Config; import com.aliyun.vpc20160428.models.DeleteVSwitchRequest; import com.aliyun.vpc20160428.models.DeleteVpcRequest; import com.google.gson.Gson; import java.util.Collections; import java.util.concurrent.Executors; import java.util.concurrent.ScheduledExecutorService; import java.util.concurrent.TimeUnit; public class DeleteResources { public static void main(String[] args) { String vpcId = "vpc-bp1aag0sb9s4i92i3****"; String vSwitchId = "vsw-bp1nzprm8h7mmnl8t****"; String securityGroupId = "sg-bp1esyhwfbqeyudt****"; String instanceId = "i-bp17f3kzgtzzj91r****"; String keyPairName = "sdk-key-pair"; ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor(); try { com.aliyun.ecs20140526.Client ecsClient = createEcsClient(); com.aliyun.vpc20160428.Client vpcClient = createVpcClient(); // 删除ECS实例 executorService.schedule(() -> deleteInstance(instanceId, ecsClient), 1, TimeUnit.SECONDS); // 删除密钥对 executorService.schedule(() -> deleteKeyPairs(keyPairName, ecsClient), 1, TimeUnit.SECONDS); // 删除安全组 executorService.schedule(() -> deleteSecurityGroup(securityGroupId, ecsClient), 60, TimeUnit.SECONDS); // 删除交换机 executorService.schedule(() -> deleteVSwitch(vSwitchId, vpcClient), 60, TimeUnit.SECONDS); // 删除VPC executorService.schedule(() -> deleteVpc(vpcId, vpcClient), 65, TimeUnit.SECONDS); } catch (Exception e) { System.err.println("An error occurred: " + e.getMessage()); // 异常处理，因为释放实例需要一定时间，可能会存在部分删除成功，部分删除失败的情况，请增加合理的删除失败数据处理机制。 } finally { executorService.shutdown(); } } public static class Constants { // 服务接入点 public static final class ENDPOINT { public static final String VPC = "vpc.cn-hangzhou.aliyuncs.com"; public static final String ECS = "ecs.cn-hangzhou.aliyuncs.com"; } // 地域 public static final String REGION_ID = "cn-hangzhou"; } public static com.aliyun.vpc20160428.Client createVpcClient() throws Exception { Config config = new Config(); config.setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")); config.setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); config.endpoint = Constants.ENDPOINT.VPC; return new com.aliyun.vpc20160428.Client(config); } public static com.aliyun.ecs20140526.Client createEcsClient() throws Exception { Config config = new Config(); config.setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")); config.setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")); config.endpoint = Constants.ENDPOINT.ECS; return new com.aliyun.ecs20140526.Client(config); } /** * 删除指定的VPC（虚拟私有云）资源 * * @param vpcId VPC的ID，标识了要删除的VPC资源 * @param vpcClient VPC客户端 */ public static void deleteVpc(String vpcId, com.aliyun.vpc20160428.Client vpcClient) { try { System.out.println("VPC is deleting, please wait..."); DeleteVpcRequest deleteVpcRequest = new DeleteVpcRequest() .setRegionId(Constants.REGION_ID) .setVpcId(vpcId); vpcClient.deleteVpc(deleteVpcRequest); } catch (Exception e) { throw new RuntimeException("DeleteVpc failed: " + e.getMessage()); } } /** * 删除指定的虚拟交换机（VSwitch） * * @param vSwitchId 虚拟交换机的ID * @param vpcClient VPC客户端 */ public static void deleteVSwitch(String vSwitchId, com.aliyun.vpc20160428.Client vpcClient) { System.out.println("VSwitch is deleting, please wait..."); try { DeleteVSwitchRequest deleteVSwitchRequest = new DeleteVSwitchRequest() .setRegionId(Constants.REGION_ID) .setVSwitchId(vSwitchId); vpcClient.deleteVSwitch(deleteVSwitchRequest); } catch (Exception e) { throw new RuntimeException("DeleteVSwitch failed: " + e.getMessage()); } } /** * 删除指定的安全组 * * @param securityGroupId 安全组的ID，标识要删除的安全组 * @param ecsClient ECS客户端 */ public static void deleteSecurityGroup(String securityGroupId, Client ecsClient) { System.out.println("SecurityGroup is deleting, please wait..."); try { DeleteSecurityGroupRequest deleteSecurityGroupRequest = new DeleteSecurityGroupRequest() .setRegionId(Constants.REGION_ID) .setSecurityGroupId(securityGroupId); ecsClient.deleteSecurityGroup(deleteSecurityGroupRequest); } catch (Exception e) { throw new RuntimeException("DeleteSecurityGroup failed: " + e.getMessage()); } } /** * 删除云服务器实例. * * @param instanceId 实例ID，标识了要删除的云服务器实例 * @param ecsClient ECS客户端 */ public static void deleteInstance(String instanceId, Client ecsClient) { System.out.println("ECS instance is deleting, please wait..."); try { DeleteInstanceRequest request = new DeleteInstanceRequest() .setForce(true) .setInstanceId(instanceId); ecsClient.deleteInstance(request); } catch (Exception e) { throw new RuntimeException("DeleteInstance failed: " + e.getMessage()); } } /** * 使用指定的ECS客户端删除密钥对 * * @param keyPairName 密钥对名称 * @param ecsClient ECS客户端 */ public static void deleteKeyPairs(String keyPairName, Client ecsClient) { System.out.println("KeyPair is deleting, please wait..."); try { // 创建删除密钥对请求，并设置区域ID和密钥对名称 DeleteKeyPairsRequest deleteKeyPairsRequest = new DeleteKeyPairsRequest() .setRegionId(Constants.REGION_ID) .setKeyPairNames(new Gson().toJson(Collections.singletonList(keyPairName))); ecsClient.deleteKeyPairs(deleteKeyPairsRequest); } catch (Exception e) { // 如果删除密钥对失败，抛出运行时异常，包含错误信息 throw new RuntimeException("DeleteKeyPairs failed: " + e.getMessage()); } } }

[上一篇：SDK概览](products/ecs/documents/developer-reference/ecs-v2-0-sdk-overview.md)[下一篇：Java SDK调用示例](products/ecs/documents/developer-reference/use-sdk-for-java.md)

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
