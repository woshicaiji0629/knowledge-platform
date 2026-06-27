### redis protocol error, got ' ' as reply type byte
可能原因：phpredis低版本Bug，更多信息请参见[phpredis/phpredis#1585](https://github.com/phpredis/phpredis/issues/1585)。
解决方法：将phpredis升级至最新版。
