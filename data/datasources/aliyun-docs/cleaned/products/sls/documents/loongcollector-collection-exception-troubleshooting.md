# LoongCollector采集异常问题汇总排查-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/loongcollector-collection-exception-troubleshooting

# LoongCollector采集异常问题汇总排查
在使用LoongCollector进行数据采集时，可能会遇到采集异常问题。本文将介绍排查采集异常问题的流程，以及一些常见场景下的处理示例。
## 采集异常问题排查指引
采集异常问题的成因复杂多样，且不同原因可能导致相同表象，甚至有时异常无法及时发现。因此需要如下指引，以实现异常的及时识别、排查与分类诊断。
登录[日志服务控制台](https://sls.console.aliyun.com/)，在日志应用区域单击SLS数据洞察。在接入管理的SLS采集规则列表页签中，按照对话框提示开启功能。
[CloudLens for SLS](cloudlens-for-sls.md)帮助监控与管理日志服务资源，提高问题定位的效率，及时感知与响应多维度指标的异常。
回到Project列表中，单击目标Project。
单击日志存储，在日志库中，将鼠标悬浮于目标LogStore上，随后单击右侧的图标，单击基础版诊断查看异常诊断信息。
高级版诊断提供异常诊断仪表盘，并支持更长时间的异常信息查询。详情可参考[运行情况诊断与监控](automatic-diagnosis-and-monitoring-of-loongcollector-operation.md)。
根据诊断显示的错误类型查阅[采集常见错误类型](loongcollector-collection-exception-troubleshooting.md)，排查错误原因。或在 /usr/local/ilogtail/目录下的ilogtail.LOG与logtail_plugin.LOG中查看客户端日志详情。
## 常见采集异常场景
### 机器组心跳FAIL
请参考[心跳异常问题汇总排查](troubleshooting-of-abnormal-heartbeat-problems.md)。
### 日志未采集
采集日志时若查询页面无数据，可能原因如下：
在控制台日志库的消费预览中查看，是否采集到日志，若采集到日志但查询无数据，一般由于未[创建索引](create-indexes.md)。
无新增日志：待采集日志文件无更新，则不会采集。
机器组心跳异常：[心跳异常问题汇总排查](troubleshooting-of-abnormal-heartbeat-problems.md)。
无采集配置：采集配置需创建并应用到机器组，然后才能下发到服务器生效，详情参考[机器组与采集配置关联指南](machine-group-and-collection-configuration-association-guide.md)。
采集配置路径错误：检查采集配置中待采集日志文件路径是否正确。
容器场景下还可以开启元容器信息预览查看采集匹配的容器情况。
如果是容器采集场景还需注意：
路径是否有挂载和软链接：不支持软链接，挂载优先级：EmptyDir > hostpath > NAS(不推荐)。更多请参考[日志源与挂载点要求（重要）](kubernetes-cluster-container-log-collection-instructions.md)。
EmptyDir挂载：性能最优，可登录容器查看看日志；hostpath挂载：可登录主机和容器查看日志，容器奔溃日志仍保留；NAS挂载：不推荐，采集NAS文件性能极低且易采集失败，且查询只能简单grep。
采集配置的label和env与容器是否一致：注意docker label需要进宿主机 docker inspect 容器id 查询。
发生采集错误：若上述检查通过，则在[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)。
### 数据重复采集
内存使用率极高，一直在崩溃。崩溃会重新从checkpoint检查点采集导致数据重复，请[修改](loongcollector-management-linux.md)[CPU](loongcollector-management-linux.md)[使用上限或网络发送并发限制](loongcollector-management-linux.md)。
文件用编辑器编辑过（如使用vim编辑保存）：查看文件创建时间，确认被采集文件是否发生重写。
#方法一：看birth time stat your_file #方法二：有时候方法一不管用，看crtime stat -c %i your_file df . #查询分区 sudo debugfs -R 'stat <3014895>' /dev/sda3 #替换<>中间的inode（<>要保留），替换sda3为上一行命令分区所在dev
检查是否存在多个采集器实例。
日志量极小的情况下（15分钟以上无新日志）：采集进度可能被清理，造成重复采集。
检查是否采集配置重复：stdout由于允许重复采集，尤其需要注意。
[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)：存在MULTI_CONFIG_MATCH_ALARM错误。
删除多余采集配置：重复采集配置采集同一个目录时，采集路径最精确的优先级最高。
修改相关配置：[实现一个文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
采集日志路径总会在多个路径变化，删除采集配置会立刻重建：
排查目录是否存在软连接导致重复采集。
排查是否由env创建或ack中配置了日志标签，配置了需要删掉。
Pod容器重启，且使用hostpath挂载，导致重复采集。
采集容器日志的原理是通过类似docker ps的方法探测容器，通过类似docker inspect的方法找到采集路径。当匹配采集配置时，采集器会向主程序报送一条采集路径+配置。当容器重启时，采集器会认为是创建新容器，并再次向主程序报送一条采集路径+配置。此时，由于业务pod日志路径挂载的是hostPath，因此前一个容器持久化的日志会被保留下来，采集器默认往回读取1M日志导致日志重复。
容器内日志发生采集重复，并且采集路径含NAS。
如果创建reader的时间点因为（NAS）目录注册慢没有赶上dump checkpoint的时间点，那么进度都会丢失。add a new watcher持续时间过长也是一个特征，解决方法是把check_point_dump_interval修改为600。
### 采集时间延迟
采集时间延迟有几类情况：
几秒内的延迟是在预期范围内的，若介意可以配置[时间插件](extract-log-time.md)。
若有大量数据延迟，检查是否有重启现象。重启后会向前采集，产生延时采集的现象。查看最新数据是否实时，若最新数据实时就没问题。
只延时一行，检查日志文件的最后一行是否没有回车。
某台机器出现延时，可能是该机器采集器启动较晚，可以通过/usr/local/ilogtail/app_info.json的时间确认，或/usr/local/ilogtail/ilogtail.LOG中是否存在“network error”网络原因导致延时。
若不符合上述场景，则在[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)或[使用](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[CloudLens for SLS](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[分析](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[LoongCollector](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)[日志采集延迟问题](use-cloudlens-for-sls-to-analyze-loongcollector-log-collection-latency.md)。
### 采集丢失
是否pod生命周期过短（<20s），建议日志打到hostPath进行采集。
查看配置env 和 label 是否和容器一致。
检查是否是采集延时导致的数据不全。
如果是标准输出日志非常长（>16K）发生截断并且是ACK、ASK、SAE场景，需要通过文件采集。
采集器重启也会导致采集数据不全。查看/usr/local/ilogtail/app_info.json的update_time确认是否重启。
主动重启：因资源达到配置上限而cuicide，特征是采集器守护进程和工作进程的启动时间有差异，请[修改](loongcollector-management-linux.md)[CPU](loongcollector-management-linux.md)[使用上限或网络发送并发限制](loongcollector-management-linux.md)。
被动重启：因资源达到container配置上限而被k8s杀死或者达到cgroup上限而被kernel杀死，特点是pod的重启次数超过一次。请查看是否OOM被杀，并调整[修改](loongcollector-management-linux.md)[CPU](loongcollector-management-linux.md)[使用上限或网络发送并发限制](loongcollector-management-linux.md)。
注意：当需要调整资源参数时，往往意味着日志量很大，需要注意[Shard](manage-shards.md)[数量](manage-shards.md)与[资源配额](manage-a-project.md)是否充足。
如果采集数据不一致发生在实例之间，需要注意是否是采集器版本不同导致。可参考[配置管理](loongcollector-management-linux.md)查看版本与升级。
不定时的丢数据，重启后过一段时间会复现：
根据[CloudLens for SLS](cloudlens-for-sls.md)检查当前LogStore配置是否超限。
查看/usr/local/ilogtail/目录下ilogtail.LOG和logtail_plugin.LOG，寻找报错进行具体排查。
若不符合上述场景，则在[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)。
### 日志格式错误
采集格式不符合预期，检查采集配置信息,参考[持续采集主机文本日志](host-text-log-collection-auto-install.md)使用完整正则模式和插件模式提取字段。
json字段无法被解析提取：通过解析工具验证日志内容是否严格符合json object，插件不支持非json objet的解析，可以尝试修改原始字段格式来规避。
一整条日志是一个整体：可能是未设置分词符导致的，建议[了解索引内容按需配置](quick-guide-to-query-and-analysis.md)。
## 常见问题
### 日志正常采集中突发异常
日志可以正常采集说明配置项大概率正确，若没有修改内容或新增相关采集配置时，可优先关注是否需要调整采集性能与提升配额。
尝试调整采集性能：[修改](loongcollector-management-linux.md)[CPU、内存使用上限。](loongcollector-management-linux.md)
借助[CloudLens for SLS](cloudlens-for-sls.md)监控：在数据洞察中查看配额使用情况，如project写入流量是否超过限额。在采集监控-文件采集监控-采集文件分布中查看是否有延迟的文件。可能当前读取速率跟不上日志的产生速率，CPU usage 满了, 读不完日志导致日志文件一直保持打开状态目录空间没法释放。
### 日志时间问题
__time__是日志采集的时间，使用sdk写入日志时可指定。
tag中的receive_time是日志服务接受到日志的时间。
日志里的 time 字段，仅仅是一个普通字段。
例如使用sdk在1月2号写入一条日志，指定日期为 1月1号（这个时间可以根据time来设置，也可以自行设置），则查询时receive time 是 1月2号，__time__是1月1号。只有receive time是真正写日志的时间，至于 __time__和日志中的 time字段，都是由自己设置的。
日志上报的时间，有时区问题吗（不同时区，同一时刻 ，本地时间不同） ：时间与时区无关，是一个Unix时间戳。自UTC 1970年1月1号开始计数经过的秒数（或者毫秒数）。 比如对于UNIX timestamp 1620994708，相当于：GMT 时间：Fri May 14 2021 12:18:28 GMT+0000。
### 日志乱码问题
日志服务默认UTF8，需要修改原始日志编码格式为UTF8。
## 附录
### 采集常见错误类型
| 错误码 | 错误说明 | 解决方法 |
| --- | --- | --- |
| LOG_GROUP_WAIT_TOO_LONG_ALARM | 数据包从产生到发送的过程中等待的时间较长。 | 检查发送是否正常，或是否存在数据量超过默认配置、配额不足或网络存在问题。 |
| LOGFILE_PERMINSSION_ALARM | 无权限读取指定文件。 | 检查服务器 LoongCollector 的启动账号，建议以 root 方式启动。 |
| SPLIT_LOG_FAIL_ALARM | 行首正则与日志行首匹配失败，无法对日志做分行。 | 检查行首正则正确性。 若是单行日志可以配置为 .* 。 |
| MULTI_CONFIG_MATCH_ALARM | 默认情况下，一个文件只能匹配一个配置。当多个配置匹配同一个文件时，只会生效一个。 Docker 标准输出可以被多个配置采集。 | 删除多余的采集配置。 修改相关配置， [实现一个文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md) 。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [iLogtail](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [文件重复配置问题](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| REGEX_MATCH_ALARM | 完整正则模式下，日志内容和正则表达式不匹配。 | 复制错误信息中的日志样例重新匹配，并生成新的正则表达式。 |
| PARSE_LOG_FAIL_ALARM | JSON、分隔符等模式下，由于日志格式不符合定义而解析失败。 | 单击错误信息，查看失败的详细报错。 |
| CATEGORY_CONFIG_ALARM | 采集配置不合法。 | 常见的错误为正则表达式提取文件路径作为 Topic 失败。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [iLogtail](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [采集配置错误问题](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| LOGTAIL_CRASH_ALARM | 因超过服务器资源使用上限而崩溃。 | [修改](loongcollector-management-linux.md) [CPU、内存使用上限。](loongcollector-management-linux.md) |
| REGISTER_INOTIFY_FAIL_ALARM | 在 Linux 系统中注册日志监听失败，可能由于没有文件夹权限或文件夹被删除。 | 检查采集器是否有权限访问该文件夹，或者该文件夹是否被删除。 |
| DISCARD_DATA_ALARM | 配置使用的 CPU 资源不够或网络发送流控导致数据丢失 | [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| SEND_DATA_FAIL_ALARM | 发送数据失败，可能原因： 阿里云账号未创建 AccessKey。 客户端所在机器与日志服务无法连通或者网络链路质量较差。 日志服务端写入配额不足。 | 使用阿里云账号创建 AccessKey。 检查本地配置文件 /usr/local/ilogtail/ilogtail_config.json ，执行 curl <服务器地址> ，查看是否有内容返回。 为 LogStore [增加](manage-shards.md) [Shard](manage-shards.md) [数量](manage-shards.md) ，以支持更大数据量的写入。 |
| SEND_QUOTA_EXCEED_ALARM | 日志写入流量超出限制。 | 在控制台上 [增加](manage-shards.md) [Shard](manage-shards.md) [数量](manage-shards.md) 。 |
| READ_LOG_DELAY_ALARM | 日志采集进度落后于日志产生进度，一般是由于配置使用的 CPU 资源不够或是网络发送流控导致。 | [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 导入历史数据时，短时间会采集大量数据，若出现该错误可忽略。 |
| DROP_LOG_ALARM | 开始丢弃日志：日志采集进度落后于日志产生进度，且未处理的日志轮转超过 20 个，一般是由于配置使用的 CPU 资源不够或是网络发送流控导致。 | [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| LOGDIR_PERMINSSION_ALARM | 没有日志监控目录读取权限。 | 检查日志监控目录是否存在。如果存在，请检查目录权限设置。 |
| ENCODING_CONVERT_ALARM | 编码转换失败。 | 检查日志编码格式配置是否与日志编码格式一致。 |
| OUTDATED_LOG_ALARM | 过期的日志：日志时间落后 12 小时以上。可能原因： 日志解析进度落后 12 小时以上。 用户自定义时间字段配置错误。 日志记录程序时间输出异常。 | 查看是否存在 READ_LOG_DELAY_ALARM。 若存在参考 READ_LOG_DELAY_ALARM 处理方式解决。 若不存在则检查时间字段配置。如果时间字段配置正确，请检查日志记录程序时间输出是否正常。 |
| STAT_LIMIT_ALARM | 日志采集配置目录中的文件数超限。 | 检查采集的目录下是否有较多文件和子目录并合理设置监控目录最大深度。 修改 [启动参数配置文件（ilogtail_config.json）](loongcollector-management-linux.md) 中 mem_usage_limit 参数。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查文件、目录数超限问题](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| DROP_DATA_ALARM | 进程退出时日志落盘到本地超时，此时会丢弃未落盘完成的日志。 | 该报错通常为采集严重阻塞导致，请 [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| INPUT_COLLECT_ALARM | 输入源采集异常。 | 根据错误提示处理。 |
| HTTP_LOAD_ADDRESS_ALARM | HTTP 数据采集配置中，设置的 Addresses 不合法。 | 检查 Addresses 合法性。 |
| HTTP_COLLECT_ALARM | HTTP 数据采集异常。 | 根据错误提示排查，一般超时导致。 |
| FILTER_INIT_ALARM | 过滤器初始化异常。 | 一般由于过滤器的正则表达式非法导致，请根据提示修复。 |
| INPUT_CANAL_ALARM | MySQL Binlog 运行异常。 | 根据错误提示排查。在配置更新时，canal 服务可能重启，服务重启的错误可以忽略。 |
| CANAL_INVALID_ALARM | MySQL Binlog 内部状态异常。 | 此错误一般由于运行时表的 schema 信息变更导致 meta 不一致。请确认报错期间是否修改过表的 schema。 |
| MYSQL_INIT_ALARM | MySQL 初始化异常。 | 根据错误提示处理。 |
| MYSQL_CHECKPOING_ALARM | MySQL Checkpoint 格式异常。 | 确认是否修改 Checkpoint 相关配置。 |
| MYSQL_TIMEOUT_ALARM | MySQL 查询超时。 | 确认 MySQL 服务器和网络是否异常。 |
| MYSQL_PARSE_ALARM | MySQL 查询结果解析失败。 | 确认 MySQL 配置的 Checkpoint 格式是否匹配对应字段的格式。 |
| AGGREGATOR_ADD_ALARM | 向聚合队列中添加数据失败。 | 数据发送过快。若真实数据量很大，可忽略。 |
| ANCHOR_FIND_ALARM | processor_anchor 插件错误、配置错误或存在不符合配置的日志。 | 查看详细报错，根据内容分为如下类型。检查相应的配置是否存在问题。 anchor cannot find key ：配置中指定了 SourceKey 但日志中不存在对应的字段。 anchor no start ：无法从 SourceKey 的值中找到 Start 对应的内容。 anchor no stop ：无法从 SourceKey 的值中找到 Stop 对应的内容。 |
| ANCHOR_JSON_ALARM | processor_anchor 插件错误：对已配置的 Start 和 Stop 所确定的内容执行 JSON 展开时发生错误。 | 查看详细报错，检查所处理的内容以及相关的配置，确定是否有配置错误或不合法日志。 |
| CANAL_RUNTIME_ALARM | MySQL Binlog 插件运行时错误。 | 查看详细报错进一步排查。一般与所连接的 MySQL master 相关。 |
| CHECKPOINT_INVALID_ALARM | Checkpoint 解析失败。 | 查看详细报错，根据其中检查点内容（前 1024 个字节）以及具体错误信息进一步排查。 |
| DIR_EXCEED_LIMIT_ALARM | 同时监听的目录数超出限制。 | 检查当前 LogStore 的采集配置是否包含较多的目录数，合理设置监控目录最大深度。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查文件、目录数超限问题](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| DOCKER_FILE_MAPPING_ALARM | 执行命令添加 Docker 文件映射失败。 | 查看详细报错，根据具体错误信息进一步排查。 |
| DOCKER_FILE_MATCH_ALARM | 无法在 Docker 容器中查找到指定文件。 | 查看详细报错，根据其中的容器信息以及查找的文件路径进一步排查。 |
| DOCKER_REGEX_COMPILE_ALARM | service_docker_stdout 插件错误，根据配置中的 BeginLineRegex 编译失败。 | 查看详细报错，检查其中的正则表达式是否正确。 |
| DOCKER_STDOUT_INIT_ALARM | service_docker_stdout 插件初始化失败。 | 查看详细报错，报错根据内容分为如下类型。 host...version...error ：检查配置中指定的 Docker Engine 是否可访问。 load checkpoint error ：加载检查点失败，如无影响可忽略此错误。 container... ：指定容器存在非法 Label 值，目前仅允许配置 stdout 和 stderr。请结合详细错误进行检查。 |
| DOCKER_STDOUT_START_ALARM | service_docker_stdout 插件采集时，stdout 大小超过限制。 | 一般因为首次采集时 stdout 已存在，可忽略。 |
| DOCKER_STDOUT_STAT_ALARM | service_docker_stdout 插件无法检测到 stdout。 | 一般因为容器退出时无法访问到 stdout，可忽略。 |
| FILE_READER_EXCEED_ALARM | 同时打开的文件对象数量超过限制。 | 一般因为当前处于采集状态的文件数过多，请检查采集配置是否合理。 |
| GEOIP_ALARM | processor_geoip 插件错误。 | 查看详细报错，报错根据内容分为如下类型。 invalid ip... ：获取 IP 地址失败，请检查配置中的 SourceKey 是否正确或是否存在不合法日志。 parse ip... ：根据 IP 地址解析城市失败，请查看详细错误信息进行排查。 cannot find key... ：无法从日志中查看到指定的 SourceKey ，请检查配置是否正确或是否存在不合法日志。 |
| HTTP_INIT_ALARM | metric_http 插件错误，配置中指定的 ResponseStringMatch 正则表达式编译错误。 | 查看详细报错，检查其中的正则表达式是否正确。 |
| HTTP_PARSE_ALARM | metric_http 插件错误，获取 HTTP 响应失败。 | 查看详细报错，根据其中的具体错误信息对配置内容或所请求的 HTTP 服务器进行检查。 |
| INIT_CHECKPOINT_ALARM | Binlog 插件错误，加载检查点失败，插件将忽略检查点并从头开始处理。 | 查看详细报错，根据其中的具体错误信息来确定是否可忽略此错误。 |
| LOAD_LOCAL_EVENT_ALARM | 执行了本地事件处理错误 | 此警告一般不会出现，查看详细报错，根据其中的文件名、配置名、project、LogStore 等信息进行进一步地排查。 |
| LOG_REGEX_FIND_ALARM | processor_split_log_regex 以及 processor_split_log_string 插件错误，无法从日志中获取到配置中指定的 SplitKey 。 | 查看详细报错，检查是否存在配置错误的情况。 |
| LUMBER_CONNECTION_ALARM | service_lumberjack 插件错误，停止插件时关闭服务器错误。 | 查看详细报错，根据具体错误信息进一步排查，此错误一般可忽略。 |
| LUMBER_LISTEN_ALARM | service_lumberjack 插件错误，初始化进行监听时发生错误。 | 查看详细报错，报错根据内容分为如下类型。 init tls error... ：请结合具体的错误信息检查 TLS 相关的配置是否正确 listen init error... ：请结合具体的错误信息检查地址相关的配置是否正确。 |
| LZ4_COMPRESS_FAIL_ALARM | 执行 LZ4 压缩发生错误。 | 查看详细报错，根据其中的 log lines、project、category、region 等值来进行进一步排查。 |
| MYSQL_CHECKPOINT_ALARM | MySQL 插件错误，检查点相关错误。 | 查看详细报错，报错根据内容分为如下类型。 init checkpoint error... ：初始化检查点失败，请根据错误信息检查配置指定的检查点列以及所获取的值是否正确。 not matched checkpoint... ：检查点信息不匹配，请根据错误信息检查是否是由于配置更新等人为原因导致的错误，如果是则可忽略。 |
| NGINX_STATUS_COLLECT_ALARM | nginx_status 插件错误，获取状态发生错误。 | 查看详细报错，根据其中的 URL 以及具体的错误信息来进行进一步排查。 |
| NGINX_STATUS_INIT_ALARM | nginx_status 插件错误，初始化解析配置中指定的 URL 失败。 | 查看详细报错，根据其中的 URL 检查地址是否正确配置。 |
| OPEN_FILE_LIMIT_ALARM | 已打开文件数量超过限制，无法打开新的文件 | 查看详细报错，根据其中的日志文件路径、Project、LogStore 等信息进行进一步排查。 |
| OPEN_LOGFILE_FAIL_ALARM | 打开文件出错。 | 查看详细报错，根据其中的日志文件路径、Project、LogStore 等信息进行进一步排查。 |
| PARSE_DOCKER_LINE_ALARM | service_docker_stdout 插件错误，解析日志失败。 | 查看详细报错，报错根据内容分为如下类型。 parse docker line error: empty line ：日志为空。 parse json docker line error... ：以 JSON 格式解析日志失败，请根据错误信息以及日志的前 512 个字节进行排查。 parse cri docker line error... ：以 CRI 格式解析日志失败，请根据错误信息以及日志的前 512 个字节进行排查。 |
| PLUGIN_ALARM | 插件初始化及相关调用发生错误。 | 查看详细报错，报错根据内容分为如下类型，请根据具体的错误信息进行进一步排查。 init plugin error... ：初始化插件失败。 hold on error... ：暂停插件运行失败。 resume error... ：恢复插件运行失败。 start service error... ：启动 service input 类型的插件失败。 stop service error... ：停止 service input 类型的插件失败。 |
| PROCESSOR_INIT_ALARM | processor_regex 插件错误，编译配置中指定的 Regex 正则表达式失败。 | 查看详细报错，检查其中的正则表达式是否正确。 |
| PROCESS_TOO_SLOW_ALARM | 日志解析速度过慢。 | 查看详细报错，根据其中的日志数量、缓冲区大小、解析时间来确定是否正常。 如果不正常，检查是否有其他进程占用了过多的 CPU 资源或是存在效率较低的复杂正则表达式等不合理的解析配置。 |
| REDIS_PARSE_ADDRESS_ALARM | redis 插件错误，配置中提供的 ServerUrls 存在解析失败的情况。 | 查看详细报错，对其中报错的 URL 进行检查。 |
| REGEX_FIND_ALARM | processor_regex 插件错误，无法从日志中找到配置中 SourceKey 指定的字段。 | 查看详细报错，检查是否存在 SourceKey 配置错误或日志不合法的情况。 |
| REGEX_UNMATCHED_ALARM | processor_regex 插件错误，匹配失败。 | 查看详细报错，报错根据内容分为如下类型，请根据具体的错误信息进行排查。 unmatch this log content... ：日志无法匹配配置中的正则表达式 match result count less... ：匹配的结果数量少于配置中指定的 Keys 数量。 |
| SAME_CONFIG_ALARM | 同一个 LogStore 下存在同名的配置，后发现的配置会被抛弃。 | 查看详细报错，根据其中的配置路径等信息排查是否存在配置错误的情况。 |
| SPLIT_FIND_ALARM | split_char 以及 split_string 插件错误，无法从日志中找到配置中 SourceKey 指定的字段。 | 查看详细报错，检查是否存在 SourceKey 配置错误或日志不合法的情况。 |
| SPLIT_LOG_ALARM | processor_split_char 以及 processor_split_string 插件错误，解析得到的字段数量与 SplitKeys 中指定的不相同。 | 查看详细报错，检查是否存在 SourceKey 配置错误或日志不合法的情况。 |
| STAT_FILE_ALARM | 通过 LogFileReader 对象进行文件采集时发生错误。 | 查看详细报错，根据其中的文件路径、错误信息进行进一步排查。 |
| SERVICE_SYSLOG_INIT_ALARM | service_syslog 插件错误，初始化失败。 | 查看详细报错，检查配置中的 Address 是否正确。 |
| SERVICE_SYSLOG_STREAM_ALARM | service_syslog 插件错误，通过 TCP 采集时发生错误。 | 查看详细报错，报错根据内容分为如下类型，请根据详细报错中的具体错误信息进行排查。 accept error... ：执行 Accept 时发生错误，插件将等待一段时间后重试。 setKeepAlive error... ：设置 Keep Alive 失败，插件将跳过此错误并继续运行。 connection i/o timeout... ：通过 TCP 读取时超时，插件将重设超时并继续读取。 scan error... ：TCP 读取错误，插件将等待一段时间后重试。 |
| SERVICE_SYSLOG_PACKET_ALARM | service_syslog 插件错误，通过 UDP 采集时发生错误。 | 查看详细报错，报错根据内容分为如下类型。 connection i/o timeout... ：通过 UDP 读取时超时，插件将重设超时并继续读取。 read from error... ：UDP 读取错误，插件将等待一段时间后重试。 |
| PARSE_TIME_FAIL_ALARM | 解析日志时间失败。 | 正则表达式提取的时间字段是否正确。 指定的时间字段内容是否匹配配置中的时间表达式。 详细的解决方案： [使用](https://developer.aliyun.com/article/1488856) [CloudLens](https://developer.aliyun.com/article/1488856) [排查日志时间解析错误问题](https://developer.aliyun.com/article/1488856) 。 |
| BINARY_UPDATE_ALARM | 二进制数据更新警告。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CAST_SENSITIVE_WORD_ALARM | 敏感词类型转换相关错误。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CHECKPOINT_ALARM | checkpoint 相关错误。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CHECKPOINT_V2_ALARM | （CheckpointManagerV2 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| COMPRESS_FAIL_ALARM | 压缩失败，失败后会直接丢弃。 | 查看详细报错，根据具体错误信息进一步排查。 |
| CONFIG_UPDATE_ALARM | 配置拉取/重启错误。 | 查看详细报错，根据具体错误信息进一步排查。 |
| DISCARD_SECONDARY_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| DOMAIN_SOCKET_BIND_ALARM | （ShennongManager 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| ENCRYPT_DECRYPT_FAIL_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| EPOLL_ERROR_ALARM | faild to init inotify fd | 查看详细报错，根据具体错误信息进一步排查。 |
| EXACTLY_ONCE_ALARM | drop exactly once log group because of invalid sequence ID | 查看详细报错，根据具体错误信息进一步排查。 |
| FUSE_FILE_TRUNCATE_ALARM | 非常规 FUSE 文件截断行为警告。 | 查看详细报错，根据具体错误信息进一步排查。 |
| GLOBAL_CONFIG_ALARM | （EnterpriseConfigProvider 专用）remove useless configs | 查看详细报错，根据具体错误信息进一步排查。 |
| HOLD_ON_TOO_SLOW_ALARM | 停止模块过慢。 | 查看详细报错，根据具体错误信息进一步排查。 |
| INNER_PROFILE_ALARM | file dev inode changed, create new reader | 查看详细报错，根据具体错误信息进一步排查。 |
| INOTIFY_DIR_NUM_LIMIT_ALARM | inotify 监听超限。 | 查看详细报错，根据具体错误信息进一步排查。 |
| INOTIFY_EVENT_OVERFLOW_ALARM | inotify event queue overflow | 查看详细报错，根据具体错误信息进一步排查。 |
| INVALID_CONTAINER_PATH_ALARM | failed to set container base dir: container log path not existed | 查看详细报错，根据具体错误信息进一步排查。 |
| INVALID_MEMORY_ACCESS_ALARM | PropagateTimeout access invalid key of mPathWdMap | 查看详细报错，根据具体错误信息进一步排查。 |
| LOG_GROUP_PARSE_FAIL_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| LOG_TRUNCATE_ALARM | signature is same but size decrease, read from now fileSize | 查看详细报错，根据具体错误信息进一步排查。 |
| LOGDIR_PERMISSION_ALARM | 打开目录失败。 | 查看详细报错，根据具体错误信息进一步排查。 |
| LOGTAIL_CONFIG_ALARM | ilogtail_config.json 不存在或解析失败。 | 查看详细报错，根据具体错误信息进一步排查。 |
| LOGTAIL_CRASH_STACK_ALARM | last logtail crash stack | 查看详细报错，根据具体错误信息进一步排查。 |
| METRIC_GROUP_PARSE_FAIL_ALARM | （ShennongManager 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| MODIFY_FILE_EXCEED_ALARM | modify cache is up limit | 查看详细报错，根据具体错误信息进一步排查。 |
| PROCESS_QUEUE_BUSY_ALARM | logprocess queue is full, put modify event to event queue again | 查看详细报错，根据具体错误信息进一步排查。 |
| READ_STOPPED_CONTAINER_ALARM | 容器停止。 | 查看详细报错，根据具体错误信息进一步排查。 |
| REGISTER_HANDLERS_TOO_SLOW_ALARM | Registering handlers 耗时过长。 | 查看详细报错，根据具体错误信息进一步排查。 |
| RELABEL_METRIC_FAIL_ALARM | 指标重标记失败。 | 查看详细报错，根据具体错误信息进一步排查。 |
| SECONDARY_READ_WRITE_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| SEND_COMPRESS_FAIL_ALARM | （DiskBufferWriter 专用） | 查看详细报错，根据具体错误信息进一步排查。 |
| SENDING_COSTS_TOO_MUCH_TIME_ALARM | 发送时间过长。 | 查看详细报错，根据具体错误信息进一步排查。 |
| SERIALIZE_FAIL_ALARM | 序列化失败。 | 查看详细报错，根据具体错误信息进一步排查。 |
| SKIP_READ_LOG_ALARM | 跳过日志读取警告。 | 查看详细报错，根据具体错误信息进一步排查。 |
| STREAMLOG_TCP_SOCKET_BIND_ALARM | TCP 端口绑定冲突警告。 | 查看详细报错，根据具体错误信息进一步排查。 |
| TOO_MANY_CONFIG_ALARM | 本地目录下配置过多 | 查看详细报错，根据具体错误信息进一步排查。 |
| UNEXPECTED_FILE_TYPE_MODE_ALARM | found unexpected type mode | 查看详细报错，根据具体错误信息进一步排查。 |
| USER_CONFIG_ALARM | （LegacyConfigProvider 专用）本地配置非法 | 查看详细报错，根据具体错误信息进一步排查。 |
| WINDOWS_WORKER_START_HINTS_ALARM | windows 工作节点启动检测告警。 | 查看详细报错，根据具体错误信息进一步排查。 |
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
