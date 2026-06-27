### 双可用区实例
在双可用区、读写分离架构实例，实例将分别提供主、备可用区连接地址。其中备可用区连接地址仅用于读请求，可实现就近访问，缩短读请求延迟。
例如实例为杭州I（主可用区）、杭州J（备可用区）。
位于杭州I的客户端（ECS实例）可以连接实例的主可用区地址，并执行读写操作。代码如下：
import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig; public class MasterReadWrite { public static void main(String[] args) { JedisPoolConfig config = new JedisPoolConfig(); config.setMaxIdle(200); config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); // 配置主可用区连接地址、端口、账号密码信息。 String host = "r-bp1vtq8tnrquy****pd.redis.rds.aliyuncs.com"; int port = 6379; String password = "default:Passw***2"; JedisPool pool = new JedisPool(config, host, port, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); // 执行相关操作，示例如下。 jedis.set("foo", "bar"); System.out.println(jedis.get("foo")); } catch (Exception e) { // 超时或其他异常处理。 e.printStackTrace(); } finally { if (jedis != null) { jedis.close(); } } pool.destroy(); // 当应用退出，需销毁资源时，调用此方法。此方法会断开连接、释放资源。 } }
位于杭州J的客户端（ECS实例）可以连接实例的备可用区地址，并仅执行读操作（如需执行写操作，仍需连接主可用区地址）。代码如下：
import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig; public class
