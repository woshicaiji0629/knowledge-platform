## 支持的数据类型
OSS中的CSV数据默认是String类型，您可以使用CAST函数进行数据转换。
通过SQL查询语句将_1和_2转换为int的示例：Select * from OSSOBject where cast (_1 as int) > cast(_2 as int)
SelectObject支持在Where条件中隐式转换，例如下面语句中的第一列和第二列将被转换成int：
Select _1 from ossobject where _1 + _2 > 100
对于JSON文件，若SQL中未指定cast函数，其类型根据JSON数据的实际类型而定，标准JSON内建的数据类型包括null、bool、int64、double、string等类型。
