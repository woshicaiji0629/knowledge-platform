## 可变配的实例规格
更改实例规格时，支持从以下源实例规格更改到目标实例规格：
说明
可通过调用API接口[DescribeResourcesModification](../developer-reference/api-ecs-2014-05-26-describeresourcesmodification.md)查询已有实例支持的更改情况。
表 1.入门级x86计算规格族

| 源实例规格族 | 可更改的目标实例规格族 |
| --- | --- |
| e | g7、c7、r7、g7ne、g7nex、c7nex、hfg7、hfc7、hfr7 g6、c6、r6、g6e、c6e、r6e、hfg6、hfc6、hfr6、re6 u1 e t6 、s6 |
| t6 、s6 | g7、c7、r7、hfg7、hfc7、hfr7、g7ne g6、c6、r6、hfg6、hfc6、hfr6、g6e、c6e、r6e、re6 t6 、s6 |
| t5 | g6、c6、r6、hfc6、hfg6、hfr6、g6a、c6a、r6a、re6 g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5、t6 、s6 |
| n4、mn4、xn4、e4 | g6、c6、r6、hfc6、hfg6、hfr6、g6a、c6a、r6a、re6 g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5、t6 、s6 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| t1、s1、s2、s3、m1、m2、c1、c2 | g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |
| n1、n2、e3 | g5、g5ne、r5、c5、ic5、hfc5、hfg5 t5 se1、sn1ne、sn2ne、se1ne、c4、ce4、cm4、re4、n4、mn4、xn4、e4 |

表 2.企业级计算规格族
