## GIS.DEL

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.DEL area polygonName |
| 时间复杂度 | O(log n) |
| 命令描述 | 删除目标 area 中指定的多边形。 |
| 选项 | area ：一个几何概念。 PolygonName ：多边形的名称。 |
| 返回值 | 执行成功：OK。 area 或 polygonName 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 命令。 命令示例： GIS.DEL hangzhou campus 返回示例： OK |

该文章对您有帮助吗？
反馈
