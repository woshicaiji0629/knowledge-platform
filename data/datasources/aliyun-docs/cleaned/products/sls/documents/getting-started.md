# 日志服务SLS快速入门-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/getting-started

# 使用LoongCollector采集并分析ECS文本日志
通过本快速入门，可在30分钟内从零开始，使用日志服务（SLS）的LoongCollector数据采集器采集一台ECS服务器上的Nginx日志。内容包括配置日志采集、通过SQL查询分析数据、查看可视化仪表盘、设置告警，以及在体验结束后清理资源以避免产生费用。
## 前置准备
开通服务与准备账号
开通日志服务：首次使用时，请登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.36447c08Bv7DT1)，根据页面提示开通服务。
准备账号：
阿里云主账号登录：默认拥有全部权限，可直接操作。
RAM用户登录：需要主账号[授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)相应权限策略：
AliyunLogFullAccess：用于创建和管理日志服务的Project和LogStore等资源。
AliyunECSFullAccess：用于在ECS实例上安装采集Agent。
AliyunOOSFullAccess：用于通过阿里云运维编排服务（OOS）在ECS实例中自动安装采集Agent。
在实际生产过程中，可以通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)，对RAM用户实现更精细化的权限管理
准备ECS实例
确保[ECS](../../ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)[实例](../../ecs/documents/user-guide/use-the-ecs-instance-in-the-console.md)的安全组配置满足出口方向开放80（HTTP）端口和443（HTTPS）端口。
生成模拟日志
[登录](../../ecs/documents/user-guide/connect-to-an-instance-overview.md)[ECS](../../ecs/documents/user-guide/connect-to-an-instance-overview.md)[实例](../../ecs/documents/user-guide/connect-to-an-instance-overview.md)。
创建脚本文件generate_nginx_logs.sh并粘贴以下内容。该脚本向/var/log/nginx/access.log文件中每5秒写入一条标准的Nginx访问日志。
generate_nginx_logs.sh
#!/bin/bash #============================================================================== # 脚本名称: generate_nginx_logs.sh # 脚本描述: 模拟NGINX服务器，持续向access.log写入日志。 #============================================================================== # --- 可配置参数 --- # 日志文件路径 LOG_FILE="/var/log/nginx/access.log" # --- 模拟数据池 --- # 随机IP地址池 IP_ADDRESSES=( "192.168.1.10" "10.0.0.5" "172.16.31.40" "203.0.113.15" "8.8.8.8" "1.1.X.X" "91.198.XXX.XXX" "114.114.114.114" "180.76.XX.XX" "223.5.5.5" ) # HTTP请求方法池 HTTP_METHODS=("GET" "POST" "PUT" "DELETE" "HEAD") # 常见请求路径池 REQUEST_PATHS=( "/index.html" "/api/v1/users" "/api/v1/products?id=123" "/images/logo.png" "/static/js/main.js" "/static/css/style.css" "/login" "/admin/dashboard" "/robots.txt" "/sitemap.xml" "/non_existent_page.html" ) # HTTP状态码池 (可以调整权重，例如多放几个200来提高其出现概率) HTTP_STATUSES=(200 200 200 200 201 301 404 404 500 502 403) # 常见User-Agent池 USER_AGENTS=( "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1" "Mozilla/5.0 (Linux; Android 11; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36" "curl/7.68.0" "Googlebot/2.1 (+http://www.google.com/bot.html)" ) # 常见Referer池 REFERERS=( "https://www.google.com/" "https://www.bing.com/" "https://github.com/" "https://stackoverflow.com/" "-" "-" "-" ) # 检查并创建日志目录 LOG_DIR=$(dirname "$LOG_FILE") if [ ! -d "$LOG_DIR" ]; then echo "日志目录 '$LOG_DIR' 不存在，正在尝试创建..." # 使用 sudo 创建目录，因为通常需要 root 权限 sudo mkdir -p "$LOG_DIR" if [ $? -ne 0 ]; then echo "错误: 无法创建目录 '$LOG_DIR'。请检查权限或手动创建。" exit 1 fi echo "目录创建成功。" fi # 检查日志文件的写入权限 trap 'echo -e "\n\n脚本被中断。正在停止日志生成..."; exit 0;' SIGINT # --- 核心函数 --- # 定义一个函数用于从数组中随机选择一个元素 # 用法: random_element "数组名" function random_element() { local arr=("${!1}") echo "${arr[$((RANDOM % ${#arr[@]}))]}" } # 捕获Ctrl+C中断信号，并优雅退出 trap 'echo -e "\n\n脚本被中断。正在停止日志生成..."; exit 0;' SIGINT # --- 主循环 --- echo "开始生成NGINX模拟日志到 $LOG_FILE ..." echo "每隔 5 秒生成一条日志。" echo "按 Ctrl+C 停止。" sleep 2 # 无限循环，持续生成日志 while true; do # 1. 获取当前时间，格式为 NGINX 默认的 [dd/Mon/YYYY:HH:MM:SS +ZZZZ] timestamp=$(date +'%d/%b/%Y:%H:%M:%S %z') # 2. 从池中随机选择数据 ip=$(random_element IP_ADDRESSES[@]) method=$(random_element HTTP_METHODS[@]) path=$(random_element REQUEST_PATHS[@]) status=$(random_element HTTP_STATUSES[@]) user_agent=$(random_element USER_AGENTS[@]) referer=$(random_element REFERERS[@]) # 3. 生成随机的响应体大小 (bytes) bytes_sent=$((RANDOM % 5000 + 100)) # 100到5100之间的随机数 # 4. 拼接成一条完整的 NGINX combined 格式日志 # 格式: $remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" log_line="$ip - - [$timestamp] \"$method $path HTTP/1.1\" $status $bytes_sent \"$referer\" \"$user_agent\"" # 5. 将日志行追加到文件中 # echo "$log_line" >> "$LOG_FILE" echo "$log_line" | sudo tee -a "$LOG_FILE" > /dev/null # 6. 等待5秒，进入下一次循环 sleep 5 done
授予执行权限：chmod +x generate_nginx_logs.sh。
在后台运行脚本：nohup ./generate_nginx_logs.sh &。
## 创建Project和LogStore
Project是日志服务的资源管理单元，用于隔离不同项目的数据；LogStore是日志数据的存储单元。
登录[日志服务控制台](https://sls.console.aliyun.com)。
单击创建Project：
所属地域：选择与ECS实例相同的地域，即可通过阿里云内网采集日志，加快日志采集速度。
Project名称：输入一个在阿里云内全局唯一的名称，例如nginx-quickstart-abc。
[其他配置](manage-a-project.md)保持默认，单击创建。
在Project创建成功页面，单击创建Logstore。
输入Logstore名称（例如nginx-access-log），[其他配置](manage-a-logstore.md)无需修改，单击确定。
默认情况下创建的是[标准型](manage-a-logstore.md)，[按写入数据量计费](billing-overview.md)的LogStore 。
## 安装LoongCollector
在创建LogStore成功的弹窗中，单击确定，打开快速数据接入面板。
单击Nginx - 文本日志卡片的立即接入。
机器组配置：
使用场景：主机场景
安装环境：ECS
单击创建机器组，在弹出面板中，选择目标ECS实例。
单击安装并创建为机器组，安装成功后，配置机器组名称（例如my-nginx-server），单击确定。
说明
如果安装失败或一直处于等待中，请检查ECS地域是否与Project相同。
单击下一步，检测机器组心跳状态。
首次新建机器组，如果心跳为FAIL，单击自动重试，等待两分钟左右心跳会变为OK。
## 创建采集配置
心跳状态为OK后，单击下一步，进入Logtail配置页面：
配置名称：填写配置名称，如：nginx-access-log-config。
文件路径：日志采集的路径，第一个输入框填写文件夹路径：/var/log/nginx，第二个输入框填写文件名access.log。
处理配置：
日志样例：单击添加日志样例，粘贴一行示例日志：
192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36"
处理模式：单击NGINX模式解析插件，在NGINX日志配置中配置log_format，复制并粘贴如下内容，单击确认。
log_format main '$remote_addr - $remote_user [$time_local] "$request" ' '$status $body_bytes_sent "$http_referer" ' '"$http_user_agent" $request_time $request_length';
生产环境中，此处的log_format必须与Nginx配置文件（通常位于 /etc/nginx/nginx.conf文件中）中的定义保持一致。
日志解析示例：
| 原始日志 | 结构化解析日志 |
| --- | --- |
| 192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36" | body_bytes_sent: 368 http_referer: - http_user_agent : Mozi11a/5.0 (Nindows NT 10.0; Win64; x64) AppleMebKit/537.36 (KHTML, like Gecko) Chrome/131.0.x.x Safari/537.36 remote_addr:192.168.*.* remote_user: - request_length: 514 request_method: GET request_time: 0.000 request_uri: /nginx-logo.png status: 200 time_local: 15/Apr/2025:16:40:00 |
单击下一步，进入查询分析配置页面，采集配置生效需要1分钟左右，单击自动刷新，出现预览数据，说明采集配置已生效。
## 查询与分析日志
单击下一步，进入结束页面。单击查询日志，系统将自动跳转到目标LogStore的查询分析页面，编写SQL分析语句，从结构化日志中提取关键业务与运维指标。指定时间范围为最近15分钟：
说明
如果出现错误弹窗，原因是索引还未配置完成，关闭后等待1分钟，即可查看access.log文件中的日志内容。
示例1：网站总访问量（PV）
统计指定时间范围内的日志总条数。
* | SELECT count(*) AS pv
示例2：按分钟统计请求量与错误率
计算每分钟的总请求数、错误请求数（HTTP状态码≥400）以及错误率。
* | SELECT date_trunc('minute', __time__) as time, count(1) as total_requests, count_if(status >= 400) as error_requests, round(count_if(status >= 400) * 100.0 / count(1), 2) as error_rate GROUP BY time ORDER BY time DESC LIMIT 100
示例3：统计不同请求方法（GET, POST等）的PV
按分钟和请求方法（GET/POST等）对访问量进行分组统计。
* | SELECT date_format(minute, '%m-%d %H:%i') AS time, request_method, pv FROM ( SELECT date_trunc('minute', __time__) AS minute, request_method, count(*) AS pv FROM log GROUP BY minute, request_method ) ORDER BY minute ASC LIMIT 10000
## 可视化数据仪表盘
配置Nginx解析插件后，日志服务会自动创建一个名为nginx-access-log_Nginx访问日志的预设仪表盘。
在左侧导航栏中，单击仪表盘>仪表盘列表。
找到并单击该仪表盘名称，查看包含PV、UV、错误率、请求方法分布等多个核心指标的可视化图表。
所有图表均可根据业务需求[自定义修改](dashboard.md)。
## 配置监控告警
配置一条告警规则，当服务出现异常（例如错误数激增）时，自动发送通知。
在左侧导航栏中，单击告警。
创建行动策略：
在通知策略>行动策略页签下，单击创建。
配置标识符和名称（例如send-notification-to-admin）。
在第一行动列表中，单击行动组。
选择渠道（例如短信），并配置接收人，选择内容模板。
单击确认。
创建告警规则：
切换到告警规则页签，单击新建告警。
规则名称：输入描述性名称，例如服务器5xx错误数过多。
查询统计：单击添加，配置查询条件。
日志库：选择已创建的nginx-access-log。
查询区间：15分钟（相对）。
查询：输入status >= 500 | SELECT *。
单击预览，确认可以查询到数据，单击确定。
触发条件：配置为当：有特定条数据>100条时，触发严重告警。
该配置表示15分钟内出现超过100个5xx错误时触发告警。
输出目标：选择SLS通知并开启。
行动策略：选择上一步创建的行动策略。
重复等待：设置为15分钟，避免过多的重复通知。
单击确定，保存告警规则。
验证：告警条件满足时，配置的通知渠道将收到告警信息。可在告警历史页面查看所有已触发的告警记录。
## 资源清理
为避免产生不必要的费用，完成操作后，务必按照以下步骤清理所有已创建的资源。
停止日志生成脚本
登录ECS实例，执行以下命令停止后台运行的日志生成脚本。
kill $(ps aux | grep '[g]enerate_nginx_logs.sh' | awk '{print $2}')
卸载LoongCollector（可选）
示例代码中${region_id}可使用cn-hangzhou替换，若想加快执行速度，请将${region_id}替换为ECS所属[地域](loongcollector-installation-linux.md)。
wget https://aliyun-observability-release-${region_id}.oss-${region_id}.aliyuncs.com/loongcollector/linux64/latest/loongcollector.sh -O loongcollector.sh;
执行卸载命令。
chmod +x loongcollector.sh; sudo ./loongcollector.sh uninstall;
删除Project。
在[日志服务控制台](https://sls.console.aliyun.com)Project列表页面，找到已创建的Project（例如nginx-quickstart-xxx）。
在右侧操作列单击删除。
在删除面板中，输入Project名称，选择删除原因。
单击确定，删除Project将同时删除其下的LogStore、采集配置、仪表盘、告警规则等所有关联资源。
警告
删除Project后，其管理的所有日志数据及配置信息都会被释放且不可恢复。删除前请慎重确认，避免数据丢失。
## 后续步骤
通过本教程，您已成功完成日志采集、查询分析、可视化仪表盘和告警配置的全流程操作。建议您继续阅读以下文档，深入理解核心概念，并结合业务需求合理规划日志资源体系：
理解[Project](manage-a-project.md)与[Store](manage-sls-store.md)概念。
熟悉[数据采集方式](data-collection-overview.md)，根据实际业务场景选择合适的采集方式。
了解[存储资源层级关系说明](resource-management-overview.md)并规划资源周期，合理分配Shard数量。
## 常见问题
### 采集日志后，显示时间与原始日志时间不一致怎么办？
默认情况下，日志服务的时间字段（__time__）使用的是日志到达服务器的时间。若要使用日志原文中的时间，需要在采集配置中添加[时间解析插件](time-parsing.md)。
### 仅创建Project和LogStore，会产生费用吗？
当您在创建LogStore时，日志服务默认预留Shard资源，因此可能产生活跃Shard租用费用。更多信息，请参见[为什么会产生活跃](why-am-i-charged-for-active-shards.md)[Shard](why-am-i-charged-for-active-shards.md)[租用费用？](why-am-i-charged-for-active-shards.md)
### 日志采集失败，如何排查？
使用Logtail采集日志失败，可能是因为Logtail心跳异常、采集错误、Logtail采集配置错误等原因。如何排查，请参见[Logtail](what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)[采集日志失败的排查思路](what-do-i-do-if-errors-occur-when-i-use-logtail-to-collect-logs.md)。
### 为什么可以查询到日志，但无法进行分析？
分析日志需要为相关字段配置字段索引并开启统计功能，请检查LogStore的[索引配置](create-indexes.md)。
### 如何停止日志服务计费？
日志服务开通后无法关闭，如果不再使用日志服务，可以删除账号下的所有Project即可[停止计费](stop-billing.md)。
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
