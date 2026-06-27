## 代码连接
说明
本地连接请[申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)后使用公网地址连接。
本示例使用Jedis客户端进行连接，完整代码示例[redistest](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250410/idlmmy/redistest.zip)。其他常见客户端连接代码请参见[常见客户端连接示例](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)。
添加pom.xml配置。
<!-- 导入spring-data-redis --> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-data-redis</artifactId> <!-- spring boot 2.0之后默认使用lettuce客户端, 使用jedis时需要排包 --> <exclusions> <exclusion> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> </exclusion> </exclusions> </dependency> <!-- 导入jedis --> <dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> </dependency>
配置连接信息，请根据注释修改对应参数。
@Configuration public class RedisConfig { @Bean JedisConnectionFactory redisConnectionFactory() { //本案例仅用于测试连接，生产环境建议将连接信息填写到配置文件中，通过@Value注解读取 //连接地址（hostName）和端口（port）在实例详情页下方连接信息区域获取，请根据客户端网络环境选择专有网络或公网连接 RedisStandaloneConfiguration config = new RedisStandaloneConfiguration("r-8vbwds91ie1rdl****.redis.zhangbei.rds.aliyuncs.com", 6379); //password填写格式为 账号:密码，例如：账号tes
