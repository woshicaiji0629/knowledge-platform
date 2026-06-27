## ErrorType:ColumnNotExists.ErrorPosition,line:0,column:1.ErrorMessage:line 1:123: Column 'XXX' cannot be resolved; it seems XXX is wrapper by ";if XXX is a string ,not a key field, please use 'XXX'
报错原因
XXX不是索引字段，不能使用双引号（""）包裹。在分析语句中，表示字符串的字符必须使用单引号（''）包裹，无符号包裹或被双引号（""）包裹的字符表示字段名或列名。
解决方法
如果XXX为分析字段，您需要为该字段配置索引，并开启统计功能。具体操作，请参见[创建索引](create-indexes.md)。
如果XXX为普通字符串，需要使用单引号（''）包裹。
