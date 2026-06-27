## Go-redis
本示例的Go版本为1.19.7、Go-redis版本为9.5.1。
重要
请使用Go-redis v9.0及以上版本，否则在使用直连模式地址时，可能会产生[不兼容报错](../support/common-errors-and-troubleshooting.md)。
package main import ( "context" "fmt" "github.com/go-redis/redis/v9" ) var ctx = context.Background() func main() { rdb := redis.NewClusterClient(&redis.ClusterOptions{ Addrs: []string{"r-bp10noxlhcoim2****.redis.rds.aliyuncs.com:6379"}, Username: "testaccount", Password: "Rp829dlwa", }) err := rdb.Set(ctx, "key", "value", 0).Err() if err != nil { panic(err) } val, err := rdb.Get(ctx, "key").Result() if err != nil { panic(err) } fmt.Println("key", val) }
