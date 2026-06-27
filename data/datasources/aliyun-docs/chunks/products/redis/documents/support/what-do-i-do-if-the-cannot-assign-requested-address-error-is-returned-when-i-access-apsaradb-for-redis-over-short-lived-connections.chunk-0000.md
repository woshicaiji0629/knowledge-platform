## 问题原因
该报错通常出现在客户端使用PHP-FPM与PhpRedis组合的架构中，这种架构在高并发场景时，处于TIME-WAIT状态下的TCP连接数较多，客户端无法分配出新的端口，则会出现Cannot assign requested address报错。
