## key (XXX) is not config as key value config,if symbol : is in your log,please wrap : with quotation mark "
报错原因
未对XXX字段建立字段索引，或者您所使用的字段中包含了特殊字符（例如空格）但未使用双引号（""）包裹。
解决方法
确认是否已为目标字段创建字段索引且开启统计功能。
如果是，请执行下一步。
如果不是，请先为目标字段创建字段索引且开启统计功能。具体操作，请参见[手动创建字段索引](create-indexes.md)。
执行该操作后，如果问题解决，则无需执行下一步。
使用双引号（""）包裹目标字段。
