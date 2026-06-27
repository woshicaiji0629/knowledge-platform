### PhpRedis
下载并安装[PhpRedis](https://github.com/phpredis/phpredis)客户端。
在PHP编辑器中输入下述代码，然后根据注释提示修改代码。
本示例的PHP版本为8.2.1、PhpRedis版本为5.3.7。
<?php /* 分别将host和port的值替换为实例的连接地址、端口号。 */ $host = "r-bp10noxlhcoim2****.redis.rds.aliyuncs.com"; $port = 6379; /* 分别将user和pwd的值替换为实例的账号和密码 */ $user = "testaccount"; $pwd = "Rp829dlwa"; $redis = new Redis(); if ($redis->connect($host, $port) == false) { die($redis->getLastError()); } if ($redis->auth([$user, $pwd]) == false) { die($redis->getLastError()); } /* 完成认证后可执行数据库操作，下述代码为您提供SET与GET的使用示例。 */ if ($redis->set("foo", "bar") == false) { die($redis->getLastError()); } $value = $redis->get("foo"); echo $value; ?>
执行上述代码。
说明
常见报错与解决方法：
Cannot assign requested address，原因分析及排查方法，请参见[Cannot assign requested address](../support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)[报错](../support/what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)。
redis protocol error, got ' ' as reply type byte，请升级您的PhpRedis客户端版本，参见[phpredis/phpredis#1585](https://github.com/phpredis/phpredis/issues/1585)。
