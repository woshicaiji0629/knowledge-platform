# 创建和管理云数据库 Tair（兼容 Redis）账号-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/create-and-manage-database-accounts

# 创建与管理账号
云数据库 Tair（兼容 Redis）支持创建多个账号，且支持设置只读、读写权限，帮助您更加灵活地管理实例，最大限度地避免误操作，提升数据安全性。
## 背景信息
为保障数据安全性，实例完成创建后会自动创建默认账号，默认账号不支持删除、替换以及修改权限。根据实例的引擎版本不同，自动创建的默认账号数量有所区别：
6.0以下版本：自动创建一个默认账号，账号名为实例ID（例如r-bp1jpghfglv6******）。
6.0及以上版本：自动创建两个默认账号，账号名分别为实例ID（例如r-bp1jpghfglv6******）和default。
您或许在创建实例时已设置默认账号的密码（也可能未设置），您可以在控制台的账号管理页面进行查看或重置密码。
默认账号的登录方式与原生Redis一致，仅输入密码即可登录，redis-cli连接示例如下：
# 例如默认账号为r-bp1jpghfglv6******，密码为Rp829dlwa。 redis-cli -h r-bp1zx****.redis.rds.aliyuncs.com -p 6379 -a Rp829dlwa
## 前提条件
实例的引擎版本为兼容Redis 4.0或以上。
说明
如果实例的引擎版本不满足要求，您可以评估业务后升级实例的引擎版本，详情请参见[升级大版本](upgrade-the-major-version-1.md)。
## 注意事项
单个实例最多能创建20个账号。
Redis开源版4.0实例及5.0实例（5.0.8版本之前），账号名称的大小写不敏感。之后版本账号名称的大小写敏感。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击账号管理。
单击页面右侧的创建账号。
在弹出的对话框中，设置账号信息。
| 配置 | 说明 |
| --- | --- |
| 账号类型 | 本地账号 ：表示您需要额外记录该账号口令，或在应用代码中通过明文配置数据库账号口令。 KMS 托管账号 ：通过 [KMS](../../../kms/documents/key-management-service/product-overview/what-is-key-management-service-1.md) 托管实例的账号密码，应用程序将无需配置静态数据库账号口令，应用程序访问实例时，调用相关 KMS 接口获取实例账号和口令信息，更多信息请参见 [通过](../use-cases/use-kms-to-manage-redis-credentials.md) [KMS](../use-cases/use-kms-to-manage-redis-credentials.md) [托管实例密码凭证](../use-cases/use-kms-to-manage-redis-credentials.md) 。 |
| 账号 | 账号名需满足以下条件： 以英文字母开头，由小写英文字母、数字或下划线（_）组成。 长度不超过 35 个字符。 不能为 [Redis](create-and-manage-database-accounts.md) [账号名保留字](create-and-manage-database-accounts.md) 。 |
| 权限设置 | 设置该账号所拥有的权限： 只读 ：仅拥有读取数据的权限，不允许修改数据。 读写 ：拥有读、写以及删除数据的权限。 |
| 密码 | 设置该账号的密码，需满足以下条件： 由大写英文字母、小写英文字母、数字、特殊字符中的至少三种组成，特殊字符为： !@#$%^&*()+-=_ 长度为 8~32 个字符。 |
| 确认密码 | 再次输入密码进行确认。 |
| 备注 （可选） | 账号的备注信息，需满足以下条件： 以英文字母或中文开头，且不能以 http:// 或 https:// 开头。 由英文字母、中文、数字、下划线（_）或短划线（-）组成。 长度为 2~256 字符。 |
单击确定。
新建账号后，请在约一分钟后刷新控制台页面，账号状态将变更为可用。
说明
新建账号的密码格式为user:password，例如新建账号为testaccount，密码为Rp829dlwa，实例的登录密码需填写为testaccount:Rp829dlwa，更多信息请参见[实例的登录方式](logon-methods.md)。
若是通过第三方数据库管理工具（例如RDM等）连接Redis实例，请在密码框中输入user:password进行连接。
可选：根据业务需求，您可以选择下述步骤管理账号：
重置密码
单击目标账号操作列的重置密码，然后在弹出的对话框中，重新设置账号的密码并单击确定。
修改权限
单击目标账号操作列的修改权限，然后在弹出的对话框中，选择所需权限并单击确定。
修改备注说明
单击目标账号操作列的修改备注，然后在弹出的对话框中，重新设置备注信息并单击确定。
删除账号
单击目标账号操作列的>删除，然后在弹出的对话框中单击确定。
警告
删除账号后，您将无法使用该账户登录。为保障不影响客户端连接，请提前将客户端的验证方式修改为其他账号、密码。
## Redis账号名保留字
创建账号时，账号名不能为下述保留字，保留字以英文逗号（,）分隔列举：
| 首字母 | 保留字 |
| --- | --- |
| a~c | add,admin,all,alter,analyze,and,as,asc,asensitive,aurora,before,between,bigint,binary,blob,both,by,call,cascade,case,change,char,character,check,collate,column,condition,connection,constraint,continue,convert,create,cross,current_date,current_time,current_timestamp,current_user,cursor |
| d~f | database,databases,day_hour,day_microsecond,day_minute,day_second,dec,decimal,declare,default,delayed,delete,desc,describe,deterministic,distinct,distinctrow,div,double,drc_rds,drop,dual,each,eagleye,else,elseif,enclosed,escaped,exists,exit,explain,false,fetch,float,float4,float8,for,force,foreign,from,fulltext |
| g~l | goto,grant,group,guest,having,high_priority,hour_microsecond,hour_minute,hour_second,if,ignore,in,index,infile,information_schema,inner,inout,insensitive,insert,int,int1,int2,int3,int4,int8,integer,interval,into,is,iterate,join,key,keys,kill,label,leading,leave,left,like,limit,linear,lines,load,localtime,localtimestamp,lock,long,longblob,longtext,loop,low_priority |
| m~r | match,mediumblob,mediumint,mediumtext,middleint,minute_microsecond,minute_second,mod,modifies,mysql,natural,no_write_to_binlog,not,null,numeric,on,optimize,option,optionally,or,order,out,outer,outfile,precision,primary,procedure,purge,raid0,range,read,reads,real,references,regexp,release,rename,repeat,replace,replicator,require,restrict,return,revoke,right,rlike,root |
| s~z | schema,schemas,second_microsecond,select,sensitive,separator,set,show,smallint,spatial,specific,sql,sql_big_result,sql_calc_found_rows,sql_small_result,sqlexception,sqlstate,sqlwarning,ssl,starting,straight_join,table,terminated,test,then,tinyblob,tinyint,tinytext,to,trailing,trigger,true,undo,union,unique,unlock,unsigned,update,usage,use,using,utc_date,utc_time,utc_timestamp,values,varbinary,varchar,varcharacter,varying,when,where,while,with,write,x509,xor,xtrabak,year_month,zerofill |
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [CreateAccount](../developer-reference/api-r-kvstore-2015-01-01-createaccount-redis.md) | 在实例中创建有特定权限的账号。 |
| [GrantAccountPrivilege](../developer-reference/api-r-kvstore-2015-01-01-grantaccountprivilege-redis.md) | 修改实例中账号的权限。 |
| [ModifyAccountDescription](../developer-reference/api-r-kvstore-2015-01-01-modifyaccountdescription-redis.md) | 修改实例中账号的描述。 |
| [ModifyAccountPassword](../developer-reference/api-r-kvstore-2015-01-01-modifyaccountpassword-redis.md) | 修改实例中指定账号的密码。 |
| [DeleteAccount](../developer-reference/api-r-kvstore-2015-01-01-deleteaccount-redis.md) | 删除实例中的指定账号。 |
## 常见问题
### 账号创建失败怎么办？
每个实例最多可设置20个账号，若超出，请删除不再使用的账号后重新创建。
连续创建时账号请等待上一个账号状态为可用时，再进行创建。
升级实例小版本后再尝试创建。
## 相关文档
[通过](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[redis-cli](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)[连接实例](use-redis-cli-to-connect-to-an-apsaradb-for-redis-instance.md)
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
