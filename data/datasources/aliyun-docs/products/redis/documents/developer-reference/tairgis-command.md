# GIS扩展命令参考与语法详解-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/tairgis-command

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# GIS

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

TairGis是一种使用R-Tree做索引，支持地理信息系统GIS（Geographic Information System）相关接口的数据结构。Redis的原生GEO命令是使用GeoHash和Redis Sorted Set结构完成的，主要用于点的查询，TairGIS在此基础上还支持线、面的查询，功能更加强大。

## 主要特性

- 

使用R-Tree作为索引存储。

- 

支持线、面的相关查询（含相交查询）。

- 

通过[GIS.SEARCH](products/redis/documents/developer-reference/tairgis-command.md)可实现原生RedisGEORADIUS命令的功能。

该Module已开源，更多信息请参见[TairGIS](https://github.com/tair-opensource/TairGis)。

## 最佳实践

- 

[基于](products/redis/documents/use-cases/user-trajectory-monitoring-using-tairgis.md)[TairGIS](products/redis/documents/use-cases/user-trajectory-monitoring-using-tairgis.md)[实现电子围栏](products/redis/documents/use-cases/user-trajectory-monitoring-using-tairgis.md)

- 

[基于](products/redis/documents/use-cases/implementation-of-the-same-city-purchase-business-based-on-tairgis.md)[TairGIS](products/redis/documents/use-cases/implementation-of-the-same-city-purchase-business-based-on-tairgis.md)[实现同城购业务](products/redis/documents/use-cases/implementation-of-the-same-city-purchase-business-based-on-tairgis.md)

## 前提条件

实例为Tair[内存型](products/redis/documents/product-overview/dram-based-instances.md)。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群架构或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

操作对象为Tair实例中的TairGIS数据。

## 命令列表

表 1.TairGIS命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [GIS.ADD](products/redis/documents/developer-reference/tairgis-command.md) | GIS.ADD area polygonName polygonWkt [polygonName polygonWkt ...] | 在 area 中添加指定名称的多边形（可添加多个），使用 WKT（Well-known text）描述。 说明 WKT 是一种文本标记语言，用于描述矢量几何对象、空间参照系统及空间参照系统之间的转换。 |
| [GIS.GET](products/redis/documents/developer-reference/tairgis-command.md) | GIS.GET area polygonName | 获取目标 area 中指定多边形的 WKT 信息。 |
| [GIS.GETALL](products/redis/documents/developer-reference/tairgis-command.md) | GIS.GETALL area [WITHOUTWKT] | 获取目标 area 中所有多边形的名称和 WKT 信息。如果设置了 WITHOUTWKT 选项，仅返回多边形的名称。 |
| [GIS.CONTAINS](products/redis/documents/developer-reference/tairgis-command.md) | GIS.CONTAINS area polygonWkt [WITHOUTWKT] | 判断指定的点、线或面是否包含在目标 area 的多边形中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| [GIS.WITHIN](products/redis/documents/developer-reference/tairgis-command.md) | GIS.WITHIN area polygonWkt [WITHOUTWKT] | 判断目标 area 是否包含在指定的点、线或面中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| [GIS.INTERSECTS](products/redis/documents/developer-reference/tairgis-command.md) | GIS.INTERSECTS area polygonWkt | 判断指定的点、线或面与目标 area 的多边形是否相交，若相交，则返回目标 area 中与其相交的多边形数量与多边形信息。 |
| [GIS.SEARCH](products/redis/documents/developer-reference/tairgis-command.md) | GIS.SEARCH area [RADIUS longitude latitude distance M|KM|FT|MI] [MEMBER field distance M|KM|FT|MI] [GEOM geom] [COUNT count] [ASC|DESC] [WITHDIST] [WITHOUTWKT] | 在指定经、纬度及半径距离范围内，查找目标 area 中的点。 |
| [GIS.DEL](products/redis/documents/developer-reference/tairgis-command.md) | GIS.DEL area polygonName | 删除目标 area 中指定的多边形。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 原生 Redis 命令，可以删除一条或多条 TairGIS 数据。 |


说明

本文的命令语法定义如下：

- 

大写关键字：命令关键字。

- 

斜体：变量。

- 

[options]：可选参数，不在括号中的参数为必选。

- 

A|B：该组参数互斥，请进行二选一或多选一。

- 

...：前面的内容可重复。

## GIS.ADD

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.ADD area polygonName polygonWkt [polygonName polygonWkt ...] |
| 时间复杂度 | O(log n) |
| 命令描述 | 在 area 中添加指定名称的多边形（可添加多个），使用 WKT（Well-known text）描述。 说明 WKT 是一种文本标记语言，用于描述矢量几何对象、空间参照系统及空间参照系统之间的转换。 |
| 选项 | area ：一个几何概念。 PolygonName ：多边形的名称。 polygonWkt ：多边形的描述信息，表示现实世界的经、纬度，使用 WKT（Well-known text）描述，支持如下类型。 POINT：描述一个点的 WKT 信息，例如 'POINT (120.086631 30.138141)' ，表示该 POINT 位于经度 120.086631，纬度 30.138141。 LINESTRING：描述一条线的 WKT 信息，由两个 POINT 组成，例如 'LINESTRING (30 10, 40 40)' 。 POLYGON：描述一个多边形的 WKT 信息，由多个 POINT 组成，例如 'POLYGON ((31 20, 29 20, 29 21, 31 31))' 。 说明 经度的取值范围为（-180,180）， 纬度的取值范围为（-90,90）。 不支持如下集合类型：MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRY 和 COLLECTION。 |
| 返回值 | 执行成功：返回插入和更新成功的多边形数量。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 返回示例： (integer) 1 |


## GIS.GET

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.GET area polygonName |
| 时间复杂度 | O(1) |
| 命令描述 | 获取目标 area 中指定多边形的 WKT 信息。 |
| 选项 | area ：一个几何概念。 PolygonName ：多边形的名称。 |
| 返回值 | 执行成功：WKT 信息。 area 或 polygonName 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.GET hangzhou campus 返回示例： 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' |


## GIS.GETALL

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.GETALL area [WITHOUTWKT] |
| 时间复杂度 | O(n) |
| 命令描述 | 获取目标 area 中所有多边形的名称和 WKT 信息。如果设置了 WITHOUTWKT 选项，仅返回多边形的名称。 |
| 选项 | area ：一个几何概念。 WITHOUTWKT ：用于控制是否返回多边形的 WKT 信息，如果加上该参数，则不返回多边形的 WKT 信息。 |
| 返回值 | 执行成功：返回多边形名称和 WKT 信息，如果设置了 WITHOUTWKT 选项，仅返回多边形的名称。 area 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.GETALL hangzhou 返回示例： 1) "campus" 2) "POLYGON((30 10,40 40,20 40,10 20,30 10))" |


