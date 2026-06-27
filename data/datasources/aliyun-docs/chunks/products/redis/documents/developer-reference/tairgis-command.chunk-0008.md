## GIS.GET

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.GET area polygonName |
| 时间复杂度 | O(1) |
| 命令描述 | 获取目标 area 中指定多边形的 WKT 信息。 |
| 选项 | area ：一个几何概念。 PolygonName ：多边形的名称。 |
| 返回值 | 执行成功：WKT 信息。 area 或 polygonName 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.GET hangzhou campus 返回示例： 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' |
