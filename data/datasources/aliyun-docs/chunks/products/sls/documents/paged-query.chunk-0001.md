### 查询结果分页示例
在分页读取时，不停地增大offset的值，直到读取到某个offset值后，获取的结果行数为0，并且结果的progress为complete状态，则表示读取了所有数据。
分页的示例代码逻辑
offset = 0 #指定从某一行开始读取查询结果，此处从第0行开始读取。 line = 100 #指定当前请求读取的行数，最大值为100。如果大于100，则仍然返回100行。此处每次读取100行。 query = "status:200" #查询status字段是200的所有日志。 while True: response = get_logstore_logs(query, offset, line) #执行读取请求。 process (response) #调用自定义逻辑，处理返回结果。 如果 response.get_count() == 0 && response.is_complete() 则读取结束，跳出当前循环 否则 offset += 100 # offset增加到100，读取下一个100行。
