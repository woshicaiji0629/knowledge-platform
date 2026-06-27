## you are using nested sql, please specify FROM LogStore in the innermost sql
错误描述[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
您正在SQL中使用嵌套子查询，请在最内层的子查询中指定表名。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
SLS为了简化用户查询，在进行单表查询时，默认指定当前所在LogStore为FROM所在表。假设您当前LogStore名为test，那么，以下3个查询语句是同义的：
语句1：您可以不指定FROM子句。
语句2：您可以使用FROM log，这将指定当前所在LogStore。
语句3：您可以明确指定您查询的表为LogStore为test。
但当您进行包含子查询的复杂查询时，SLS无法为您推断各子查询中目标表，所以您必须在子查询中手动指定FROM子句。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/innermost_sql_missing_from.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
如果您想查询当前LogStore，您可以直接使用"FROM log"常量字符串指定From表为当前LogStore。
当然您也可以明确指定您要查询的目标LogStore名字。
