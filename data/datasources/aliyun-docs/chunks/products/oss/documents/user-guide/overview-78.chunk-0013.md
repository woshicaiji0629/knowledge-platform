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
import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Endpoint对应的Region信息，例如cn-hangzhou。 String region = "cn-hangzhou"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 填写Bucket名称，例如examplebucket。 String bucketName = "examplebucket"; // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfi
