## ErrorType:SyntaxError.ErrorPosition,line:1,column:9.ErrorMessage:line 1:9: identifiers must not contain ':'
报错原因
您所分析的字段中包含了半角冒号（:）。
解决方法
使用半角双引号（""）包裹字段。例如您要分析__tag__:__receive_time__字段，可使用语句*| select "__tag__:__receive_time__"。
重要
在分析字段前，必须先创建字段索引。具体操作，请参见[手动创建字段索引](create-indexes.md)。
