### 基于最后一次修改时间的生命周期规则是否支持将Object从低频访问类型转换为标准类型？
不支持。您可以通过以下方式将Object从低频访问类型转为标准类型：
通过CopyObject的方式
CopyObject接口支持将单个Object从低频访问类型转为标准类型。
通过ossutil工具
ossutil支持通过set-meta命令添加X-Oss-Storage-Class选项的方式将单个或多个Object从低频访问类型转换为标准类型。具体操作，请参见[设置或更新元数据](../developer-reference/set-meta.md)。
