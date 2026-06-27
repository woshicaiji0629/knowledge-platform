# 解决Terraform添加CDN域名时的HTTPS配置报错-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/developer-reference/using-terraform-to-add-cdn-domain-name-results-in-https-configuration-error

# 使用Terraform添加CDN域名出现HTTPS配置报错
解决Terraform添加CDN域名时，出现HTTPS配置报错的问题。
## 问题现象
Terraform给出的报错日志如下：
│ Error: [ERROR] terraform-provider-alicloud/alicloud/resource_alicloud_cdn_domain_new.go:576: Resource public1.sige-test3.com SetCdnDomainSSLCertificate Failed!!! [SDK alibaba-cloud-sdk-go ERROR]: │ SDKError: │ StatusCode: 400 │ Code: SSLPri.MissingParameter │ Message: code: 400, The SSLPri parameter is required. request id: F5512B73-4FCE-56DD-8F05-19BA81C701F1 │ Data: {"Code":"SSLPri.MissingParameter","HostId":"cdn.aliyuncs.com","Message":"The SSLPri parameter is required.","Recommend":"https://api.alibabacloud.com/troubleshoot?intl_lang=EN_US&q=SSLPri.MissingParameter&product=Cdn&requestId=F5512B73-4FCE-56DD-8F05-19BA81C701F1","RequestId":"F5512B73-4FCE-56DD-8F05-19BA81C701F1"} │ │ with alicloud_cdn_domain_new.default, │ on main.tf line 1, in resource "alicloud_cdn_domain_new" "default": │ 1: resource "alicloud_cdn_domain_new" "default"
## 问题原因
在使用alicloud_cdn_domain_new新建CDN域名并且添加HTTPS证书的时候，客户在传参里面设置了cert_type参数，并且设置值为cas（表示使用阿里云证书中心的证书）。
在cert_type="cas"的情况下，若为阿里云国际站账号，则必须同时设置cert_region="ap-southeast-1"（国际的阿里云证书中心）；而阿里云中国站账号，则可以不设置，因为cert_region的默认值是cn-hangzhou（中国内地的阿里云证书中心）。
更多关于alicloud_cdn_domain_new的参数信息，敬请参见[alicloud_cdn_domain_new](https://help.aliyun.com/zh/terraform/alicloud-cdn-domain-new)。
## 解决方案
在使用alicloud_cdn_domain_new新建CDN域名且添加HTTPS证书的时候，当cert_type设置为"cas"时：
若当前账号是阿里云国际站账号，cert_region必填，且cert_region="ap-southeast-1"。
若当前账号不是阿里云国际账号，cert_region非必填，cert_region="cn-hangzhou"。
例如：
# 添加一个加速域名 resource "alicloud_cdn_domain_new" "domain" { domain_name = "mycdndomain.alicloud-provider.cn" cdn_type = "download" scope = "overseas" sources { content = "myoss.oss-rg-china-mainland.aliyuncs.com" type = "oss" priority = "20" port = 80 weight = "15" } # 证书配置 # cert_id 需现在阿里云证书中心购买或上传证书并记录其ID # cert_type=“cas” 表示使用阿里云证书中心的证书 # cert_regin = "ap-southeast-1" 表示使用国际站的阿里云证书中心 certificate_config { cert_id = "1111111" cert_name = "cert-2987438279834" cert_type = "cas" cert_region = "ap-southeast-1" } }
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
