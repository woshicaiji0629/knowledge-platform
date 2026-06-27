## GIS.ADD

| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.ADD area polygonName polygonWkt [polygonName polygonWkt ...] |
| 时间复杂度 | O(log n) |
| 命令描述 | 在 area 中添加指定名称的多边形（可添加多个），使用 WKT（Well-known text）描述。 说明 WKT 是一种文本标记语言，用于描述矢量几何对象、空间参照系统及空间参照系统之间的转换。 |
| 选项 | area ：一个几何概念。 PolygonName ：多边形的名称。 polygonWkt ：多边形的描述信息，表示现实世界的经、纬度，使用 WKT（Well-known text）描述，支持如下类型。 POINT：描述一个点的 WKT 信息，例如 'POINT (120.086631 30.138141)' ，表示该 POINT 位于经度 120.086631，纬度 30.138141。 LINESTRING：描述一条线的 WKT 信息，由两个 POINT 组成，例如 'LINESTRING (30 10, 40 40)' 。 POLYGON：描述一个多边形的 WKT 信息，由多个 POINT 组成，例如 'POLYGON ((31 20, 29 20, 29 21, 31 31))' 。 说明 经度的取值范围为（-180,180）， 纬度的取值范围为（-90,90）。 不支持如下集合类型：MULTIPOINT、MULTILINESTRING、MULTIPOLYGON、GEOMETRY 和 COLLECTION。 |
| 返回值 | 执行成功：返回插入和更新成功的多边形数量。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： GIS.ADD hangzhou campus 'POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))' 返回示例： (integer) 1 |