## GIS.CONTAINS

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.CONTAINS area polygonWkt [WITHOUTWKT] |
| 时间复杂度 | 最理想情况： 最差情况：O(log n) |
| 命令描述 | 判断指定的点、线或面是否包含在目标 area 的多边形中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| 选项 | area ：一个几何概念。 polygonWkt ：指定与目标 area 进行比较的多边形描述信息，使用 WKT（Well-known text）描述，支持如下类型。 POINT：描述一个点的 WKT 信息。 LINESTRING：描述一条线的 WKT 信息。 POLYGON：描述一个多边形的 WKT 信息。 WITHOUTWKT ：用于控制是否返回多边形的 WKT 信息，如果加上该参数，则不返回多边形的 WKT 信息。 |
| 返回值 | 执行成功：命中的多边形数量与多边形信息。 area 不存在：empty list or set。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.CONTAINS hangzhou 'POINT (30 11)' 返回示例： 1) "1" 2) 1) "campus" 2) "POLYGON((30 10,40 40,20 40,10 20,30 10))" |


## GIS.WITHIN

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.WITHIN area polygonWkt [WITHOUTWKT] |
| 时间复杂度 | 最理想情况： 最差情况：O(log n) |
| 命令描述 | 判断目标 area 是否包含在指定的点、线或面中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| 选项 | area ：一个几何概念。 polygonWkt ：指定与目标 area 进行比较的多边形描述信息，使用 WKT（Well-known text）描述，支持如下类型。 POINT：描述一个点的 WKT 信息。 LINESTRING：描述一条线的 WKT 信息。 POLYGON：描述一个多边形的 WKT 信息。 说明 不支持 MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRY 和 COLLECTION。 WITHOUTWKT ：用于控制是否返回多边形的 WKT 信息，如果加上该参数，则不返回多边形的 WKT 信息。 |
| 返回值 | 执行成功：命中的多边形数量与多边形信息。 area 不存在：empty list or set。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.WITHIN hangzhou 'POLYGON ((30 5, 50 50, 20 50, 5 20, 30 5))' 返回示例： 1) "1" 2) 1) "campus" 2) "POLYGON((30 10,40 40,20 40,10 20,30 10))" |


