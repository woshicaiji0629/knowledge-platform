# 如何使用日志服务中的仪表盘-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/dashboard-real-time-monitoring-and-visualization

# 使用仪表盘
日志服务可视化是将系统、应用或服务生成的原始日志数据转换成图形化界面展示的过程。本文介绍如何使用仪表盘。
## 预期效果
日志服务仪表盘包含丰富的图表类型，可以灵活地设置图表样式，以满足各类场景对展示数据的不同需求。
## 查看仪表盘列表
在日志服务中，图标代表仪表盘，图标代表仪表盘列表，图标代表演示列表。
### 仪表盘列表
单击仪表盘>仪表盘列表，查看当前Project下的所有仪表盘。
### 演示列表
单击仪表盘>演示列表，查看当前Project下的所有演示列表。
## 仪表盘模式
### 显示模式
查看仪表盘时，系统默认呈现显示模式，允许您浏览该仪表盘下的所有统计图表。此外，日志服务还提供了在显示模式下对仪表盘进行刷新、订阅及分享等操作的功能。
在显示模式下，右键单击统计图表可弹出上下文菜单，包含查看、创建免密分享、预览查询语句、选择时间范围、另存为告警、下载图表、下载图表数据等操作。
显示模式操作说明
| 区域 | 操作说明 |
| --- | --- |
| 仪表盘列表区域 | 单击 仪表盘 > 仪表盘列表 ，可以看到当前 Project 下所有的仪表盘。单击目标仪表盘，进入到显示模式。 |
| 操作区域 | 时间选择 ：您可以 [设置仪表盘的查询时间](dashboard-real-time-monitoring-and-visualization.md) ， 设置后，所有统计图表展示的是同一时段的查询和分析结果。 SQL 增强 ：您可以运行 SQL 增强，用于优化查询分析语句。 刷新 ：您可以通过 [手动刷新或自动刷新](dashboard-real-time-monitoring-and-visualization.md) 两种方式刷新仪表盘。 重置 ：重置所有图表的查询时间范围，恢复至默认时间范围，用于改变时间范围后还原到初始状态的场景。 告警 ：您可以为图表 [创建告警规则](alarm-settings-quick-start.md) 。 订阅 ： [订阅仪表盘](dashboard-real-time-monitoring-and-visualization.md) 后， 您可以定期将仪表盘渲染为图片，通过邮件、钉钉等方式发送给指定人员。 另存为 ： 复制并保存为目标仪表板的新独立版本，完成后刷新页面，在仪表盘列表中查看。 分享 ：您可以将仪表盘 [免密分享](secret-free-sharing-and-integrated-dashboard.md) 给其他人。 全屏 ：您可以选择 显示器全屏 或者 窗口全屏 ，当您不需要全屏展示时，您可以按 Esc 键退出全屏。 仪表盘体验调研 ：反馈您宝贵的意见。 编辑 ：进入仪表盘编辑模式。 |
| 过滤器 | 当您为仪表盘 [添加过滤器](user-guide/add-a-filter.md) 后，仪表盘会显示您创建的过滤器。 |
| 图表区域 | 单击 对单个图表可以进行窗口放大 查看 、 创建免密分享 、 预览查询语句 、 选择时间范围 、 另存为告警 、以 PNG 图片格式 下载图表 或者以 CSV 格式 下载图表数据 。 |
### 编辑模式
单击仪表盘页面的编辑进入编辑模式后，您能够进行如下操作：修改仪表盘名称、添加新图表、调整布局、编辑现有图表以及导入图表等。
编辑模式下，单击图表卡片右上角的三点图标，可展开包含编辑、复制、删除三个选项的上下文菜单，用于对单个图表进行操作。
编辑模式操作说明
| 区域 | 操作说明 |
| --- | --- |
| 仪表盘列表区域 | 单击 仪表盘 > 仪表盘列表 ，可以看到当前 Project 下所有的仪表盘。单击目标仪表盘，在仪表盘右上角单击 编辑 进入编辑模式。 |
| 操作区域 | 撤销 ：取消最近一次对图表的修改，恢复到上一次保存或操作的状态。 重做 ：撤销后的反向操作，恢复最近一次被撤销的修改。 层级置顶 ：将选中的图表提升到所有元素之上，确保它显示在最前面。 层级置底 ：将选中的图表放置到所有元素之下，使其显示在最底层。 设置对齐方式 ：调整图表的对齐方式，如左对齐、右对齐等。 设置图表位置和大小 ：调整图表左边距、上边距、高度和宽度。 过滤器 ：通过 [添加过滤器](dashboard-real-time-monitoring-and-visualization.md) 可对整个仪表盘进行查询过滤。 删除 ：当您选中一个或多个图表时，可批量删除。 添加 ：您可以为仪表盘添加 图表 、 连线 和 图形 。 图表 ：单击 添加新图表 ，为仪表盘添加 [统计图表（Pro](user-guide/overview-of-charts.md) [版本）](user-guide/overview-of-charts.md) 或 [统计图表](chart-overview.md) 。 连线 ：选择 连线类型 、 线条样式 、 线宽 及 线条颜色 。您可以为图表间添加并设置连线， 图形 ：为仪表盘添加 矩形 、 菱形 、 文本 或 自定义 SVG 。 导入图表 ：向当前仪表盘导入新图表。 切换布局 ：日志服务中仪表盘支持 网格布局 和 自由布局 两种布局模式，您可以自由切换。 历史版本 ：您可以查看仪表盘的历史操作，如果您误操作了仪表盘，则可以使用此功能将其恢复到历史版本。 重要 支持最多保存 20 个历史版本。 不支持通过 API 方式操作历史版本。 恢复操作将覆盖当前仪表盘内容，请谨慎操作。 设置 ：在仪表盘设置页面，可以恢复旧版本、修改仪表盘 JSON 和管理过滤器。 保存 ：编辑模式下的所有操作，都必须保存后才会生效。 取消 ：退出编辑模式。 |
| 图表区域 | 单击 对单个图表进行编辑、复制和删除。 |
## 使用仪表盘
### 刷新仪表盘
您可以通过手动或自动两种方式刷新仪表盘，具体操作如下。
在仪表盘页面的右上方，选择刷新>仅一次，表示立即刷新一次仪表盘。
在仪表盘页面的右上方，选择刷新>自动刷新，表示按照指定的时间间隔自动刷新仪表盘。时间间隔可设置为15秒、60秒、5分钟或15分钟。
### 查询仪表盘
您可以全局设置仪表盘的查询时间范围，设置后，所有统计图表展示的是同一时段的查询和分析结果。
重要
选定的查询时间范围仅供临时查看结果，系统不会保存。下次查看仪表盘时，系统仍使用默认的时间范围。
时间选择
在仪表盘页面的上方，单击时间选择，选择时间范围。选择时间范围后，将鼠标放在时间上，可查看具体的时间范围。
| 时间选择 | 说明 |
| --- | --- |
| 相对时间 | 表示查询距离当前时间 1 分钟、5 分钟、15 分钟等时间区间的日志数据。例如当前时间为 19:20:31，设置相对时间 1 小时，表示查询 18:20:31~19:20:31 的日志数据。 |
| 整点时间 | 表示查询最近整点 1 分钟、15 分钟等时间区间的日志数据。例如当前时间为 19:20:31，设置整点时间 1 小时，表示查询 18:00:00~19:00:00 的日志数据。 |
| 自定义时间 | 表示查询指定时间范围的日志数据。 |
查看特定条件的仪表盘
在仪表盘页面的上方，单击时间选择，选择时间范围后，再单击仪表盘过滤器，添加过滤条件，表示查询指定时间和指定条件下的日志数据。例如当前是2024-09-06日，设置时间为昨天（相对），添加method为GET，status为200的过滤条件，表示查询2024-09-05 00:00:00 ~ 2024-09-06 00:00:00内method为GET，status为200的日志数据。
### 分享仪表盘
创建仪表盘后，您可以分享到钉钉、企业微信或阿里云账号，也可以将仪表盘嵌入钉钉文档。具体操作，请参见[免密分享与集成仪表盘](secret-free-sharing-and-integrated-dashboard.md)。
### 订阅仪表盘
创建仪表盘后，您可以定期将仪表盘渲染为图片，通过邮件、钉钉等方式发送给指定人员。
重要
订阅仪表盘，有如下限制：
每个仪表盘只能创建一个订阅任务。
每天最多给每个邮箱发送50封邮件。
每个Project中订阅任务和告警任务的总数最多100个。如果有特殊需求，请提[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)申请调整限额。
如果表格分页显示，订阅仪表盘时，仅支持发送表格第一页的数据截图。
跨Project数据不支持订阅，如果仪表盘所查询的数据来源于另一个Project，订阅功能无法获取到这些数据。
参数说明
| 参数 | 说明 |
| --- | --- |
| 订阅名称 | 订阅任务的名称。 |
| 频率 | 订阅仪表盘后，发送通知的频率。 每小时 ：每小时发送一次订阅通知。 每天 ：在每天的某个固定时间点发送一次订阅通知。 每周 ：在周几的某个固定时间点发送一次订阅通知。 固定间隔 ：按固定间隔发送订阅通知，单位为天。 Cron ：通过 Cron 表达式指定时间间隔，Cron 表达式最小单位为分钟，但建议设置间隔为 1 小时以上。例如 Cron 表达式为 * 0/1 * * * ，表示从 0 点开始，每隔 1 小时发送一次。 |
| 全局时间 | 预设 ：发送订阅报表时，对应的查询时间范围为仪表盘中统计图表的查询时间范围。 说明 在仪表盘显示模式下，所有的查询时间范围都是临时的，仅供您动态查阅不同时间段的图表数据。 在仪表盘编辑模式下，双击目标统计图表，然后在编辑页面，修改其查询时间范围。系统会保存该时间范围，即您下次查看该统计图表时，仍为该时间范围。 自定义 ：发送订阅报表时，对应的查询时间范围为您在此处设置的自定义时间范围。 |
| 添加水印 | 在生成的图片上添加水印，水印内容为通知渠道地址，例如邮箱地址。 |
| 通知列表 | 订阅仪表盘的通知方式包括邮件、Webhook-钉钉机器人、Webhook-飞书机器人、Webhook-企业微信机器人和自定义 Webhook。 邮件 在 收件人 中填写邮箱地址，多个邮箱地址之间用英文逗号（,）分隔。 在 主题 中配置邮件主题。如果没有配置主题，日志服务将使用默认主题（日志服务报表）。 Webhook 在 请求地址 中填写对应的 WebHook 地址。 如何获取钉钉机器人的 WebHook 地址，请参见 [通知渠道说明](notification-methods.md) 。 在 标题 中配置通知标题。 |
### 为仪表盘添加过滤器
为目标仪表盘添加过滤器后，您可以根据指定条件对仪表盘中的所有统计图表进行筛选，无需修改查询分析语句。具体操作，请参见[添加过滤器](add-filter.md)。
### 播放仪表盘
创建演示列表：当前Project中没有演示列表时，有2个入口可以创建，您可以单击立即创建或者进行创建。
在创建演示列表对话框中，完成如下配置，然后单击确定。
| 参数 | 说明 |
| --- | --- |
| 播放列表名称 | 设置播放列表的名称。 |
| 轮播间隔时间 | 设置仪表盘轮播的时间间隔。 |
| 目标仪表盘名称 | 添加目标仪表盘。支持跨 Project 添加仪表盘。 |
播放仪表盘：选择目标演示列表，单击右上角播放按钮，系统将根据您设置的时间间隔，自动播放您所添加的仪表盘。您也可以单击上一页、下一页，手动播放仪表盘。
工具栏还包含时间选择和编辑按钮。
### 下钻分析
在仪表盘发现异常时，可以利用[为仪表盘添加交互事件实现下钻分析](drill-down-events.md)功能快速进行下钻分析，如在LogStore查询分析、Trace分析或访问其他仪表盘等，以实现定位异常根因。具体操作，请参见[使用仪表盘下钻分析定位异常根因](user-guide/use-instrument-cluster-drill-in-analysis-to-locate-the-root-cause.md)。
## 支持的图表类型
### 表格（Pro版本）
表格由一组或多组单元格组成，表格中的项被组织为行和列，表格的第一行称为表头，指明表格每一列的内容和意义。例如查询每个http_referer对应的响应体总字节数，并用线图展示body_bytes_sent。
(*)| SELECT http_referer, array_agg(body_bytes_sent) as body_bytes_sent GROUP BY http_referer
使用场景：[表格](table.md)能够精确地展示每个数据项的具体数值。适用于数据分析、财务报表、科学实验记录等场景。
### 线图（Pro版本）
线图属于趋势类分析图表，一般用于表示一组数据在一个有序数据类别（多为连续时间间隔）上的变化情况，用于直观分析数据变化趋势。例如查询每个时间点的页面访问量（PV），并设置上下浮动范围展示。
(*)| select __time__ - __time__ % 60 as time, COUNT(*) as pv, COUNT(*) + 50 as pv2, COUNT(*) - 50 as pv3 GROUP BY time order by time
使用场景：[线图](line-chart.md)主要用于展示数据随时间或其他连续变量的变化趋势。适用于分析时间序列数据，如股票价格、气温变化、销售数据等场景。在线图中，可以清晰地观测到数据在某一个周期内的变化，例如：
递增性或递减性
增减的速率情况
增减的规律（如周期变化）
峰值和谷值
### 柱状图（Pro版本）
柱状图使用垂直的柱子显示类别之间的数值比较，用于描述分类数据，并统计每一个分类中的数量。例如展示UV最高的前5个host及其页面访问量（PV）。
(*)| select host, COUNT(*) as pv, approx_distinct(remote_addr) as uv GROUP BY host ORDER BY uv desc LIMIT 5
使用场景：[柱状图](column-chart.md)主要用于比较不同类别或不同时间点的数据大小。适用于展示分类数据，如不同产品的销售量、不同地区的人口数量等。
### 统计图（Pro版本）
统计图可包含一个或多个单值图，单值图可用于突出显示单个数值。例如展示最近15分钟页面访问量（PV）。
(*)| select COUNT(*) as PV
使用场景：[统计图](single-value-chart.md)主要用于直观展示单个关键指标的当前数值及其变化趋势，适用于需要了解业务状态或监控异常情况的场景。
### 饼图（Pro版本）
饼图通过将一个圆饼按照分类的占比划分成多个区块，整个圆饼代表数据的总量，每个区块（圆弧）表示该分类占总体的比例大小，所有区块（圆弧）的加和等于 100%。比如统计每个request_method（请求方法，如GET、POST等）的次数。
(*)| SELECT request_method, arbitrary(request_length) as len, COUNT(*) as c group by request_method
使用场景：[饼图](pie-chart.md)主要用于展示数据的占比关系。它适用于展示不同部分在整体中的比例，如不同产品的市场份额、各个部门的预算比例等。
### 地图（Pro版本）
以地图作为背景，通过图形颜色、图像标记的方式展示地理数据信息。比如按国家分组统计每个国家的记录数（count）。
(*)| select ip_to_country(remote_addr) as address, count(1) as count group by address order by count desc limit 10
使用场景：[地图](maps.md)用于展示地理空间数据。适用于分析地理位置相关的数据，如人口分布、城市扩张、交通流量等。
选择更多图表，请参见[流图](flow-chart.md)、[计量图](bar-gauge.md)、[直方图](histogram.md)、[雷达图](radar-chart.md)、[交叉表](cross-table.md)、[散点图](scatter-chart.md)、[拓扑图](topology-chart.md)、[火焰图](flame-graph.md)、[Markdown](manage-a-markdown-chart.md)[图表](manage-a-markdown-chart.md)、[时间轴](display-query-results-on-a-timeline-chart.md)、[词云](display-query-results-on-a-word-cloud.md)、[桑基图](display-query-results-in-a-sankey-diagram.md)、[高德地图](gaud-map.md)、[轨迹图](display-query-results-on-a-trail-map.md)、[矩形树图](display-query-results-on-a-treemap-chart.md)、[时序状态图](timing-state-diagram.md)、[漏斗图](display-query-results-on-a-funnel-chart.md)。
## 相关文档
创建仪表盘请参见[快速创建仪表盘](dashboard-overview.md)，分享仪表盘请参见[免密分享与集成仪表盘](secret-free-sharing-and-integrated-dashboard.md)。
使用仪表盘发现异常指标，请参见[使用仪表盘快速发现异常指标](use-dashboards-to-quickly-discover-abnormal-metrics.md)，对异常进行分析，请参见[使用仪表盘下钻分析定位异常根因](user-guide/use-instrument-cluster-drill-in-analysis-to-locate-the-root-cause.md)。
日志服务支持通过统计图表的方式对查询分析结果进行可视化展示，具体请参见[统计图表概述](chart-overview.md)和[统计图表概述](user-guide/overview-of-charts.md)。
日志服务支持将查询和分析结果通过图表形式保存到仪表盘中，具体操作请参见[添加统计图表到仪表盘](add-a-chart-to-a-dashboard-1.md)和[添加统计图表到仪表盘](add-a-chart-to-a-dashboard.md)。
关于过滤器类型过滤器的操作示例，请参见[添加过滤器类型的过滤器](add-a-filter-of-the-filter-type.md)。关于变量类型过滤器的操作示例，请参见[添加变量类型的过滤器](add-a-filter-of-the-replace-variable-type.md)。
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
