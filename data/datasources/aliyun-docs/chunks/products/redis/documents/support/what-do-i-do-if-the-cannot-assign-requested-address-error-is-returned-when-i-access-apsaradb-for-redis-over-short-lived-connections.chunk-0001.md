### 使用Pconnect替换Connect（推荐）
用长连接替代短连接，该方案可减少TCP连接，同时可以避免每次请求都会重新建立连接的问题，减少延时。
例如Connect连接代码示例如下：
$redis->connect('[$Hostname]', [$Port]); $redis->auth('[$Inst_Password]');
参数说明：[$Hostname]、[$Port]和[$Inst_Password]分别为Redis实例的连接地址、端口号和密码，如何查看请参见[查看连接地址](../user-guide/view-endpoints.md)。
使用Pconnect替换Connect，即使用Persistent Connection的方式连接，示例如下：
$redis->pconnect('[$Hostname]', [$Port], 0, NULL, 0, 0, ['auth' => ['[$Inst_Password]']]); // 若PhpRedis版本大于等于5.3.0，建议使用Pconnect初始化方式，避免断连时出现no auth。 // timeout、persistent_id、retry_interval和read_timeout等参数根据业务实现情况修改。
