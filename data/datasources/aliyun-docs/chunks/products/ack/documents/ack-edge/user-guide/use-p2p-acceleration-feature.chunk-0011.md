### 审计日志
开启审计日志
修改p2p configmap里audit字段为true。
DeployConfig: mode: agent logDir: /dadi-p2p/log logAudit: true logAuditMode: stdout # 输出到控制台, file为输出到日志目录/dadi-p2p/log/audit.log
审计日志格式
格式如下，其含义为：从接收到请求至结果返回的处理耗时，单位：us。
2022/08/30 15:44:52|AUDIT|th=00007FBA247C5280|download[pathname=/https://cri-pi840la*****-registry.oss-cn-hangzhou.aliyuncs.com/docker/registry/v2/blobs/sha256/dd/dd65726c224b09836aeb6ecebd6baf58c96be727ba86da14e62835569896008a/data][offset=125829120][size=2097152][latency=267172] .... 2022/08/30 15:44:55|AUDIT|th=00007FBA2EFEAEC0|http:pread[pathname=/https://cri-pi840lacia*****-registry.oss-cn-hangzhou.aliyuncs.com/docker/registry/v2/blobs/sha256/dd/dd65726c224b09836aeb6ecebd6baf58c96be727ba86da14e62835569896008a/data][offset=127467520][size=65536][latency=21]
主要字段为：时间、 AUDIT、线程指针、操作码[pathname=][size=][latency=]。
其中AUDIT和线程指针一般不用关心，size为单次请求大小，若为负数则表示异常；latency为单次请求延迟，单位：us。
常见操作码如下：
http:pread：表示HTTP Proxy处理下游数据请求。
rpc:stat：表示P2P Agent获取文件长度。
rpc:pread：表示P2P Agent处理下游数据请求。
download：表示P2P Agent从上游下载数据。
filewrite：表示P2P Agent写入当前数据分片到缓存。
fileread：表示P2P Agent从缓存读取数据分片。
日志示例
download[pathname=mytest][offset=0][size=65536][latency=26461] ## P2P Agent从上游下载mytest文件[0,65536)这
