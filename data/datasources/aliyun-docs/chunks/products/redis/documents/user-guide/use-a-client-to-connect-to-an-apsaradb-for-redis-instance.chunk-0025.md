client.Set(ctx, "foo", "bar", 0).Err(); err != nil { panic(err) } val, err := client.Get(ctx, "foo").Result() if err != nil { panic(err) } fmt.Println("set : foo -> ", val) } func main() { ExampleClient() }
执行上述代码。
