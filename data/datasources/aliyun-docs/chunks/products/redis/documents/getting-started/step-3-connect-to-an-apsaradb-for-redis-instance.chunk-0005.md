ingRedisSerializer()); template.setValueSerializer(new GenericJackson2JsonRedisSerializer()); return template; } }
测试连接。
@SpringBootTest public class RedisTest { @Autowired private RedisTemplate<String, Object> redisTemplate; @Test void test() { try { redisTemplate.opsForValue().set("test_key", "hello world！"); System.out.println("连接成功:"+redisTemplate.opsForValue().get("test_key")); } catch (Exception e) { e.printStackTrace(); System.out.println("连接出现异常，请根据文档：" + "https://help.aliyun.com/zh/redis/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis" + "排查网络、白名单、账号密码问题。" + "也可根据报错信息查询文档：https://help.aliyun.com/zh/redis/support/common-errors-and-troubleshooting"); } } }
运行上述代码,连接成功将返回如下结果：
连接成功:hello world！
