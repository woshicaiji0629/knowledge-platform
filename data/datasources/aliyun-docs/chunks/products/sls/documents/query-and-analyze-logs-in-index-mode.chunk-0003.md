-to-query-and-analyze-logs.md) ：当您需要对日志数据进行结构化信息提取、字段操作和数据过滤时，可以使用 SPL。 重要 分析语句默认分析当前 LogStore 中的数据，不需要填写 FROM 子句和 WHERE 子句。 分析语句不支持使用 offset，不区分大小写，末尾不需要加分号。 |

日志服务查询分析提供了antlr语法文件，支持用户结合antlr工具进行基于SLS查询的二次开发。
以下是antlr语法文件：
[IndexQueryParser](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250814/jjzlqs/IndexQueryParser.g4)
[IndexQueryLexer](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250814/jodlnb/IndexQueryLexer.g4)
