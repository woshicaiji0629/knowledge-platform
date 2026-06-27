# 兼容Redis内存型云数据库-资源包-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/resource-plan-overview

# 资源包
云数据库Tair（兼容 Redis）推出资源包，可抵扣部分按量付费实例的实例规格费用，助力企业降本增效。
## 资源包概述
通常，包年包月的计费方式是性价比最高的，若您计划长期持有，请直接选择包年包月的计费方式。
若您的业务可能存在变化与调整，您可以选择“按量付费+资源包”的计费方式，同时享受按量付费的灵活与近似包年包月的低价。
| 介绍项 | 说明 |
| --- | --- |
| 抵扣对象 | 资源包可抵扣当前账户中同时满足下述所有条件实例的实例规格费用，且优先从资源包抵扣，条件如下： 实例为 Redis 开源版 （即社区版）或 Tair（企业版） 实例。 部署模式为 经典 。 计费方式为按量付费。 说明 若资源包剩余容量不足，超出的费用仍以按量付费的形式从账户余额中扣除。 |
| 抵扣顺序 | 支持购买多个资源包，按资源包的到期时间顺序优先抵扣，优先抵扣先到期的资源包。 |
| 是否支持续费或升降配 | 不支持，若资源包容量不足、即将到期或已过期，您可以再次购买资源包叠加使用。 |
| 有效期 | 每个资源包的有效期为 6 个月、1 年或 2 年（仅 1,000 度 以上的资源包允许选择 2 年有效期），到期后资源包的剩余容量自动失效。 |
## 资源包价格与容量
云数据库Tair（兼容 Redis）采用单位CU（Capacity Unit）*H，简称“度”，来定义一个资源包能够提供的资源容量。资源包单价为21元/度，云数据库Tair（兼容 Redis）提供了3种不同容量的资源包规格，资源包容量越大，折扣越多。相同规格阶梯的资源包，有效期越短，折扣越多。
| 资源包规格阶梯（度） | 有效期 | 单价（元/度） | Redis 社区版 1 GB 主从版实例单月成本示例（元） | 折扣（相比按量付费） |
| --- | --- | --- | --- | --- |
| 15~99 | 6 个月 | 18.90 | 136 | 9 折 |
| 1 年 | 19.95 | 144 | 95 折 |  |
| 100~999 | 6 个月 | 17.85 | 129 | 85 折 |
| 1 年 | 18.90 | 136 | 9 折 |  |
| 1000~10000 | 6 个月 | 13.65 | 98 | 65 折 |
| 1 年 | 14.70 | 106 | 7 折 |  |
| 2 年 | 16.80 | 121 | 8 折 |  |
说明
本示例以华东1（杭州）地域、Redis社区版1 GB标准版实例为例：
按量付费：单价为0.21元/小时，每月成本为0.21元/小时 * 24（小时） * 30（天）=151.2元。
按量付费 + 资源包：华东1（杭州）的地域抵扣系数为1、Redis社区版1 GB标准版实例的实例规格消耗系数为0.01，每月成本为1（地域抵扣系数）* 0.01（实例规格消耗系数）* 24（小时） * 30（天）* 资源包单价。
## 资源包抵扣规则
资源包抵扣对象：当前账户下所有按量付费、经典版Redis开源版或经典版Tair（企业版）实例的实例规格费用。
资源包消耗公式：地域抵扣系数 * 实例规格消耗系数（度/小时）* 使用时长（小时）
例如中国香港地域的Redis开源版1 GB主从版实例：中国香港地域的抵扣系数为1.15、实例规格消耗系数为0.01度/小时，则该实例24小时所消耗的度数：0.01（度/小时）* 1.15 * 24（小时）=0.276度。
各地域的抵扣系数与各实例规格消耗系数如下。
## 地域抵扣系数
当前资源包为全球地域通用，在抵扣不同地域的实例规格费用时，将以不同的系数进行抵扣。
| 实例所在地域 | 地域抵扣系数 |
| --- | --- |
| 中国内地（不含张家口、乌兰察布和中国香港） | 1.00 |
| 华北 3（张家口）、华北 6（乌兰察布） | 0.75 |
| 中国香港 | 1.15 |
| 日本（东京） | 1.69 |
| 新加坡、印度尼西亚（雅加达） | 1.46 |
| 马来西亚（吉隆坡） | 1.48 |
| 菲律宾（马尼拉） | 1.32 |
| 德国（法兰克福） | 1.21 |
| 英国（伦敦） | 1.18 |
| 美国（硅谷） | 1.01 |
| 美国（弗吉尼亚） | 1.24 |
| 阿联酋（迪拜） | 1.61 |
## 实例规格消耗系数
下表列出不同实例规格每小时所消耗的资源量。
Redis社区版-标准版-双副本
| 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- |
| 256 MB 主从版 | redis.master.micro.default | 0.0030 |
| 1 GB 主从版 | redis.master.small.default | 0.0100 |
| 2 GB 主从版 | redis.master.mid.default | 0.0180 |
| 4 GB 主从版 | redis.master.stand.default | 0.0340 |
| 8 GB 主从版 | redis.master.large.default | 0.0660 |
| 16 GB 主从版 | redis.master.2xlarge.default | 0.1290 |
| 32 GB 主从版 | redis.master.4xlarge.default | 0.2560 |
| 64 GB 主从版 | redis.master.8xlarge.default | 0.5060 |
Redis社区版-标准版-单副本
| 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- |
| 1 GB 单副本 | redis.basic.small.default | 0.0060 |
| 2 GB 单副本 | redis.basic.mid.default | 0.0100 |
| 4 GB 单副本 | redis.basic.stand.default | 0.0180 |
| 8 GB 单副本 | redis.basic.large.default | 0.0350 |
| 16 GB 单副本 | redis.basic.2xlarge.default | 0.0690 |
| 32 GB 单副本 | redis.basic.4xlarge.default | 0.1360 |
Redis社区版-集群版-双副本
| 分片数 | 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- | --- |
| 2 分片 | 2 GB 集群版（2 分片） | redis.logic.sharding.1g.2db.0rodb.4proxy.default | 0.0280 |
| 4 GB 集群版（2 分片） | redis.logic.sharding.2g.2db.0rodb.4proxy.default | 0.0420 |  |
| 8 GB 集群版（2 分片） | redis.logic.sharding.4g.2db.0rodb.4proxy.default | 0.0800 |  |
| 12 GB 集群（2 分片） | redis.logic.sharding.6g.2db.0rodb.4proxy.default | 0.1260 |  |
| 16 GB 集群版（2 分片） | redis.logic.sharding.8g.2db.0rodb.4proxy.default | 0.1490 |  |
| 20 GB 集群（2 分片） | redis.logic.sharding.10g.2db.0rodb.4proxy.default | 0.1890 |  |
| 32 GB 集群版（2 分片） | redis.logic.sharding.16g.2db.0rodb.4proxy.default | 0.2980 |  |
| 4 分片 | 4 GB 集群版（4 分片） | redis.logic.sharding.1g.4db.0rodb.4proxy.default | 0.0420 |
| 8 GB 集群版（4 分片） | redis.logic.sharding.2g.4db.0rodb.4proxy.default | 0.0800 |  |
| 16 GB 集群版（4 分片） | redis.logic.sharding.4g.4db.0rodb.4proxy.default | 0.1490 |  |
| 24 GB 集群版（4 分片） | redis.logic.sharding.6g.4db.0rodb.4proxy.default | 0.2290 |  |
| 32 GB 集群版（4 分片） | redis.logic.sharding.8g.4db.0rodb.4proxy.default | 0.2980 |  |
| 40 GB 集群版（4 分片） | redis.logic.sharding.10g.4db.0rodb.4proxy.default | 0.3770 |  |
| 64 GB 集群版（4 分片） | redis.logic.sharding.16g.4db.0rodb.4proxy.default | 0.5950 |  |
| 128 GB 集群版（4 分片） | redis.logic.sharding.32g.4db.0rodb.8proxy.default | 1.1900 |  |
| 8 分片 | 8 GB 集群版（8 分片） | redis.logic.sharding.1g.8db.0rodb.8proxy.default | 0.0800 |
| 16 GB 集群版（8 分片） | redis.logic.sharding.2g.8db.0rodb.8proxy.default | 0.1490 |  |
| 32 GB 集群版（8 分片） | redis.logic.sharding.4g.8db.0rodb.8proxy.default | 0.2980 |  |
| 48 GB 集群版（8 分片） | redis.logic.sharding.6g.8db.0rodb.8proxy.default | 0.4570 |  |
| 64 GB 集群版（8 分片） | redis.logic.sharding.8g.8db.0rodb.8proxy.default | 0.5950 |  |
| 80 GB 集群版（8 分片） | redis.logic.sharding.10g.8db.0rodb.8proxy.default | 0.7440 |  |
| 128 GB 集群版（8 分片） | redis.logic.sharding.16g.8db.0rodb.8proxy.default | 1.1900 |  |
| 256 GB 集群版（8 分片） | redis.logic.sharding.32g.8db.0rodb.8proxy.default | 2.3810 |  |
| 16 分片 | 16 GB 集群版（16 分片） | redis.logic.sharding.1g.16db.0rodb.16proxy.default | 0.1490 |
| 32 GB 集群版（16 分片） | redis.logic.sharding.2g.16db.0rodb.16proxy.default | 0.2980 |  |
| 64 GB 集群版（16 分片） | redis.logic.sharding.4g.16db.0rodb.16proxy.default | 0.5950 |  |
| 96 GB 集群版（16 分片） | redis.logic.sharding.6g.16db.0rodb.16proxy.default | 0.8930 |  |
| 128 GB 集群版（16 分片） | redis.logic.sharding.8g.16db.0rodb.16proxy.default | 1.1900 |  |
| 160 GB 集群版（16 分片） | redis.logic.sharding.10g.16db.0rodb.16proxy.default | 1.4880 |  |
| 256 GB 集群版（16 分片） | redis.logic.sharding.16g.16db.0rodb.16proxy.default | 2.3810 |  |
| 512 GB 集群版（16 分片） | redis.logic.sharding.32g.16db.0rodb.16proxy.default | 4.7620 |  |
| 32 分片 | 64 GB 集群版（32 分片） | redis.logic.sharding.2g.32db.0rodb.32proxy.default | 0.5950 |
| 128 GB 集群版（32 分片） | redis.logic.sharding.4g.32db.0rodb.32proxy.default | 1.1900 |  |
| 192 GB 集群版（32 分片） | redis.logic.sharding.6g.32db.0rodb.32proxy.default | 1.7860 |  |
| 256 GB 集群版（32 分片） | redis.logic.sharding.8g.32db.0rodb.32proxy.default | 2.3810 |  |
| 320 GB 集群版（32 分片） | redis.logic.sharding.10g.32db.0rodb.32proxy.default | 2.9760 |  |
| 512 GB 集群版（32 分片） | redis.logic.sharding.16g.32db.0rodb.32proxy.default | 4.7620 |  |
| 1024 GB 集群版（32 分片） | redis.logic.sharding.32g.32db.0rodb.32proxy.default | 9.5238 |  |
| 48 分片 | 382 GB 集群版（48 分片） | redis.logic.sharding.8g.48db.0rodb.48proxy.default | 1.9737 |
| 480 GB 集群版（48 分片） | redis.logic.sharding.10g.48db.0rodb.48proxy.default | 4.5260 |  |
| 768 GB 集群版（48 分片） | redis.logic.sharding.16g.48db.0rodb.48proxy.default | 7.1430 |  |
| 1536 GB 集群版（48 分片） | redis.logic.sharding.32g.48db.0rodb.48proxy.default | 14.2860 |  |
| 64 分片 | 128 GB 集群版（64 分片） | redis.logic.sharding.2g.64db.0rodb.64proxy.default | 1.1900 |
| 256 GB 集群版（64 分片） | redis.logic.sharding.4g.64db.0rodb.64proxy.default | 2.3810 |  |
| 512 GB 集群版（64 分片） | redis.logic.sharding.8g.64db.0rodb.64proxy.default | 4.7620 |  |
| 640 GB 集群版（64 分片） | redis.logic.sharding.10g.64db.0rodb.64proxy.default | 6.0340 |  |
| 1024 GB 集群版（64 分片） | redis.logic.sharding.16g.64db.0rodb.64proxy.default | 9.5240 |  |
| 2048 GB 集群版（64 分片） | redis.logic.sharding.32g.64db.0rodb.64proxy.default | 19.0480 |  |
| 96 分片 | 1536 GB 集群版（96 分片） | redis.logic.sharding.16g.96db.0rodb.96proxy.default | 14.2860 |
| 3072 GB 集群版（96 分片） | redis.logic.sharding.32g.96db.0rodb.96proxy.default | 28.5710 |  |
| 128 分片 | 512 GB 集群版（128 分片） | redis.logic.sharding.4g.128db.0rodb.128proxy.default | 4.7620 |
| 2048 GB 集群版（128 分片） | redis.logic.sharding.16g.128db.0rodb.128proxy.default | 19.0480 |  |
| 4096 GB 集群版（128 分片） | redis.logic.sharding.32g.128db.0rodb.128proxy.default | 38.0950 |  |
| 256 分片 | 1024 GB 集群版（256 分片） | redis.logic.sharding.4g.256db.0rodb.256proxy.default | 9.5240 |
| 2048 GB 集群版（256 分片） | redis.logic.sharding.8g.256db.0rodb.256proxy.default | 19.0480 |  |
| 4096 GB 集群版（256 分片） | redis.logic.sharding.16g.256db.0rodb.256proxy.default | 38.0950 |  |
Redis社区版-集群版-单副本
| 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- |
| 16 GB 单副本集群版 | redis.sharding.basic.small.default | 0.0800 |
| 32 GB 单副本集群版 | redis.sharding.basic.mid.default | 0.1590 |
| 64 GB 单副本集群版 | redis.sharding.basic.large.default | 0.3180 |
| 128 GB 单副本集群版 | redis.sharding.basic.2xlarge.default | 0.6350 |
| 256 GB 单副本集群版 | redis.sharding.basic.4xlarge.default | 1.2700 |
| 512 GB 单副本集群版 | redis.sharding.basic.8xlarge.default | 2.5400 |
| 1 TB 单节点集群版 | redis.sharding.basic.16xlarge.default | 5.0800 |
| 2 TB 单节点集群版 | redis.sharding.basic.32xlarge.default | 10.1600 |
Redis社区版-读写分离版
| 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- |
| 1 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.small.1db.1rodb.4proxy.default | 0.0220 |
| 1 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.small.1db.3rodb.4proxy.default | 0.0340 |
| 1 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.small.1db.5rodb.6proxy.default | 0.0460 |
| 2 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.mid.1db.1rodb.4proxy.default | 0.0390 |
| 2 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.mid.1db.3rodb.4proxy.default | 0.0590 |
| 2 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.mid.1db.5rodb.6proxy.default | 0.0800 |
| 4 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.stand.1db.1rodb.4proxy.default | 0.0690 |
| 4 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.stand.1db.3rodb.4proxy.default | 0.1090 |
| 4 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.stand.1db.5rodb.6proxy.default | 0.1490 |
| 8 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.large.1db.1rodb.4proxy.default | 0.1270 |
| 8 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.large.1db.3rodb.4proxy.default | 0.2070 |
| 8 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.large.1db.5rodb.6proxy.default | 0.2870 |
| 16 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.2xlarge.1db.1rodb.4proxy.default | 0.2460 |
| 16 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.2xlarge.1db.3rodb.4proxy.default | 0.4030 |
| 16 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.2xlarge.1db.5rodb.6proxy.default | 0.5630 |
| 32 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.4xlarge.1db.1rodb.4proxy.default | 0.4820 |
| 32 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.4xlarge.1db.3rodb.4proxy.default | 0.7980 |
| 32 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.4xlarge.1db.5rodb.6proxy.default | 1.1140 |
| 64 GB 读写分离版（2 副本，含 1 只读副本） | redis.logic.splitrw.8xlarge.1db.1rodb.4proxy.default | 0.9650 |
| 64 GB 读写分离版（4 副本，含 3 只读副本） | redis.logic.splitrw.8xlarge.1db.3rodb.4proxy.default | 1.5950 |
| 64 GB 读写分离版（6 副本，含 5 只读副本） | redis.logic.splitrw.8xlarge.1db.5rodb.6proxy.default | 2.2290 |
Tair内存型-标准版
| 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- |
| 1 GB 主从版 | redis.amber.master.small.multithread | 0.0140 |
| 2 GB 主从版 | redis.amber.master.mid.multithread | 0.0252 |
| 4 GB 主从版 | redis.amber.master.stand.multithread | 0.0476 |
| 8 GB 主从版 | redis.amber.master.large.multithread | 0.0917 |
| 16 GB 主从版 | redis.amber.master.2xlarge.multithread | 0.1806 |
| 32 GB 主从版 | redis.amber.master.4xlarge.multithread | 0.3584 |
| 64 GB 主从版 | redis.amber.master.8xlarge.multithread | 0.7084 |
Tair内存型-集群版
| 分片数 | 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- | --- |
| 2 分片 | 2 GB 集群版 | redis.amber.logic.sharding.1g.2db.0rodb.6proxy.multithread | 0.0392 |
| 4 GB 集群版 | redis.amber.logic.sharding.2g.2db.0rodb.6proxy.multithread | 0.0588 |  |
| 8 GB 集群版 | redis.amber.logic.sharding.4g.2db.0rodb.6proxy.multithread | 0.1113 |  |
| 16 GB 集群版 | redis.amber.logic.sharding.8g.2db.0rodb.6proxy.multithread | 0.2086 |  |
| 32 GB 集群版 | redis.amber.logic.sharding.16g.2db.0rodb.6proxy.multithread | 0.4165 |  |
| 64 GB 集群版 | redis.amber.logic.sharding.32g.2db.0rodb.6proxy.multithread | 0.8330 |  |
| 4 分片 | 8 GB 集群版 | redis.amber.logic.sharding.2g.4db.0rodb.12proxy.multithread | 0.1113 |
| 16 GB 集群版 | redis.amber.logic.sharding.4g.4db.0rodb.12proxy.multithread | 0.2086 |  |
| 32 GB 集群版 | redis.amber.logic.sharding.8g.4db.0rodb.12proxy.multithread | 0.4165 |  |
| 64 GB 集群版 | redis.amber.logic.sharding.16g.4db.0rodb.12proxy.multithread | 0.8330 |  |
| 128 GB 集群版 | redis.amber.logic.sharding.32g.4db.0rodb.12proxy.multithread | 1.6667 |  |
| 8 分片 | 16 GB 集群版 | redis.amber.logic.sharding.2g.8db.0rodb.24proxy.multithread | 0.2086 |
| 32 GB 集群版 | redis.amber.logic.sharding.4g.8db.0rodb.24proxy.multithread | 0.4165 |  |
| 64 GB 集群版 | redis.amber.logic.sharding.8g.8db.0rodb.24proxy.multithread | 0.8330 |  |
| 128 GB 集群版 | redis.amber.logic.sharding.16g.8db.0rodb.24proxy.multithread | 1.6667 |  |
| 256 GB 集群版 | redis.amber.logic.sharding.32g.8db.0rodb.24proxy.multithread | 3.3334 |  |
| 16 分片 | 32 GB 集群版 | redis.amber.logic.sharding.2g.16db.0rodb.48proxy.multithread | 0.4165 |
| 96 GB 集群版 | redis.amber.logic.sharding.6g.16db.0rodb.48proxy.multithread | 1.2502 |  |
| 128 GB 集群版 | redis.amber.logic.sharding.8g.16db.0rodb.48proxy.multithread | 1.6667 |  |
| 256 GB 集群版 | redis.amber.logic.sharding.16g.16db.0rodb.48proxy.multithread | 3.3334 |  |
| 512 GB 集群版 | redis.amber.logic.sharding.32g.16db.0rodb.48proxy.multithread | 6.6668 |  |
| 32 分片 | 32 GB 集群版 | redis.amber.logic.sharding.1g.32db.0rodb.96proxy.multithread | 0.6293 |
| 64 GB 集群版 | redis.amber.logic.sharding.2g.32db.0rodb.96proxy.multithread | 0.8330 |  |
| 256 GB 集群版 | redis.amber.logic.sharding.8g.32db.0rodb.96proxy.multithread | 3.3334 |  |
| 512 GB 集群版 | redis.amber.logic.sharding.16g.32db.0rodb.96proxy.multithread | 6.6668 |  |
| 1024 GB 集群版 | redis.amber.logic.sharding.32g.32db.0rodb.96proxy.multithread | 13.3336 |  |
| 48 分片 | 768 GB 集群版 | redis.amber.logic.sharding.16g.48db.0rodb.144proxy.multithread | 10.0002 |
| 1536 GB 集群版 | redis.amber.logic.sharding.32g.48db.0rodb.144proxy.multithread | 19.9997 |  |
| 64 分片 | 64 GB 集群版 | redis.amber.logic.sharding.1g.64db.0rodb.192proxy.multithread | 1.2586 |
| 128 GB 集群版 | redis.amber.logic.sharding.2g.64db.0rodb.192proxy.multithread | 1.6667 |  |
| 256 GB 集群版 | redis.amber.logic.sharding.4g.64db.0rodb.192proxy.multithread | 3.3334 |  |
| 512 GB 集群版 | redis.amber.logic.sharding.8g.64db.0rodb.192proxy.multithread | 6.6668 |  |
| 1024 GB 集群版 | redis.amber.logic.sharding.16g.64db.0rodb.192proxy.multithread | 13.3336 |  |
| 2048 GB 集群版 | redis.amber.logic.sharding.32g.64db.0rodb.192proxy.multithread | 26.6665 |  |
| 128 分片 | 2048 GB 集群版 | redis.amber.logic.sharding.16g.128db.0rodb.384proxy.multithread | 26.6665 |
| 4096 GB 集群版 | redis.amber.logic.sharding.32g.128db.0rodb.384proxy.multithread | 53.3330 |  |
| 256 分片 | 4096 GB 集群版 | redis.amber.logic.sharding.16g.256db.0rodb.768proxy.multithread | 53.3330 |
Tair内存型-读写分离版
| 规格 | 规格码（InstanceClass） | 每小时消耗的度数（度/小时） |
| --- | --- | --- |
| 1 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.small.1db.1rodb.6proxy.multithread | 0.0308 |
| 2 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.mid.1db.1rodb.6proxy.multithread | 0.0546 |
| 4 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.stand.1db.1rodb.6proxy.multithread | 0.0959 |
| 8 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.large.1db.1rodb.6proxy.multithread | 0.1778 |
| 16 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.2xlarge.1db.1rodb.6proxy.multithread | 0.3444 |
| 32 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.4xlarge.1db.1rodb.6proxy.multithread | 0.6755 |
| 64 GB 读写分离版（2 副本，含 1 只读副本） | redis.amber.logic.splitrw.8xlarge.1db.1rodb.6proxy.multithread | 1.3510 |
| 1 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.small.1db.3rodb.12proxy.multithread | 0.0476 |
| 2 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.mid.1db.3rodb.12proxy.multithread | 0.0819 |
| 4 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.stand.1db.3rodb.12proxy.multithread | 0.1519 |
| 8 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.large.1db.3rodb.12proxy.multithread | 0.2891 |
| 16 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.2xlarge.1db.3rodb.12proxy.multithread | 0.5642 |
| 32 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.4xlarge.1db.3rodb.12proxy.multithread | 1.1165 |
| 64 GB 读写分离版（4 副本，含 3 只读副本） | redis.amber.logic.splitrw.8xlarge.1db.3rodb.12proxy.multithread | 2.2330 |
| 1 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.small.1db.5rodb.18proxy.multithread | 0.0637 |
| 2 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.mid.1db.5rodb.18proxy.multithread | 0.1127 |
| 4 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.stand.1db.5rodb.18proxy.multithread | 0.2086 |
| 8 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.large.1db.5rodb.18proxy.multithread | 0.4018 |
| 16 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.2xlarge.1db.5rodb.18proxy.multithread | 0.7882 |
| 32 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.4xlarge.1db.5rodb.18proxy.multithread | 1.5603 |
| 64 GB 读写分离版（6 副本，含 5 只读副本） | redis.amber.logic.splitrw.8xlarge.1db.5rodb.18proxy.multithread | 3.1199 |
## 如何购买、查看抵扣情况与退订
关于如何购买按量付费实例和资源包，请参见[创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md)和[购买资源包](purchase-a-resource-plan.md)。
关于如何查看资源包的抵扣情况，请参见[查看资源包抵扣情况](view-fees-offset-by-resource-plans.md)。
若需退订资源包，且满足以下所有条件，请[提交工单](https://selfservice.console.aliyun.com/ticket/category/redis/today)处理。
资源包未使用。
购买资源包不超过5天。
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
