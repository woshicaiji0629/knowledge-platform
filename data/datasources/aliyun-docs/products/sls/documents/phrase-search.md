# 短语查询的语法、使用限制和示例-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/phrase-search

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 短语查询

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍短语查询的语法、使用限制和示例。

## 概述

日志服务查询采用的是分词法，短语查询匹配的是分词后的词元序列及其相邻位置，不是对原始字符串做逐字符匹配。例如查询语句为abc def，将匹配所有包含abc和def的日志，不区分先后顺序，无法精准匹配目标短语。现在日志服务推出短语查询，用于精准匹配一段短语。

说明

如果短语中的标点符号属于当前索引配置的分词符，这些标点仅用于切分词元，不作为短语匹配内容。例如逗号#"aa,bb"、方括号#"[aa bb]"和空格#",aa bb,"均为分词符时，会被解析为相同的词元序列aa、bb，因此查询结果一致。若相关标点未配置为分词符，或字段使用了不同的分词配置，则查询结果可能不同。

日志服务接收到短语查询请求后，执行流程主要分为如下两步：

- 

先执行对应的非短语查询语句进行日志查询。例如执行#"abc def"语句，实际先执行"abc def"语句。

说明

为避免查询量太大，目前执行短语查询时，限制步骤1最多返回10,000条结果。

- 

在上述查询结果中再挑选符合短语查询条件的日志，并返回最终的查询结果。

## 语法

说明

- 

[SLS Query Skill 智能查询分析日志](products/sls/documents/sls-query-skill-intelligent-log-query-and-analysis.md)：日志服务提供了Agent Skill，支持在本地 AI Agent 中通过自然语言查询和分析 SLS 日志数据。

- 

[通过](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)：日志服务也提供了AI智能辅助SQL语句的使用，支持自然语言生成SQL、解释复杂SQL、优化SQL语句。

- 

字段查询

key:#"abc def"

- 

全文查询

#"abc def"

## 使用限制

- 

短语查询的结果只支持向前、向后的连续翻页，不支持随机跳转。

- 

执行短语查询后，日志分布直方图展示的是非短语查询的结果。

- 

短语查询不支持搭配模糊查询。

- 

短语查询语句中必须添加半角双引号（""）。

- 

短语查询语句中不支持搭配not语句，即不支持not #"abc def"。

- 

短语查询语句中不支持搭配分析语句，即不支持#"abc" | select ***。因此使用短语查询时，也不支持快速分析功能。

## 翻页说明

当您执行一次翻页操作时，日志服务会对应执行一次短语查询操作，用于保证查询结果的连续性。

短语查询每次最多查询10,000条日志，在翻页过程中，可能出现某页中显示的日志数量少于每页显示对应的数量，但仍支持向后翻页。即表示当前查询的10,000条日志中，满足短语查询条件的日志数量少于每页显示对应的数量。

例如日志总数为20,000条，每页支持显示100条，当您执行一次短语查询后，只返回89条且向后翻页功能可用，此时说明前10,000条日志中只有89条日志满足短语查询条件。您可以执行翻页操作，日志服务会自动在后10,000条日志中，执行第二次短语查询，并返回符合条件的日志。

## 示例

- 

例如您要查询包含redo_index/1的日志。

- 

使用非短语查询语句"redo_index/1"，日志服务将根据全文索引匹配部分关键词。在搜索栏中直接输入redo_index/1进行非短语查询时，日志服务会按分词符/拆分查询词，匹配到包含redo_index和1等词元的日志条目（如路径/redo_index/318/.../1/...、/redo_index/14912/.../1/...），返回大量非精确匹配结果。

- 

使用短语查询语句#"redo_index/1"，日志服务将匹配完整的短语redo_index/1。使用短语查询语句#"redo_index/1"，日志服务精确匹配包含完整字符串redo_index/1的日志记录，查询结果中日志条目的文件路径字段包含/redo_index/1/完整片段，表明短语查询未对该字符串进行分词拆分。

- 

例如您要查询包含02/Mar的日志（[调试](https://sls.aliyun.com/doc/playground/demo.html?dest=/lognext/project/nginx-demo-log/logsearch/nginx-access-log%3FslsRegion%3Dcn-shanghai%26isShare%3Dtrue%26queryString%3Drequest_time%20in%20%5B50%20100%5D)）。

- 

使用非短语查询语句time_local: 02/Mar，日志服务将根据全文索引匹配部分关键词。

查询结果中包含time_local值为01/Mar/2025:15:02:56的日志条目。该条目的日期实际为01/Mar而非02/Mar，但因为时间部分15:02:56中包含关键词02，且日期部分包含关键词Mar，两个关键词被分别匹配命中，因此该条目也被返回。

- 

使用短语查询语句time_local: #"02/Mar"，日志服务将匹配完整的短语02/Mar。

查询结果显示匹配到的日志中time_local字段值为02/Mar/2025:23:59:56，其中包含完整短语02/Mar，符合匹配预期。

[上一篇：查询语法与功能](products/sls/documents/query-syntax.md)[下一篇：LiveTail](products/sls/documents/livetail.md)

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
