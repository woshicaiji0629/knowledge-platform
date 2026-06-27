# 通过标签对专有网络、路由表和交换机进行标记和分类-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/manage-vpc-tags

# 管理标签
使用[标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)标记并分类 VPC，建立业务视角的资源视图，便于资源的搜索和聚合。[便于资源的搜索和聚合](https://help.aliyun.com/zh/resource-management/tag/user-guide/use-tag-for-automated-operations)。
[标签设计示例](https://help.aliyun.com/zh/resource-management/tag/use-cases/best-practices-for-tag-design)。
## 适用范围
配额：单个 VPC、交换机和路由表支持绑定的标签数量均为 20 个，暂不支持提升配额。
安全：严禁在标签中存放敏感信息（如密码、AK/SK），标签信息可能会在账单中明文显示。
规范：
每个标签都由一对键值对（Key-Value）组成。标签键/值区分大小写，不支持aliyun、acs:、http://、https://前缀。
一个实例上的每条标签的标签键（Key）必须唯一。
不支持未绑定实例的空标签存在，标签必须绑定在实例上。
不同地域中的标签信息不互通。 例如，在华东1（杭州）地域创建的标签在华东2（上海）地域不可见。
支持修改标签的键和值，以及删除实例的标签。删除实例时，其绑定的所有标签都会被删除，但不会影响其他实例绑定的标签。
## 添加/删除标签
### 控制台
单个管理：前往[专有网络控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/vpcs)，将鼠标悬停在目标实例标签列的图标，单击气泡框中的绑定或编辑。针对需要删除的标签键值对，单击其右侧的图标。
如果未显示标签列，可通过 VPC 列表右上方设置展示标签列表项。
批量管理：选中需要批量添加/删除标签的 VPC，在页面左下方选择设置标签>批量添加标签或设置标签>批量删除标签。
精准检索：在列表上方单击标签筛选，选择或输入键值对，即可过滤出符合筛选条件的 VPC。
### API
调用[TagResources](developer-reference/api-vpc-2016-04-28-tagresources.md)为指定的资源统一创建并绑定标签。
调用[UnTagResources](developer-reference/api-vpc-2016-04-28-untagresources.md)为指定的资源列表统一解绑标签。
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
