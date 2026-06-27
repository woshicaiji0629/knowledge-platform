# 日志服务如何设置时序图-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/time-series-chart

# 时序图
时序图是为MetricStore定制的可视化图表，支持Prometheus查询数据结果的可视化，并支持多个查询结果同时显示。本文介绍设置时序图的操作步骤。
## 简介
时序图属于趋势类分析图表，一般用于展示一组数据在一个连续时间间隔上的变化情况，即直观地展示数据变化趋势。在时序图中，您可以清晰地观测到数据在某一个周期内的变化，例如：
递增性或递减性
增减的速率情况
增减的规律（如周期变化）
峰值和谷值
时序图是用于分析数据随时间变化趋势的最佳选择。您也可以绘制多条线用于分析多组数据在同一时间周期的变化趋势，进而分析数据之间的相互作用和影响（如同增同减，成反比等）。同时，日志服务时序图还支持数据的同环比，便于您查看数据在其他时间和当前时间的对比情况。
## 通用配置
通用配置用于对时序图进行全局配置。
基本配置
| 参数 | 说明 |
| --- | --- |
| 标题 | 设置时序图的标题。 |
| 显示标题 | 打开 显示标题 开关后，将在时序图中显示标题。 |
| 显示边框 | 打开 显示边框 开关后，将在时序图中显示边框。 |
| 显示背景 | 打开 显示背景 开关后，将在时序图中显示背景颜色。 |
| 显示时间 | 打开 显示时间 开关后，将在时序图中显示查询时间。 |
| 固定时间 | 打开 固定时间 开关后，将固定查询分析的时间，不受仪表盘全局时间的影响。 |
标准配置
| 参数 | 说明 |
| --- | --- |
| 格式化 | 设置数字的显示格式。 |
| 单位 | 设置数字的单位。 |
| 小数点后位数 | 设置数字的小数点后的位数。 |
| 显示名 | 修改图例的名称。 设置显示名后，该时序图中的所有图例名称都将变更为该值。如果您要修改某个图例的名称，可以使用字段配置。 |
| 颜色方案 | 选择时序图的颜色方案，用于设置时序图背景以及图例的颜色。 内置 ：使用内置颜色。 单色 ：使用您所选择的某个颜色。 |
数据配置
| 参数 | 说明 |
| --- | --- |
| 数据补全 | 打开 数据补全 开关后，日志服务会从第一个数据开始，按照补全窗口进行数据补全。 |
| 补全窗口 | 设置补全窗口。最小值为 0，单位：秒。 默认情况下，日志服务会自动定义补全窗口。 |
| 补全值 | 设置补全的内容。默认值为 0，表示将缺失的值设置为 0。 |
图例配置
| 参数 | 说明 |
| --- | --- |
| 显示图例 | 打开 显示图例 开关后，将在时序图中显示图例。 |
| 图例位置 | 设置图例的位置。 |
| 动作行为 | 设置图例的动作行为。 单选 ：单击某个图例时，时序图上只显示该图例对应的数据。 切换 ：单击某个图例时，时序图上隐藏该图例对应的数据，再次单击可取消隐藏。 |
| 最大宽度（高度）% | 设置图例的最大宽度和高度。 |
Tooltip配置
| 参数 | 说明 |
| --- | --- |
| 排序方式 | 设置数据的排序方式。 |
| 显示模式 | 设置数据的显示模式。 当您将鼠标悬浮在时序图上时，将根据您所设置的显示方式显示数据。 |
X轴配置
| 参数 | 说明 |
| --- | --- |
| 显示 x 轴 | 打开 显示 x 轴 开关后，将在时序图中显示 X 轴。 |
| x 轴标题 | 设置 X 轴的标题。 |
| 格式化 | 选择对应的格式，对 X 轴上的时间进行格式化处理。 |
| x 轴高度 | 设置 X 轴的高度。 默认情况下，日志服务会自动设置 X 轴的高度。 |
| 拖拽缩放目标 | 拖拽缩放目标后，支持刷新全局时间或当前单个图表时间。 |
Y轴配置
| 参数 | 说明 |
| --- | --- |
| 显示 y 轴 | 打开 显示 y 轴 开关后，将在时序图中显示 Y 轴。 |
| y 轴标题 | 设置 Y 轴的标题。 |
| y 轴位置 | 设置 Y 轴的位置。 |
| 是否堆叠 | 开启该功能后，将堆叠显示 Y 轴数据。 |
| y 轴宽度 | 设置 Y 轴的宽度。 默认情况下，日志服务会自动设置 Y 轴的宽度。 |
| 最大值 | 设置 Y 轴的最大值。 默认情况下，日志服务会自动设置 Y 轴的最大值。 |
| 最小值 | 设置 Y 轴的最小值。 默认情况下，日志服务会自动设置 Y 轴的最小值。 |
| 弹性最小值 | 设置 Y 轴的弹性最小值。当所有值都大于弹性最小值时，弹性最小值才会生效。 默认情况下，日志服务会自动设置 Y 轴的弹性最小值。 |
| 弹性最大值 | 设置 Y 轴的弹性最大值。当所有值都小于弹性最大值时，弹性最大值才会生效。 默认情况下，日志服务会自动设置 Y 轴的弹性最大值。 |
| y 轴 id | 设置 y 轴 ID。一般情况下该字段在 通用配置 中无意义，如果您要定义多个 Y 轴，需要在 字段配置 中进行配置。Y 轴 ID 可以为任意字符串。不同 ID 的 Y 轴在时序图上会显示不同的 Y 轴。更多信息，请参见 [添加多](create-a-line-chart-with-multiple-y-axes.md) [Y](create-a-line-chart-with-multiple-y-axes.md) [轴线图](create-a-line-chart-with-multiple-y-axes.md) 。 Y 轴 ID 的优先级高于 标准配置 中单位的配置。例如两个 Y 轴的单位相同时，会合并为一个 Y 轴。当两个 Y 轴的单位相同但 ID 不同时，会显示为两个 Y 轴。 |
图形配置
| 参数 | 说明 |
| --- | --- |
| 图形类型 | 选择时序图的类型。 |
| 连线方式 | 选择时序图的连线方式。 |
| 线宽 | 设置线的宽度。 |
| 显示点 | 设置显示点。 |
| 透明度 | 设置时序图的透明度。 |
| 点大小 | 设置时序图上点的大小。 |
| 渐变方式 | 设置时序图的渐变方式。 透明度 ：基于线条颜色，并受到 透明度 的影响。 不渐变 ：无渐变，使用线条颜色填充。 |
阈值
| 参数 | 说明 |
| --- | --- |
| 上界线 | 选择上界线。 |
| 下界线 | 选择下界线。 |
| 界线填充颜色 | 设置填充颜色。 |
| 界限填充透明度 | 选择颜色的透明度。 |
变量替换
| 参数 | 说明 |
| --- | --- |
| 变量替换 | 变量替换相当于为单个统计图表添加变量类型的过滤器。您在 通用配置 中设置了变量替换后，日志服务将在当前统计图表的左上边添加一个过滤器。您可以在过滤器中选择对应的值，日志服务会自动将查询和分析语句中的变量替换为您所选择的变量值，执行一次查询和分析操作。配置示例，请参见 [示例](user-guide/variables.md) [2：设置变量替换](user-guide/variables.md) 。 |
文档链接
| 参数 | 说明 |
| --- | --- |
| 添加文档链接 | 支持自定义设置文档链接或描述信息。设置后，相关信息将被展示在时序图的右上角。 |
## 字段配置
字段配置用于对单个查询分析的结果或单个查询分析结果中的单列数据进行个性化的可视化设置。字段配置中的配置项说明请参见[通用配置](time-series-chart.md)。
例如下述时序图展示不同主机的CPU使用率随时间的变化情况，每条线代表一台主机。如果您要为每条线自定义颜色，可使用字段配置。
## 交互事件
交互事件用于对单个字段或单个查询分析进行下钻分析，加深数据分析的维度。交互事件包括打开日志库、打开快速查询、打开仪表盘、打开Trace分析、打开Trace详情和自定义HTTP链接。更多信息，请参见[为仪表盘添加交互事件实现下钻分析](drill-down-events.md)。
例如A表示对查询分析A设置交互事件。将查询分析A的交互事件设置为打开日志库，则您单击线上的任意点，然后单击打开日志库，将跳转到您所设置的日志库中。
## 同比环比
日志服务时序图支持时序数据的同环比。例如在查询当前192.168.XX.XX主机的CPU使用率变化情况时，您要对比前一天同时段的CPU使用率变化情况，可单击图标，设置对应的时间。设置完成后，日志服务将自动展示对比结果。
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
