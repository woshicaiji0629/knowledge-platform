### 分析结果分页示例
您可以使用SQL中的Limit语法实现分析结果分析显示，例如通过* | select count(1) , url group by url语句进行查询分析，指定返回1000行日志。您可以通过分页指定每次读取500行，共2次读取完成，示例如下：
* | select count(1) , url group by url limit 0, 500 * | select count(1) , url group by url limit 500, 500
分析结果分页的示例代码逻辑
offset = 0 //指定从某一行开始读取查询结果，此处从第0行开始读取。 line = 500 //指定当前请求读取的行数，最大值为1,000,000。如果一次读取太多，会影响网络延时和客户端的处理速度。此处每次读取500行。 query = "* | select count(1) , url group by url limit " while True: real_query = query + offset + "," + line response = get_logstore_logs(real_query) //执行读取请求。 process (response) //调用自定义逻辑，处理返回的结果。 如果 response.get_count() == 0 则读取结束，跳出当前循环 否则 offset += 500 //offset增加到500，读取下一个500行。
