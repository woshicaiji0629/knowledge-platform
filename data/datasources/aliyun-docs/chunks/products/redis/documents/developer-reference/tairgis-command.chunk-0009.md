## GIS.GETALL

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.GETALL area [WITHOUTWKT] |
| 时间复杂度 | O(n) |
| 命令描述 | 获取目标 area 中所有多边形的名称和 WKT 信息。如果设置了 WITHOUTWKT 选项，仅返回多边形的名称。 |
| 选项 | area ：一个几何概念。 WITHOUTWKT ：用于控制是否返回多边形的 WKT 信息，如果加上该参数，则不返回多边形的 WKT 信息。 |
| 返回值 | 执行成功：返回多边形名称和 WKT 信息，如果设置了 WITHOUTWKT 选项，仅返回多边形的名称。 area 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.GETALL hangzhou 返回示例： 1) "campus" 2) "POLYGON((30 10,40 40,20 40,10 20,30 10))" |
