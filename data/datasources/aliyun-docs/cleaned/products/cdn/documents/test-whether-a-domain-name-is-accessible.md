# 在本地测试加速域名-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/test-whether-a-domain-name-is-accessible

# 模拟访问测试（可选）
您在CDN控制台成功添加加速域名后，为保证DNS解析可以顺利切换而不影响现有业务，建议您先在本地测试加速域名，验证加速域名访问正常后，再将加速域名的DNS解析记录指向CNAME域名。本文介绍如何在本地测试加速域名。
说明
模拟访问等同于正常的CDN访问，因此也会产生CDN基础服务和增值服务费用（如果测试的是增值服务），计费方式与正常使用CDN的计费方式相同。详细信息，请参见[计费组成](product-overview/billing-overview.md)。
## 前提条件
您已成功添加加速域名。如果未添加，请参见[添加加速域名](add-a-domain-name.md)完成添加。
您在域名管理中设置的源站业务可被正常访问。
## 操作步骤
获取加速域名的CNAME地址。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，复制加速域名对应的CNAME地址。
说明
请复制状态为正常运行的CNAME地址。
获取CNAME对应的IP地址。在命令行（CMD，PowerShell或终端）中使用nslookup命令查询CNAME地址，得到IP地址。
说明
以下通过nslookup命令得到的IP地址仅作为参考，实际以nslookup您的真实CNAME地址得到的IP地址为准。
nslookup xxx xxx w.kunlunle.com Server: 100 Address: 100.xxx.xxx.53 Non-authoritative answer: Name: xxx.p.kunlunle.com Address: 117.xxx.214 Name: flaskzx.zhang-xin.top.w.kunlunle.com Address: xxx:e:1:3::3fa
在本地电脑绑定hosts文件。
您需要将步骤2得到的IP地址和加速域名绑定到电脑本地hosts文件中，绑定顺序为IP地址在前，加速域名在后，顺序不能颠倒。
本文以加速域名为example.aliyundoc.com，生成的CNAME地址为example.aliyundoc.com.w.kunlunle.com，nslookup example.aliyundoc.com.w.kunlunle.com得到IP地址为192.168.0.1为例，为您介绍绑定方法。
### Windows系统
进入路径C:\Windows\System32\drivers\etc，使用记事本以管理员身份打开hosts文件。
编辑hosts文件。
文件内容可能类似如下：
# localhost name resolution is handled within DNS itself. # 127.0.0.1 localhost # ::1 localhost
在文件末尾添加获取到的IP地址和加速域名，例如：
192.168.0.1 example.aliyundoc.com
保存更改。
编辑完成后，选择文件>保存或按Ctrl + S保存更改。
（可选）刷新DNS缓存是为了确保DNS解析的更改立即生效。
打开命令提示符（以管理员身份运行），输入以下命令并按回车：
ipconfig /flushdns
## macOS系统
打开Terminal终端，使用以下命令以管理员权限打开hosts文件。
sudo vim /etc/hosts
您将被提示输入管理员密码，输入密码后按回车继续。
编辑hosts文件。
文件内容可能类似如下：
## # Host Database # # localhost is used to configure the loopback interface # when the system is booting. Do not change this entry. ## 127.0.0.1 localhost 255.255.255.255 broadcasthost ::1 localhost
在文件末尾添加获取到的IP地址和加速域名，例如：
192.168.0.1 example.aliyundoc.com
保存更改并退出。
按Esc键退出插入模式，然后输入:wq按回车，保存文件并退出vim。
（可选）刷新DNS缓存是为了确保DNS解析的更改立即生效。
在终端中输入以下命令并按回车：
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
测试加速域名是否访问正常。
成功绑定hosts文件后，您可以打开浏览器，在本地访问加速域名进行连通性测试，测试结果可通过浏览器自带的开发者工具查看。
如果Remote Address后的IP和您在hosts文件中绑定的IP一致，表示配置正确，您可以在域名解析服务商处配置CNAME。在开发者工具中切换到Network面板，选中目标请求后查看Headers信息。若Status Code为200 OK，表示连通性正常；同时关注Remote Address后的 IP 地址。
如果Remote Address后的IP和您在hosts文件中绑定的IP不一致，表示配置不正确，您需要检查hosts文件中绑定的IP地址是否正确，确保该IP地址是CNAME地址的IP。
成功访问加速域名后，如果您需要验证其它功能，可在电脑本地进行相应的验证。
## 后续步骤
[配置](add-a-cname-record-for-a-domain-name.md)[CNAME](add-a-cname-record-for-a-domain-name.md)：添加域名后，阿里云CDN会为您分配对应的CNAME域名，您需要完成CNAME配置，CDN服务才能生效。
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