## GIS.INTERSECTS

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.INTERSECTS area polygonWkt |
| 时间复杂度 | 最理想情况： 最差情况：O(log n) |
| 命令描述 | 判断指定的点、线或面与目标 area 的多边形是否相交，若相交，则返回目标 area 中与其相交的多边形数量与多边形信息。 |
| 选项 | area ：一个几何概念。 polygonWkt ：指定与目标 area 进行比较的多边形描述信息，使用 WKT（Well-known text）描述，支持如下类型。 POINT：描述一个点的 WKT 信息。 LINESTRING：描述一条线的 WKT 信息。 POLYGON：描述一个多边形的 WKT 信息。 WITHOUTWKT ：用于控制是否返回多边形的 WKT 信息，如果加上该参数，则不返回多边形的 WKT 信息。 |
| 返回值 | 执行成功：命中的多边形数量与多边形信息。 area 不存在：empty list or set。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.INTERSECTS hangzhou 'LINESTRING (30 10, 40 40)' 返回示例： 1) "1" 2) 1) "campus" 2) "POLYGON((30 10,40 40,20 40,10 20,30 10))" |


## GIS.SEARCH

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.SEARCH area [RADIUS longitude latitude distance M|KM|FT|MI] [MEMBER field distance M|KM|FT|MI] [GEOM geom] [COUNT count] [ASC|DESC] [WITHDIST] [WITHOUTWKT] |
| 时间复杂度 | 最理想情况： 最差情况：O(log n) |
| 命令描述 | 在指定经、纬度及半径距离范围内，查找目标 area 中的点。 |
| 选项 | area ：一个几何概念。 RADIUS ：传入经度（longitude）、纬度（latitude）、半径距离（distance）和半径单位（M 表示米、KM 表示千米、FT 表示英尺、MI 表示英里）进行搜索，例如 RADIUS 15 37 200 KM 。 MEMBER ：选择当前 area 中已存在的 POINT 作为搜索原点，并指定半径进行搜索，取值顺序为多边形名称（field）、半径（distance）、半径单位（M 表示米、KM 表示千米、FT 表示英尺、MI 表示英里），例如 MEMBER Agrigento 100 KM 。 GEOM ：按照 WKT 的格式设置搜索范围，可以是任意多边形，例如 GEOM 'POLYGON((10 30,20 30,20 40,10 40))' 。 COUNT ：用于限定返回的个数，例如 COUNT 3 。 ASC | DESC ：用于控制返回信息按照距离排序， ASC 表示根据中心位置，由近到远排序； DESC 表示由远到近排序。 WITHDIST ：用于控制是否返回目标点与搜索原点的距离。 WITHOUTWKT ：用于控制是否返回目标点的 WKT 信息，如果加上该参数，则不返回 WKT 信息。 说明 只能同时使用 RADIUS 、 MEMBER 和 GEOM 中的一种方式。 |
| 返回值 | 执行成功：命中的目标点数量与 WKT 信息。 area 不存在：empty list or set。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD Sicily "Palermo" "POINT (13.361389 38.115556)" "Catania" "POINT(15.087269 37.502669)" 命令。 命令示例： GIS.SEARCH Sicily RADIUS 15 37 200 km WITHDIST ASC 返回示例： 1) (integer) 2 2) 1) "Catania" 2) "POINT(15.087269 37.502669)" 3) "56.4413" 4) "Palermo" 5) "POINT(13.361389 38.115556)" 6) "190.4424" |


## GIS.DEL

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.DEL area polygonName |
| 时间复杂度 | O(log n) |
| 命令描述 | 删除目标 area 中指定的多边形。 |
| 选项 | area ：一个几何概念。 PolygonName ：多边形的名称。 |
| 返回值 | 执行成功：OK。 area 或 polygonName 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.DEL hangzhou campus 返回示例： OK |


[上一篇：exZset](products/redis/documents/developer-reference/tairzset-command.md)[下一篇：Bloom](products/redis/documents/developer-reference/tairbloom-command.md)

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
