# 解决CDN回源配置不当导致的重定向次数过多-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/support/too-many-redirects-occur-after-my-domain-name-is-accelerated-by-alibaba-cloud-cdn

# CDN加速后提示重定向的次数过多的解决方案
## 问题描述
通过CDN加速后，访问加速域名提示：该网页无法正常运作，xxx将您重定向的次数过多。（报错：ERR_TOO_MANY_REDIRECTS）
## 常见原因
用户通过HTTPS协议（443端口）访问加速域名（如https://example.aliyun.com/）。
CDN以HTTP协议（80 端口）回源（如http://example.aliyun.com/）。
源站服务器（如Nginx）配置了HTTP到HTTPS的重定向规则，通过HTTP协议回源时，服务器会返回301/302状态码，并且将请求重定向到HTTPS协议的URL（例如https://example.aliyun.com/）。随后，客户端（如浏览器）会遵循跳转规则，通过HTTPS协议（默认端口443）重新发起请求，最终访问加速域名。
上述过程形成循环，超过浏览器单次请求允许的重定向次数后，浏览器终止请求并报错。
## 解决方案
如果您遇到的问题符合上述逻辑，您可以完成以下四步来解决您的问题。
### 步骤一：将源站回源端口设置为443
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在源站信息区域，选择编辑源站配置。
将源站的端口信息改为443，然后点击确定。
### 步骤二：修改回源协议类型为跟随
如果没有开启回源协议功能，则可以忽略此步骤。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
在配置页签中，找到回源协议区域，点击修改配置。
协议类型选择跟随，然后点击确定。
### 步骤三：对资源的缓存进行刷新
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击刷新预热。
操作类型选择刷新，操作方式选择目录。
在URL中填写您的根目录地址（例如，若加速域名为https://www.example.com/image/static/1.png，那么您需要在此处填写的URL为https://www.example.com/。此处需要注意，目录刷新的URL必须以https://或http://开头，以/结尾）。
点击提交，开始缓存刷新的任务。
在操作记录中可以看到缓存刷新任务的进度。
### 步骤四：清除本地浏览器缓存
此处以Chrome浏览器为例作为演示。
在Chrome浏览器右上角，依次点击“更多”图标删除浏览数据。
选择时间范围，例如过去一小时或时间不限。
选择要移除的信息的类型（缓存的图片和文件为必选项，其他选项为可选项）。
点击删除数据。
## 验证步骤
您可以通过以下方式验证：
使用curl -I 加速域名（例如：curl -I https://www.example.com/image/static/1.png）检查响应头是否包含Location跳转信息。如果响应头不包含Location，说明问题已解决。
或者，使用浏览器无痕模式直接访问加速域名进行验证，如果能够正常访问，说明问题已解决。
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
