## ErrorType:SyntaxError.ErrorPosition,line:1,column:19.ErrorMessage:line 1:19: Expression "data" is not of type ROW
报错原因
查询和分析语句中所使用的字段的数据类型错误。
解决方法
请检查ROW函数的参数是否正确，并且参数中所有的字段是否存在且符合要求。如果参数正确，但结果仍然不是ROW类型，可以尝试使用CAST函数将其转换为ROW类型。
