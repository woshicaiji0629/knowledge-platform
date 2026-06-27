# 共享自定义镜像用于同地域跨账号部署ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/share-a-custom-image

# 共享自定义镜像
自定义镜像支持在多个阿里云账号或企业组织内的相同地域下共享使用，在快速部署一致的应用环境的同时，避免重复构建镜像。
## 适用范围
仅支持同地域跨账号共享。
当前账号只能共享自己创建的自定义镜像，其他阿里云账号共享给当前账号的镜像无法再次共享。
不支持在中国站和国际站阿里云账号之间共享基于云市场镜像创建的自定义镜像。
## 共享方式
| 共享方式 | 适用场景 | 优势 | 限制与说明 |
| --- | --- | --- | --- |
| 共享给指定账号 | 向少量、固定的合作伙伴或个人账号共享镜像。 | 操作简单。 | 需手动管理接收方账号 ID。 |
| 在企业组织内共享 | 通过 [资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/product-overview/resource-directory-overview#concept-2436329) 向整个组织或特定资源夹下的成员账号动态共享镜像 | 成员加入或退出组织时，自动同步共享权限，便于集中管理。 | 依赖资源目录服务 [进行资源共享](https://help.aliyun.com/zh/resource-management/resource-sharing/product-overview/resource-sharing-overview#title-c0b-k4s-aup) 。共享方的阿里云账号需满足如下任一条件： 未开通资源目录但已是资源目录的成员。 已经过 [企业实名认证](https://help.aliyun.com/zh/account/verify-your-identity-enterprise-account/) 并 [开通资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/enable-a-resource-directory) 且已 [启用资源目录组织共享](https://help.aliyun.com/zh/resource-management/resource-sharing/user-guide/enable-resource-sharing) 。 |
## 准备工作
在执行镜像共享前，应完成必要的准备和安全检查，以保障数据安全与权限合规。
获取接收方信息：
共享给指定账号：需提前获取被共享方的阿里云账号的主账号ID。
在企业组织内共享：需确保账号已启用资源目录并开启资源共享功能。
清理镜像敏感数据：为防止数据泄露，共享前必须清理镜像中的敏感信息。建议在制作镜像前移除历史记录、SSH密钥、网络配置、临时文件及各类访问凭证非必要数据。
（条件必选）共享加密镜像授权准备：需参见[跨账号共享加密资源](encryption-related-permissions.md)创建AliyunECSShareEncryptImageDefaultRole角色并授权。
## 操作步骤
### 场景一：共享给指定阿里云账号
## 控制台
单击[ECS](https://ecs.console.aliyun.com/image)[控制台-镜像](https://ecs.console.aliyun.com/image)，选择目标资源所在的资源组和地域。
在自定义镜像页签，找到待共享的自定义镜像，在操作列单击共享镜像。
在共享镜像弹窗中，完成以下配置：
在对端待共享账号 ID处输入被共享方的阿里云账号ID。
阅读并确认安全确认信息后勾选，单击确定。
## API
可以调用API接口[管理镜像共享权限](../developer-reference/api-ecs-2014-05-26-modifyimagesharepermission.md)将当前阿里云账号的自定义镜像共享给其他阿里云账号。
### 场景二：在企业组织内共享
单击[ECS](https://ecs.console.aliyun.com/image)[控制台-镜像](https://ecs.console.aliyun.com/image)，选择目标资源所在的资源组和地域。
在自定义镜像页签，找到待共享的自定义镜像，在操作列单击共享镜像。
在共享对象类型处单击组织内共享跳转到[资源共享控制台](https://resourcemanager.console.aliyun.com/resource-share)，参见[创建共享单元](https://help.aliyun.com/zh/resource-management/resource-sharing/user-guide/create-a-resource-share-1#task-2436332)完成共享操作，需要共享的资源需选择ECS镜像。
仅开通了资源目录的管理账号或成员账号才可以进行组织内共享，若页面看不到组织内共享入口，请先[开通资源目录](https://help.aliyun.com/zh/document_detail/183645.html#task-2152699)。
重要
已通过资源目录共享的镜像，不应再通过共享给指定阿里云账号的方式重复分享给相同的账号，避免造成资源目录中镜像共享数据不一致的问题。
## 费用说明
共享镜像不收取共享功能费用，但当共享镜像的最终来源为付费镜像，且被共享方使用该镜像创建ECS实例情况下，会向被共享方收取共享镜像的使用费用。
例如：源镜像A是付费镜像，阿里云账号A把该镜像共享给阿里云账号B，阿里云账号B使用该共享镜像创建了实例，则阿里云账号B除实例资源费用外需要支付镜像的费用。
## 使用限制
可共享的账号数量受配额限制。共享行为不占用接收方的自定义镜像额度。具体限额可通过[配额中心](https://quotas.console.aliyun.com/products/ecs/quotas?spm=a2c4g.11186623.0.0.376656addmG73f)查询每个自定义镜像能够共享用户数限额项查看和[调整配额](quota-management.md)。
ECS不支持将自定义镜像共享给轻量应用服务器使用。但轻量应用服务器创建的自定义镜像支持[共享镜像到](https://help.aliyun.com/zh/simple-application-server/user-guide/share-a-custom-image)[ECS](https://help.aliyun.com/zh/simple-application-server/user-guide/share-a-custom-image)使用。
## 常见问题
如何查看已共享镜像的共享对象？
## 控制台
镜像共享成功后，在自定义镜像页签，将鼠标悬浮至共享镜像的图标处，可以查看共享对象的阿里云账号ID。
## API
可以调用API接口[DescribeImageSharePermission](../api-describeimagesharepermission.md)查询自定义镜像已经共享的所有用户。
如何跨地域共享镜像？
需参考[复制自定义镜像](copy-an-image.md)，将待共享镜像复制到目标地域后再共享。
如何删除共享中的镜像？
共享中的镜像不支持直接删除，需要先[取消共享镜像](unshare-custom-images.md)，才能删除。
如何查看阿里云账号主账号的ID？
将鼠标移至控制台右上角的用户头像，在弹出的用户信息框中，如果标识的账号为主账号，则显示的账号ID即为阿里云账号ID。
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
