# 使用redis-cli代码DMS连接Tair实例-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/getting-started/step-3-connect-to-an-apsaradb-for-redis-instance

# 步骤3：连接实例
本示例指导您通过redis-cli、代码和[数据管理](https://help.aliyun.com/zh/dms/product-overview/what-is-dms)[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms)快速连接云数据库 Tair（兼容 Redis）。
## 前提条件
已设置实例的[IP](step-2-configure-whitelists.md)[白名单](step-2-configure-whitelists.md)。
已设置实例密码，未设置请参见[修改或重置密码](../user-guide/change-or-reset-the-password.md)（创建实例时已设置请忽略）。
## 操作步骤
## redis-cli
本示例在ECS（Linux）上使用redis-cli访问处于同一专有网络的云数据库 Tair（兼容 Redis）。
说明
本地连接请[申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)后使用公网地址连接。
登录ECS实例，依次执行以下命令，下载、安装编译redis-cli。
sudo yum -y install gcc # 安装gcc依赖环境 wget https://download.redis.io/releases/redis-7.2.0.tar.gz tar xzf redis-7.2.0.tar.gz cd redis-7.2.0&&make
本文以redis-7.2.0版本为例演示操作流程，您也可以安装其他版本。编译安装通常需要2分钟~3分钟。
执行下述命令连接实例。
src/redis-cli -hhostname-apassword-pport
参数说明：
hostname：实例连接地址，您可以在控制台的连接信息区域获取实例的专有网络连接地址，例如r-8vbwds91ie1rdl****.redis.zhangbei.rds.aliyuncs.com，更多信息请参见[查看连接地址](../user-guide/view-endpoints.md)。
password：密码。
port：端口号，默认为6379。
连接示例：
src/redis-cli -h r-8vbwds91ie1rdl****.redis.zhangbei.rds.aliyuncs.com -a TestPassword123 -p 6379
写入与读写数据。
执行命令SET bar foo。
预计返回OK。
执行命令GET bar。
预计返回"foo"。
## 代码连接
说明
本地连接请[申请公网连接地址](../user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance.md)后使用公网地址连接。
本示例使用Jedis客户端进行连接，完整代码示例[redistest](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250410/idlmmy/redistest.zip)。其他常见客户端连接代码请参见[常见客户端连接示例](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)。
添加pom.xml配置。
<!-- 导入spring-data-redis --> <dependency> <groupId>org.springframework.boot</groupId> <artifactId>spring-boot-starter-data-redis</artifactId> <!-- spring boot 2.0之后默认使用lettuce客户端, 使用jedis时需要排包 --> <exclusions> <exclusion> <groupId>io.lettuce</groupId> <artifactId>lettuce-core</artifactId> </exclusion> </exclusions> </dependency> <!-- 导入jedis --> <dependency> <groupId>redis.clients</groupId> <artifactId>jedis</artifactId> </dependency>
配置连接信息，请根据注释修改对应参数。
@Configuration public class RedisConfig { @Bean JedisConnectionFactory redisConnectionFactory() { //本案例仅用于测试连接，生产环境建议将连接信息填写到配置文件中，通过@Value注解读取 //连接地址（hostName）和端口（port）在实例详情页下方连接信息区域获取，请根据客户端网络环境选择专有网络或公网连接 RedisStandaloneConfiguration config = new RedisStandaloneConfiguration("r-8vbwds91ie1rdl****.redis.zhangbei.rds.aliyuncs.com", 6379); //password填写格式为 账号:密码，例如：账号testaccount，密码Rp829dlwa，password填写testaccount:Rp829dlwa //忘记账号密码请在实例详情页左侧菜单列表点击账号管理重置密码或创建账号 config.setPassword(RedisPassword.of("账号:密码")); JedisPoolConfig jedisPoolConfig = new JedisPoolConfig(); // 最大连接数, 根据业务需要设置，不能超过实例规格规定的最大连接数。 jedisPoolConfig.setMaxTotal(30); // 最大空闲连接数, 根据业务需要设置，不能超过实例规格规定的最大连接数。 jedisPoolConfig.setMaxIdle(20); // 关闭 testOn[Borrow|Return]，防止产生额外的PING。 jedisPoolConfig.setTestOnBorrow(false); jedisPoolConfig.setTestOnReturn(false); JedisClientConfiguration jedisClientConfiguration = JedisClientConfiguration.builder().usePooling().poolConfig( jedisPoolConfig).build(); return new JedisConnectionFactory(config, jedisClientConfiguration); } @Bean public RedisTemplate<String, Object> redisTemplate() { RedisTemplate<String, Object> template = new RedisTemplate<>(); template.setConnectionFactory(redisConnectionFactory()); template.setKeySerializer(new StringRedisSerializer()); template.setValueSerializer(new GenericJackson2JsonRedisSerializer()); return template; } }
测试连接。
@SpringBootTest public class RedisTest { @Autowired private RedisTemplate<String, Object> redisTemplate; @Test void test() { try { redisTemplate.opsForValue().set("test_key", "hello world！"); System.out.println("连接成功:"+redisTemplate.opsForValue().get("test_key")); } catch (Exception e) { e.printStackTrace(); System.out.println("连接出现异常，请根据文档：" + "https://help.aliyun.com/zh/redis/support/how-do-i-troubleshoot-connection-issues-in-apsaradb-for-redis" + "排查网络、白名单、账号密码问题。" + "也可根据报错信息查询文档：https://help.aliyun.com/zh/redis/support/common-errors-and-troubleshooting"); } } }
运行上述代码,连接成功将返回如下结果：
连接成功:hello world！
## DMS
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在页面右上角，单击登录数据库。
在DMS登录页面，选择访问方式为密码登录，并输入密码。
此方式将使用默认账号进行登录，您可以在控制台的账号管理页面查看账号详情信息。
单击登录。
写入与读写数据。
在DMSSQLConsole页面，输入命令SET foo hello，并单击执行(F8)。
预计返回OK。
输入命令GET foo，并单击执行(F8)。
预计返回hello。
## 相关文档
以下文档中将提供更详细的说明与示例。
[客户端程序连接教程](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)
[通过](../user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](../user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](../user-guide/use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)
[通过](../user-guide/log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md)[DMS](../user-guide/log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md)[连接实例](../user-guide/log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md)
特殊连接方式
[启用](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)[TLS（SSL）加密连接实例](../user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance-that-has-ssl-encryption-enabled.md)：启用TLS加密功能提高数据链路的安全性，保障数据的完整性。
[使用直连模式连接实例](../user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)：集群架构实例可申请直连地址，通过该地址可直接访问后端的数据分片（类似连接原生Redis集群）。相比代理模式，直连模式节约了通过代理处理请求的时间，可以在一定程度上提高实例的响应速度。
[使用](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[Sentinel](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[兼容模式连接实例](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)：实例提供Sentinel（哨兵）兼容模式，开启后客户端可以像连接原生Redis Sentinel一样连接实例。
## 常见报错
| 报错信息 | 原因及解决方法 |
| --- | --- |
| (error) ERR illegal address | 未设置正确的白名单，可依次排查如下事项： 是否已将客户端的 IP 地址添加至实例的白名单中，详情请参见 [设置白名单](step-2-configure-whitelists.md) 。 是否选择正确的实例连接地址，例如通过公网连接实例，需连接实例的公网连接地址，若此时选择实例的专有网络连接地址会导致连接失败。 使用 ECS 通过专有网络连接时，检查 ECS 是否与实例为同一 VPC，若两者不是同一 VPC，则可使用公网的方式进行访问。 排查后，可通过 ping 实例地址 进行测试，例如 ping r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com ，若返回正常，则表示客户端与实例可正常连接。 |
| (error) ERR client ip is not in whitelist |  |
| Could not connect to Redis |  |
| (error) ERR invalid password (error) WRONGPASS invalid username-password pair | 密码错误，请使用正确的密码和密码格式。根据选取账号的不同，密码格式有一定区别。 使用默认账号：直接填写密码即可。例如实例默认账号为 r-bp1zxszhcgatnx**** ，自定义密码为 Password21 ，密码验证命令为 AUTH Password21 。 使用新创建的账号：密码格式为 user:password 。例如自定义账号为 testaccount ，密码为 Rp829dlwa ，密码验证命令为 AUTH testaccount:Rp829dlwa 。 说明 如果通过第三方数据库管理工具（例如 RDM 等）连接实例，请在密码框中输入 user:password 进行连接，请不要在 用户名 框中输入任何信息，否则会导致连接失败。 如果忘记密码，您可以重置密码。具体操作，请参见 [修改或重置密码](../user-guide/change-or-reset-the-password.md) 。 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
