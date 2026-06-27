### Jedis
本示例使用Maven方式进行构建，您也可以手动下载[Jedis](https://github.com/redis/jedis/releases)客户端。
打开编译器，新建项目。
在pom.xml文件中添加下述代码。
本示例的Jedis版本为4.3.0。
<dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> <version>4.3.0</version> </dependency>
在编辑器中输入下述代码，然后根据注释提示修改代码。
import redis.clients.jedis.Jedis; import redis.clients.jedis.JedisPool; import redis.clients.jedis.JedisPoolConfig; public class JedisExample { public static void main(String[] args) { JedisPoolConfig config = new JedisPoolConfig(); // 最大空闲连接数，需自行评估，不超过Redis实例的最大连接数。 config.setMaxIdle(200); // 最大连接数，需自行评估，不超过Redis实例的最大连接数。 config.setMaxTotal(300); config.setTestOnBorrow(false); config.setTestOnReturn(false); // 分别将host和password的值替换为实例的连接地址、密码。 String host = "r-bp1s1bt2tlq3p1****pd.redis.rds.aliyuncs.com"; // 默认账号password可直接填写密码；新建账号password填写格式为 账号:密码，例如新建账号testaccount，密码Rp829dlwa，password填写testaccount:Rp829dlwa。 String password = "r-bp1s1bt2tlq3p1****:Database123"; JedisPool pool = new JedisPool(config, host, 6379, 3000, password); Jedis jedis = null; try { jedis = pool.getResource(); // 执行相关操作，示例如下。 jedis.set("foo10", "bar"); System.out.println(jedis.get("foo10")); jedis.zadd("sose", 0, "car"); jedis.zadd
