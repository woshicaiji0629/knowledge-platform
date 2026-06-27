| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [GIS.ADD](tairgis-command.md) | GIS.ADD area polygonName polygonWkt [polygonName polygonWkt ...] | 在 area 中添加指定名称的多边形（可添加多个），使用 WKT（Well-known text）描述。 说明 WKT 是一种文本标记语言，用于描述矢量几何对象、空间参照系统及空间参照系统之间的转换。 |
| [GIS.GET](tairgis-command.md) | GIS.GET area polygonName | 获取目标 area 中指定多边形的 WKT 信息。 |
| [GIS.GETALL](tairgis-command.md) | GIS.GETALL area [WITHOUTWKT] | 获取目标 area 中所有多边形的名称和 WKT 信息。如果设置了 WITHOUTWKT 选项，仅返回多边形的名称。 |
| [GIS.CONTAINS](tairgis-command.md) | GIS.CONTAINS area polygonWkt [WITHOUTWKT] | 判断指定的点、线或面是否包含在目标 area 的多边形中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| [GIS.WITHIN](tairgis-command.md) | GIS.WITHIN area polygonWkt [WITHOUTWKT] | 判断目标 area 是否包含在指定的点、线或面中，若包含，则返回目标 area 中命中的多边形数量与多边形信息。 |
| [GIS.INTERSECTS](tairgis-command.md) | GIS.INTERSECTS area polygonWkt | 判断指定的点、线或面与目标 area 的多边形是否相交，若相交，则返回目标 area 中与其相交的多边形数量与多边形信息。 |
| [GIS.SEARCH](tairgis-command.md) | GIS.SEARCH area [RADIUS longitude latitude distance M|KM|FT|MI] [MEMBER field distance M|KM|FT|MI] [GEOM geom] [COUNT count] [ASC|DESC] [WITHDIST] [WITHOUTWKT] | 在指定经、纬度及半径距离范围内，查找目标 area 中的点。 |
| [GIS.DEL](tairgis-command.md) | GIS.DEL area polygonName | 删除目标 area 中指定的多边形。 |
| [DE
