## Unexpected parameters (bigint) for function url_decode. Expected: url_decode(varchar(x))
错误描述[​](https://sls.aliyun.com/doc/sqlerror/unexpected_parameters_for_function.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
SQL语句中存在语法错误，使用SQL函数时，输入的参数类型不正确。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/unexpected_parameters_for_function.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
该函数需要接收一个字符串类型的参数，但是输入的参数类型为bigint。
这类错误可能出现在不同的函数中，不一定是url_decode，也有可能是regexp_like，但错误原因一样：使用SQL函数时，输入的参数类型不正确。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/unexpected_parameters_for_function.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
将输入的参数转换为字符串类型后再传递给url_decode函数。可以使用CAST或CONVERT函数将bigint类型的参数转换为字符串类型的参数，或者直接在调用该函数时使用引号将参数括起来，将其转换为字符串类型。例如：
SELECT url_decode(CAST(bigint_param AS varchar(20))) -- 使用CAST函数将bigint类型参数转换为字符串类型SELECT url_decode('123456789') -- 若参数是字面量，可以直接将参数括起来，将其转换为
