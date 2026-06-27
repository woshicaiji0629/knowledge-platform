e：表示P2P Agent写入当前数据分片到缓存。
fileread：表示P2P Agent从缓存读取数据分片。
日志示例
download[pathname=mytest][offset=0][size=65536][latency=26461] ## P2P Agent从上游下载mytest文件[0,65536)这段数据的延迟为26461us rpc:pread[pathname=mytest][offset=0][size=65536][latency=2] ## P2P Agent向下游返回mytest文件[0,65536)这段数据的延迟为2us http:pread[pathname=mytest][offset=0][size=65536][latency=26461] ## 代理向从上游下载mytest文件[0,65536)这段数据的延迟为26461us
