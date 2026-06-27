## GIS.CONTAINS

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.CONTAINS area polygonWkt [WITHOUTWKT] |
| 时间复杂度 | 最理想情况： 最差情况：O(log n) |
| 命令描述 | 判断指定的点、线或面是否包含在目标 area 的多边形中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| 选项 | area ：一个几何概念。 polygonWkt ：指定与目标 area 进行比较的多边形描述信息，使用 WKT（Well-known text）描述，支持如下类型。 POINT：描述一个点的 WKT 信息。 LINESTRING：描述一条线的 WKT 信息。 POLYGON：描述一个多边形的 WKT 信息。 WITHOUTWKT ：用于控制是否返回多边形的 WKT 信息，如果加上该参数，则不返回多边形的 WKT 信息。 |
| 返回值 | 执行成功：命中的多边形数量与多边形信息。 area 不存在：empty list or set。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.CONTAINS hangzhou 'POINT (30 11)' 返回示例： 1) "1" 2) 1) "campus" 2) "POLYGON((30 10,40 40,20 40,10 20,30 10))" |
