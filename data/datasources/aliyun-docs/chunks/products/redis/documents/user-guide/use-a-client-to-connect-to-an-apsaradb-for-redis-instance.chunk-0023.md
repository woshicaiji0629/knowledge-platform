### node-redis
下载并安装[node-redis](https://github.com/redis/node-redis)客户端。
在node-redis客户端中输入下述代码，然后根据注释提示修改代码。
本示例的Node.js版本为19.4.0、node-redis版本为4.5.1。
import { createClient } from 'redis'; // 分别设置实例的端口号、连接地址、账号、密码 const host = 'r-bp10noxlhcoim2****.redis.rds.aliyuncs.com'; const port = 6379; const username = 'testaccount'; // 如果密码中包含特殊字符（!@#$%^&*()+-=_）建议用encodeURIComponent进行编码:password = encodeURIComponent(password) const password = 'Rp829dlwa'; const client = createClient({ // redis://[[username]:[password]@[host][:port]/[db-number] url: `redis://${username}:${password}@${host}:${port}/0` }); client.on('error', (err) => console.log('Redis Client Error', err)); await client.connect(); await client.set('foo', 'bar'); const value = await client.get('foo'); console.log("get foo: %s", value); await client.disconnect();
说明
若提示SyntaxError: Cannot use import statement outside a module，请将.js文件的后缀改为.mjs，并在调用时增加--experimental-modules选项，例如node --experimental-modules redis.mjs。
执行上述代码。
