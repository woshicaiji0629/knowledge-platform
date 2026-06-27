# DashScope SDK连接复用配置-大模型服务平台百炼(Model Studio)-阿里云帮助中心

Source: https://help.aliyun.com/zh/model-studio/connection-multiplexing-configuration

# DashScope SDK连接复用配置
在调用大模型服务时，高并发场景下可能会出现请求超时、资源消耗大等问题。为解决这些问题，可通过连接复用优化网络连接的使用效率。
## 连接复用
DashScope SDK 支持通过复用已有的连接来减少资源消耗，提高请求处理效率。
Java SDK：内置连接池机制，支持配置连接数、超时时间等参数，默认启用。
Python SDK：支持通过传入自定义 Session 实现连接复用，包括同步和异步两种方式。
## Java SDK
DashScope Java SDK 内置了连接池机制，默认启用。建议您根据具体业务合理调整连接池的连接数和超时时间，优化连接复用效果。
### 配置参数说明
| 参数 | 含义 | 默认值 | 单位 | 备注 |
| --- | --- | --- | --- | --- |
| connectTimeout | 建立连接的超时时间。 | 120 | 秒 | 在低延迟场景中，通常需要设置较短的连接超时时间，以减少等待时间，提高响应速度。 |
| readTimeout | 读取数据的超时时间。 | 300 | 秒 |  |
| writeTimeout | 写入数据的超时时间。 | 60 | 秒 |  |
| connectionIdleTimeout | 连接池中空闲连接的超时时间。 | 300 | 秒 | 在高并发场景下，适当延长空闲连接超时时间，有利于避免频繁创建连接，从而降低资源消耗。 |
| connectionPoolSize | 连接池中的最大连接数。 | 32 | 个 | 在高并发场景下： 连接数过低时，可能导致请求阻塞或超时，或者频繁创建连接，增加资源消耗； 连接数过高时，可能导致服务端负载过大。 建议根据业务需求调整配置。 |
| maximumAsyncRequests | 最大并发请求数。全局的并发请求数限制（包含所有主机）。需要小于或等于最大连接数，否则可能出现请求阻塞的情况。 | 32 | 个 |  |
| maximumAsyncRequestsPerHost | 单台主机的最大并发请求数。需要小于或等于最大并发请求数。 | 32 | 个 |  |
### 代码示例
运行代码前，请[配置](first-api-call-to-qwen.md)[API Key](first-api-call-to-qwen.md)[到环境变量](first-api-call-to-qwen.md)并[安装最新版](install-sdk.md)[SDK](install-sdk.md)。
以下代码示例展示了如何配置连接池相关参数（如超时时间、最大连接数等），并调用大模型服务。您可以根据实际需求调整相关参数，以优化并发性能和资源利用率。
// 建议DashScope SDK的版本 >= 2.12.0 import java.time.Duration; import java.util.Arrays; import com.alibaba.dashscope.aigc.generation.Generation; import com.alibaba.dashscope.aigc.generation.GenerationParam; import com.alibaba.dashscope.aigc.generation.GenerationResult; import com.alibaba.dashscope.common.Message; import com.alibaba.dashscope.common.Role; import com.alibaba.dashscope.exception.ApiException; import com.alibaba.dashscope.exception.InputRequiredException; import com.alibaba.dashscope.exception.NoApiKeyException; import com.alibaba.dashscope.protocol.ConnectionConfigurations; import com.alibaba.dashscope.utils.Constants; public class Main { public static GenerationResult callWithMessage() throws ApiException, NoApiKeyException, InputRequiredException { Generation gen = new Generation(); Message systemMsg = Message.builder() .role(Role.SYSTEM.getValue()) .content("You are a helpful assistant.") .build(); Message userMsg = Message.builder() .role(Role.USER.getValue()) .content("你是谁？") .build(); GenerationParam param = GenerationParam.builder() // 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key // 若没有配置环境变量，请用百炼API Key将下行替换为：.apiKey("sk-xxx") .apiKey(System.getenv("DASHSCOPE_API_KEY")) // 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models .model("qwen-plus") .messages(Arrays.asList(systemMsg, userMsg)) .resultFormat(GenerationParam.ResultFormat.MESSAGE) .build(); System.out.println(userMsg.getContent()); return gen.call(param); } public static void main(String[] args) { // 连接池配置 Constants.connectionConfigurations = ConnectionConfigurations.builder() .connectTimeout(Duration.ofSeconds(10)) // 建立连接的超时时间, 默认 120s .readTimeout(Duration.ofSeconds(300)) // 读取数据的超时时间, 默认 300s .writeTimeout(Duration.ofSeconds(60)) // 写入数据的超时时间, 默认 60s .connectionIdleTimeout(Duration.ofSeconds(300)) // 连接池中空闲连接的超时时间, 默认 300s .connectionPoolSize(256) // 连接池中的最大连接数, 默认 32 .maximumAsyncRequests(256) // 最大并发请求数, 默认 32 .maximumAsyncRequestsPerHost(256) // 单个主机的最大并发请求数, 默认 32 .build(); try { GenerationResult result = callWithMessage(); System.out.println(result.getOutput().getChoices().get(0).getMessage().getContent()); } catch (ApiException | NoApiKeyException | InputRequiredException e) { // 使用日志框架记录异常信息 System.err.println("An error occurred while calling the generation service: " + e.getMessage()); } System.exit(0); } }
## Python SDK
DashScope Python SDK 支持通过传入自定义 Session 实现连接复用，提供[HTTP](connection-multiplexing-configuration.md)[异步](connection-multiplexing-configuration.md)（协程）和[HTTP](connection-multiplexing-configuration.md)[同步](connection-multiplexing-configuration.md)两种调用方式。
### HTTP异步调用方式
在异步调用场景中，您可以通过aiohttp.ClientSession配合aiohttp.TCPConnector实现连接复用。TCPConnector支持配置连接数限制等参数：
| 参数 | 含义 | 默认值 | 备注 |
| --- | --- | --- | --- |
| limit | 总连接数限制 | 100 | 控制最大连接数。在高并发场景下，适当增加此值可以提高并发能力。 |
| limit_per_host | 每个主机的连接数限制 | 0（无限制） | 限制对单个主机的最大连接数，避免对单一服务端造成过大压力。 |
| ssl | SSL 上下文配置 | None | 用于 HTTPS 连接的 SSL 证书验证配置。 |
代码示例
运行代码前，请[配置](first-api-call-to-qwen.md)[API Key](first-api-call-to-qwen.md)[到环境变量](first-api-call-to-qwen.md)并[安装最新版](install-sdk.md)[SDK](install-sdk.md)。
以下代码示例展示了如何在异步场景下配置连接复用，并调用大模型服务：
import asyncio import aiohttp import ssl import certifi from dashscope import AioGeneration import dashscope import os async def main(): # 以下为华北2（北京）地域的URL，各地域的URL不同。 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx" dashscope.api_key = os.getenv("DASHSCOPE_API_KEY") # 配置连接参数 connector = aiohttp.TCPConnector( limit=100, # 总连接数限制 limit_per_host=30, # 每个主机的连接数限制 ssl=ssl.create_default_context(cafile=certifi.where()), ) # 创建自定义Session并传入调用方法 async with aiohttp.ClientSession(connector=connector) as session: response = await AioGeneration.call( model='qwen-plus', prompt='你好，请介绍一下你自己', session=session, # 传入自定义 Session ) print(response) asyncio.run(main())
### HTTP同步调用方式
在同步调用场景中，您可以通过requests.Session实现连接复用。在同一个 Session 内的多次请求会复用底层 TCP 连接，避免重复建立连接的开销。
代码示例
运行代码前，请[配置](first-api-call-to-qwen.md)[API Key](first-api-call-to-qwen.md)[到环境变量](first-api-call-to-qwen.md)并[安装最新版](install-sdk.md)[SDK](install-sdk.md)。
以下代码示例展示了如何在同步场景下配置连接复用，并调用大模型服务：
import requests from dashscope import Generation import dashscope import os # 以下为华北2（北京）地域的URL，各地域的URL不同。 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx" dashscope.api_key = os.getenv("DASHSCOPE_API_KEY") # 使用 with 语句确保 Session 正确关闭 with requests.Session() as session: response = Generation.call( model='qwen-plus', prompt='你好', session=session # 传入自定义 Session ) print(response)
如果需要在多次调用中复用同一个 Session，可以采用以下方式：
import requests from dashscope import Generation import dashscope import os # 以下为华北2（北京）地域的URL，各地域的URL不同。 dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1' # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key # 若没有配置环境变量，请用百炼API Key将下行替换为：dashscope.api_key = "sk-xxx" dashscope.api_key = os.getenv("DASHSCOPE_API_KEY") # 创建 Session 对象 session = requests.Session() try: # 多次调用复用同一个 Session response1 = Generation.call( model='qwen-plus', prompt='你好', session=session ) print(response1) response2 = Generation.call( model='qwen-plus', prompt='介绍一下你自己', session=session ) print(response2) finally: # 确保 Session 正确关闭 session.close()
## 最佳实践
Java SDK：根据业务并发量合理配置connectionPoolSize、maximumAsyncRequests等参数，避免连接数过高或过低。
Python SDK：推荐使用with语句自动管理 Session 的生命周期，确保资源正确释放。
选择合适的调用方式：如果您的应用是异步架构（如使用 asyncio、FastAPI 等），建议使用异步调用方式；如果是传统同步架构，使用同步调用方式即可。
## 错误码
如果模型调用失败并返回报错信息，请参见[错误码](error-code.md)进行解决。
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
