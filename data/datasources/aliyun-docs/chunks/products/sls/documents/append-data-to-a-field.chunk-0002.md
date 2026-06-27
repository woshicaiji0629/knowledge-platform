## 示例
例如Logtail所在服务器的IP地址为192.0.2.1，主机名为david，存在环境变量WORKING_GROUP的值为prod。如果您需要为__labels__字段添加以上数据，可参见如下配置：
原始数据
"__labels__":"a#$#b"
Logtail插件处理配置
{ "processors":[ { "type":"processor_appender", "detail": { "Key": "__labels__", "Value": "|host#$#{{__host__}}|ip#$#{{__ip__}}|group#$#{{$WORKING_GROUP}}", "SortLabels": true } } ] }
处理结果
"__labels__":"a#$#b|group#$#prod|host#$#david|ip#$#192.0.2.1"
该文章对您有帮助吗？
反馈
