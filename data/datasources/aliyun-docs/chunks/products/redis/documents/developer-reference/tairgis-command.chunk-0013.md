| 类别 | 说明 |
| --- | --- |
| 语法 | GIS.SEARCH area [RADIUS longitude latitude distance M|KM|FT|MI] [MEMBER field distance M|KM|FT|MI] [GEOM geom] [COUNT count] [ASC|DESC] [WITHDIST] [WITHOUTWKT] |
| 时间复杂度 | 最理想情况： 最差情况：O(log n) |
| 命令描述 | 在指定经、纬度及半径距离范围内，查找目标 area 中的点。 |
| 选项 | area ：一个几何概念。 RADIUS ：传入经度（longitude）、纬度（latitude）、半径距离（distance）和半径单位（M 表示米、KM 表示千米、FT 表示英尺、MI 表示英里）进行搜索，例如 RADIUS 15 37 200 KM 。 MEMBER ：选择当前 area 中已存在的 POINT 作为搜索原点，并指定半径进行搜索，取值顺序为多边形名称（field）、半径（distance）、半径单位（M 表示米、KM 表示千米、FT 表示英尺、MI 表示英里），例如 MEMBER Agrigento 100 KM 。 GEOM ：按照 WKT 的格式设置搜索范围，可以是任意多边形，例如 GEOM 'POLYGON((10 30,20 30,20 40,10 40))' 。 COUNT ：用于限定返回的个数，例如 COUNT 3 。 ASC | DESC ：用于控制返回信息按照距离排序， ASC 表示根据中心位置，由近到远排序； DESC 表示由远到近排序。 WITHDIST ：用于控制是否返回目标点与搜索原点的距离。 WITHOUTWKT ：用于控制是否返回目标点的 WKT 信息，如果加上该参数，则不返回 WKT 信息。 说明 只能同时使用 RADIUS 、 MEMBER 和 GEOM 中的一种方式。 |
| 返回值 | 执行成功：命中的目标点数量与 WKT 信息。 area 不存在：empty list or set。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 GIS.ADD Sicily "Palermo" "POINT (13.361389 38.115556)" "Catania" "POINT(15.087269 37.502669)" 命令。 命令示例： GIS.SEARCH Sicily RADIUS 15 37 200 km WITHDIST ASC 返回示例： 1) (integer) 2 2) 1) "Catania" 2) "POINT(15.087269 37.502669)" 3) "56.4413" 4) "Palermo" 5) "POINT(1
