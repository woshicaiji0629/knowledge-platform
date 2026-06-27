# 使用JavaSDK快速入门OSS文件管理-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/oss-sdk-quick-start?spm=a2c4g.11186623.help-menu-31815.d_1_5.315e3167o0vZzy

# OSS SDK快速入门
使用OSS SDK集成阿里云对象存储服务（OSS），为应用程序提供高效的存储管理与访问。本文以OSS Java SDK为例介绍如何完成创建存储空间（Bucket）、上传文件、下载文件、列举文件以及删除文件和Bucket等操作。
## 前提条件
已[注册阿里云账号](https://account.aliyun.com/register/qr_register.htm?oauth_callback=https%3A%2F%2Fbailian.console.aliyun.com%2F%3FapiKey%3D1)。
已[个人实名认证](https://help.aliyun.com/zh/document_detail/324614.html#task-2020003)或[企业实名认证](https://help.aliyun.com/zh/account/overview)。
已[开通](https://oss.console.aliyun.com/overview)[OSS](https://oss.console.aliyun.com/overview)[服务](https://oss.console.aliyun.com/overview)。
## 配置凭证
[创建有](../../../ram/documents/create-an-accesskey-pair-1.md)[OSS](../../../ram/documents/create-an-accesskey-pair-1.md)[管理权限的](../../../ram/documents/create-an-accesskey-pair-1.md)[RAM](../../../ram/documents/create-an-accesskey-pair-1.md)[用户](../../../ram/documents/create-an-accesskey-pair-1.md)[AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md)。
使用ROS脚本快速创建有OSS管理权限的RAM用户AccessKey
在资源编排ROS控制台的[创建资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks/create?templateUrl=https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241114/itgrlo/createossadmin.yaml&step=1&hideTemplateSelector=false)页面的安全确认下，勾选确认，然后单击创建。
创建完成后，在输出中，复制创建的AccessKey。
使用RAM用户AccessKey配置环境变量。
### Linux
在命令行界面执行以下命令来将环境变量设置追加到~/.bashrc文件中。
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
执行以下命令使变更生效。
source ~/.bashrc
执行以下命令检查环境变量是否生效。
echo $OSS_ACCESS_KEY_ID echo $OSS_ACCESS_KEY_SECRET
### macOS
在终端中执行以下命令，查看默认Shell类型。
echo $SHELL
根据默认Shell类型进行操作。
Zsh
执行以下命令来将环境变量设置追加到~/.zshrc文件中。
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
执行以下命令使变更生效。
source ~/.zshrc
执行以下命令检查环境变量是否生效。
echo $OSS_ACCESS_KEY_ID echo $OSS_ACCESS_KEY_SECRET
Bash
执行以下命令来将环境变量设置追加到~/.bash_profile文件中。
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile
执行以下命令使变更生效。
source ~/.bash_profile
执行以下命令检查环境变量是否生效。
echo $OSS_ACCESS_KEY_ID echo $OSS_ACCESS_KEY_SECRET
### Windows
CMD
在CMD中运行以下命令。
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
运行以下命令，检查环境变量是否生效。
echo %OSS_ACCESS_KEY_ID% echo %OSS_ACCESS_KEY_SECRET%
PowerShell
在PowerShell中运行以下命令。
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
运行以下命令，检查环境变量是否生效。
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
参考上述方式修改系统环境变量后，请重启或刷新您的编译运行环境，包括IDE、命令行界面、其他桌面应用程序及后台服务，以确保最新的系统环境变量成功加载。
## 安装SDK
已安装Java 7 及以上版本。
通过以下命令查看Java版本。
java -version
如果当前计算环境没有Java或版本低于Java 7，请[下载](https://www.oracle.com/cn/java/technologies/downloads/)[Java](https://www.oracle.com/cn/java/technologies/downloads/)。
您可以通过以下三种方式安装OSS Java SDK。
说明
请根据需求选择合适的OSS Java SDK版本，推荐您使用最新的3.17.4版本，确保本文中的代码示例可以正常运行。关于版本功能的更多信息，请参见[GitHub](https://github.com/aliyun/aliyun-oss-java-sdk/releases)。
### 在Maven项目中加入依赖项（推荐方式）
在Maven工程中使用OSS Java SDK，只需在pom.xml中加入相应依赖即可。以在<dependencies>中加入3.17.4版本的依赖为例：
<dependency> <groupId>com.aliyun.oss</groupId> <artifactId>aliyun-sdk-oss</artifactId> <version>3.17.4</version> </dependency>
如果使用的是Java 9及以上的版本，则需要添加以下JAXB相关依赖。
<dependency> <groupId>javax.xml.bind</groupId> <artifactId>jaxb-api</artifactId> <version>2.3.1</version> </dependency> <dependency> <groupId>javax.activation</groupId> <artifactId>activation</artifactId> <version>1.1.1</version> </dependency> <!-- no more than 2.3.3--> <dependency> <groupId>org.glassfish.jaxb</groupId> <artifactId>jaxb-runtime</artifactId> <version>2.3.3</version> </dependency>
### 在Eclipse项目中导入JAR包
以3.17.4版本为例，步骤如下：
下载[JavaSDK](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250424/jkaljk/aliyun-oss-java-sdk-demo-mvn-3.17.4.zip)[开发包](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250424/jkaljk/aliyun-oss-java-sdk-demo-mvn-3.17.4.zip)。
解压该开发包。
将解压后文件夹中的文件aliyun-sdk-oss-3.17.4.jar以及lib文件夹下的所有文件拷贝到您的项目中。
在Eclipse中选择您的工程，右键选择Properties>Java Build Path>Add JARs。
选中拷贝的所有JAR文件，导入到Libraries中。
### 在IntelliJ IDEA项目中导入JAR包
以3.17.4版本为例，步骤如下：
下载[JavaSDK](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250424/frtebc/aliyun-oss-java-sdk-demo-mvn-3.17.4.zip)[开发包代码](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250424/frtebc/aliyun-oss-java-sdk-demo-mvn-3.17.4.zip)。
解压该开发包。
将解压后文件夹中的文件aliyun-sdk-oss-3.17.4.jar以及lib文件夹下的所有JAR文件拷贝到您的项目中。
在IntelliJ IDEA中选择您的工程，右键选择File>Project Structure>Modules>Dependencies>+>JARs or directories。
选中拷贝的所有JAR文件，导入到External Libraries中。
## 运行示例
运行以下代码示例以体验OSS的完整使用流程：创建一个Bucket、上传文件、下载文件、列举文件以及删除文件和Bucket。
import java.io.*; import java.util.Random; import com.aliyun.oss.*; import com.aliyun.oss.model.OSSObject; import com.aliyun.oss.model.ObjectListing; import com.aliyun.oss.model.OSSObjectSummary; import com.aliyun.oss.common.auth.*; import com.aliyun.oss.common.comm.SignVersion; public class OssJavaSdkQuickStart { /** 生成一个唯一的 Bucket 名称 */ public static String generateUniqueBucketName(String prefix) { // 获取当前时间戳 String timestamp = String.valueOf(System.currentTimeMillis()); // 生成一个 0 到 9999 之间的随机数 Random random = new Random(); int randomNum = random.nextInt(10000); // 生成一个 0 到 9999 之间的随机数 // 连接以形成一个唯一的 Bucket 名称 return prefix + "-" + timestamp + "-" + randomNum; } public static void main(String[] args) throws com.aliyuncs.exceptions.ClientException { // Endpoint以华东1（杭州）为例，填写为https://oss-cn-hangzhou.aliyuncs.com，其它Region请按实际情况填写。 String endpoint = "https://oss-cn-hangzhou.aliyuncs.com"; String bucketName = generateUniqueBucketName("demo"); // 填写Bucket所在地域。以华东1（杭州）为例，Region填写为cn-hangzhou。 String region = "cn-hangzhou"; // 从环境变量中获取访问凭证。运行本代码示例之前，请先配置环境变量 EnvironmentVariableCredentialsProvider credentialsProvider = CredentialsProviderFactory.newEnvironmentVariableCredentialsProvider(); // 创建OSSClient实例。 // 当OSSClient实例不再使用时，调用shutdown方法以释放资源。 ClientBuilderConfiguration clientBuilderConfiguration = new ClientBuilderConfiguration(); // 显式声明使用 V4 签名算法 clientBuilderConfiguration.setSignatureVersion(SignVersion.V4); OSS ossClient = OSSClientBuilder.create() .endpoint(endpoint) .credentialsProvider(credentialsProvider) .region(region) .build(); try { // 1. 创建存储空间（Bucket） ossClient.createBucket(bucketName); System.out.println("1. Bucket " + bucketName + " 创建成功。"); // 2. 上传文件 String objectName = "exampledir/exampleobject.txt"; String content = "Hello OSS"; ossClient.putObject(bucketName, objectName, new ByteArrayInputStream(content.getBytes())); System.out.println("2. 文件 " + objectName + " 上传成功。"); // 3. 下载文件 OSSObject ossObject = ossClient.getObject(bucketName, objectName); InputStream contentStream = ossObject.getObjectContent(); BufferedReader reader = new BufferedReader(new InputStreamReader(contentStream)); String line; System.out.println("3. 下载的文件内容："); while ((line = reader.readLine()) != null) { System.out.println(line); } contentStream.close(); // 4. 列出文件 System.out.println("4. 列出 Bucket 中的文件："); ObjectListing objectListing = ossClient.listObjects(bucketName); for (OSSObjectSummary objectSummary : objectListing.getObjectSummaries()) { System.out.println(" - " + objectSummary.getKey() + " (大小 = " + objectSummary.getSize() + ")"); } // 5. 删除文件 ossClient.deleteObject(bucketName, objectName); System.out.println("5. 文件 " + objectName + " 删除成功。"); // 6. 删除存储空间（Bucket） ossClient.deleteBucket(bucketName); System.out.println("6. Bucket " + bucketName + " 删除成功。"); } catch (OSSException oe) { System.out.println("Caught an OSSException, which means your request made it to OSS, " + "but was rejected with an error response for some reason."); System.out.println("Error Message:" + oe.getErrorMessage()); System.out.println("Error Code:" + oe.getErrorCode()); System.out.println("Request ID:" + oe.getRequestId()); System.out.println("Host ID:" + oe.getHostId()); } catch (ClientException | IOException ce) { System.out.println("Caught an ClientException, which means the client encountered " + "a serious internal problem while trying to communicate with OSS, " + "such as not being able to access the network."); System.out.println("Error Message:" + ce.getMessage()); } finally { if (ossClient != null) { ossClient.shutdown(); } } } }
成功的返回示例如下：
1. Bucket demo-1731651903982-4074 创建成功。 2. 文件 exampledir/exampleobject.txt 上传成功。 3. 下载的文件内容： Hello OSS 4. 列出 Bucket 中的文件： - exampledir/exampleobject.txt (大小 = 9) 5. 文件 exampledir/exampleobject.txt 删除成功。 6. Bucket demo-1731651903982-4074 删除成功。
## 其他语言
您也可以使用其他SDK语言，实现创建存储空间（Bucket）、上传文件（Object）、下载文件等操作。
[OSS Python SDK V2](../developer-reference/2-0-manual-preview-version.md)
[OSS Go SDK V2](../developer-reference/manual-for-go-sdk-v2.md)
[OSS PHP SDK V2](../developer-reference/manual-for-php-v2.md)
[OSS Node.js SDK](../developer-reference/nodejs-sdk.md)
[OSS C# SDK V2（预览版）](../developer-reference/oss-sdk-for-c-2-0.md)
[OSS C# SDK V1](../developer-reference/preface-4.md)
[OSS Java SDK V2（预览版）](../developer-reference/oss-sdk-for-java-2-0.md)
[OSS Java SDK V1](../developer-reference/oss-java-sdk.md)
[OSS Browser.js SDK](../developer-reference/browser-js.md)
[OSS Android SDK](../developer-reference/introduction.md)
[OSS iOS SDK](../developer-reference/preface-5.md)
[OSS Harmony SDK（预览版）](../developer-reference/harmony.md)
[OSS Swift SDK（预览版）](../developer-reference/oss-sdk-for-swift.md)
[OSS Ruby SDK](../developer-reference/ruby.md)
[OSS C++ SDK](../developer-reference/cpp.md)
[OSS C SDK](../developer-reference/preface-2.md)
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
