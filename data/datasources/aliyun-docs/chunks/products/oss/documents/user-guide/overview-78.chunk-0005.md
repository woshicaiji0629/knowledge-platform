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
import com.aliyun.oss.*; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; import com.aliyun.oss.model.*; public class Demo { public static void main(String[] args) throws Exception { // Endpoint以华东1（杭州）为例，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; // 填写Endpoint对应的Region信息，例如cn-hangzhou。 String region = "cn-hangzhou"; // 从环境变量中获取访问凭证。运行本代码示例之前，请确保已设置环境变量OSS_ACCESS_KEY_ID和OSS_ACCESS_KEY_SECRET。 EnvironmentVariableCredentialsProvider credent
