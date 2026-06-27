### Error while reading line from the server.
可能原因：读取超时，您可能正在执行一个慢查询。
解决方法：适当增大超时时间或将客户端的read_write_timeout参数改为0或-1，更多信息请参见[Predis questions](https://stackoverflow.com/questions/11776029/predis-is-giving-error-while-reading-line-from-server/11931651#11931651)。
