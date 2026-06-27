# OSS与文件系统在数据模型上的差异及概念对比-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/comparison-between-oss-and-traditional-file-systems

# OSS与文件系统的对比
本文介绍OSS与文件系统在数据模型、数据获取等方面的差异对比以及概念对应关系。
## 差异对比
下表为OSS与文件系统在数据模型、数据获取、优势以及劣势的差异对比。
| 对比项 | OSS | 文件系统 |
| --- | --- | --- |
| 数据模型 | OSS 是一个分布式的对象存储服务，提供的是一个 Key-Value 对形式的对象存储服务。 | 文件系统是一种典型的树状索引结构。 |
| 数据获取 | 根据 Object 的名称（Key）唯一的获取该 Object 的内容。 虽然您可以使用类似 test1/test.jpg 的名称，但是这并不表示 Object 是保存在 test1 目录下。对于 OSS 来说， test1/test.jpg 仅仅只是一个字符串，与 example.jpg 并没有本质的区别。因此不同名称的 Object 之间的访问消耗的资源是类似的。 | 一个名为 test1/test.jpg 的文件，访问过程需要先访问到 test1 目录，然后再在该目录下查找名为 test.jpg 的文件。 |
| 优势 | 支持海量的用户并发访问。 | 支持文件的修改，例如修改指定偏移位置的内容、截断文件尾部等。也支持文件夹的操作，例如重命名目录、删除目录、移动目录等非常容易。 |
| 劣势 | OSS 保存的 Object 不支持修改（追加写 Object 需要调用特定的接口，生成的 Object 也和正常上传的 Object 类型上有差别）。用户即使只需要修改一个字节也需要重新上传整个 Object。 OSS 可以通过一些操作来模拟类似文件夹的功能，但是代价非常高。例如重命名目录，如果希望将 test1 目录重命名成 test2，则 OSS 的实际操作是将所有以 test1/ 开头的 Object 都重新复制成以 test2/ 开头的 Object，该操作会消耗大量的带宽、存储、计算、时间资源。因此在使用 OSS 时请尽量避免类似的操作。 | 受限于单个设备的性能。访问越深的目录消耗的资源也越大，操作拥有很多文件的目录也会非常慢。 |
从上述表格得知，不建议将OSS映射为文件系统。如果结合您的业务场景需要将OSS挂载为文件系统，建议只执行写入文件、删除文件、读取文件操作。使用OSS应该充分发挥其优点，即海量数据处理能力，优先用来存储海量的非结构化数据，例如图片、视频、文档等。
## 概念对应
下表为OSS与文件系统的概念对应说明。
| 对象存储 OSS | 文件系统 |
| --- | --- |
| Object | 文件 |
| Bucket | 主目录 |
| Region | 无 |
| Endpoint | 无 |
| AccessKey | 无 |
| 无 | 多级目录 |
| GetService | 获取主目录列表 |
| GetBucket | 获取文件列表 |
| PutObject | 写文件 |
| AppendObject | 追加写文件 |
| GetObject | 读文件 |
| DeleteObject | 删除文件 |
| 无 | 修改文件内容 |
| CopyObject （目标文件和源文件相同） | 修改文件属性 |
| CopyObject（目标文件和源文件不同） | 复制文件 |
| CopyObject+DeleteObject | 重命名文件 |
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
