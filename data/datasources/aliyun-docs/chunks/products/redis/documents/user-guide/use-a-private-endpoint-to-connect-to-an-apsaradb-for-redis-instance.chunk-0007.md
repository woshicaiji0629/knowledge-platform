## PhpRedis
本示例的PhpRedis版本为5.3.7，更多信息请参见[PhpRedis](https://github.com/phpredis/phpredis)。
<?php // 直连地址和连接端口。 $array = ['r-bp1xxxxxxxxxxxx.redis.rds.aliyuncs.com:6379']; // 连接密码。 $pwd = "xxxx"; // 使用密码连接集群。 $obj_cluster = new RedisCluster(NULL, $array, 1.5, 1.5, true, $pwd); // 输出连接结果。 var_dump($obj_cluster); if ($obj_cluster->set("foo", "bar") == false) { die($obj_cluster->getLastError()); } $value = $obj_cluster->get("foo"); echo $value; ?>
