## CreateAutoProvisioningGroup最佳实践
本章节提供CreateAutoProvisioningGroup接口对应的Java代码示例，使您快速了解该接口的使用方式。
安装ECS Java SDK以及阿里云核心库。
具体操作，请参见[SDK](../developer-reference/ecs-v2-0-sdk-overview.md)[概览](../developer-reference/ecs-v2-0-sdk-overview.md)。
编写调用CreateAutoProvisioningGroup接口的Java代码。
代码示例如下：
import com.aliyun.ecs20140526.Client; import com.aliyun.ecs20140526.models.CreateAutoProvisioningGroupRequest; import com.aliyun.ecs20140526.models.CreateAutoProvisioningGroupResponse; import com.aliyun.teaopenapi.models.Config; import com.aliyun.teautil.models.RuntimeOptions; import com.google.gson.Gson; public class Test { public static void main(String[] args_) throws Exception { Config config = new Config() .setAccessKeyId(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")) .setAccessKeySecret(System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")) .setEndpoint("ecs.cn-heyuan.aliyuncs.com"); Client client = new Client(config); CreateAutoProvisioningGroupRequest.CreateAutoProvisioningGroupRequestLaunchTemplateConfig launchTemplateConfig = new CreateAutoProvisioningGroupRequest.CreateAutoProvisioningGroupRequestLaunchTemplateConfig() .setVSwitchId("vsw-f8zadqudz*********") .setInstanceType("ecs.s6-c1m1.small"
