## 分析公网访问ECS的来源IP
假设已经创建了1台向公网开放的、监听80端口的Web服务器，并通过安全组限制了源IP访问。
那么可以通过创建流日志，来查询访问80端口的来源IP，并统计访问被安全组允许或拒绝的情况。
创建流日志
资源实例选择Web服务器的弹性网卡。
流量类型选择全部流量。
投递配置选择投递至日志服务并开启流日志分析报表功能。
其他选项保持默认。
分析流日志
查询分析语句
过滤访问10.0.0.1:80端口的源IP，并显示每个IP被安全组允许和拒绝的次数：
dstaddr:10.0.0.1 AND dstport:80 | SELECT -- 过滤目的IP是10.0.0.1，目的地端口是80的日志 srcaddr, SUM(CASE WHEN action = 'ACCEPT' THEN 1 ELSE 0 END) AS accept_count, -- 每当ACCEPT（即被允许）时计1 SUM(CASE WHEN action = 'REJECT' THEN 1 ELSE 0 END) AS reject_count -- 每当REJECT（即被拒绝）时计1 FROM log GROUP BY srcaddr -- 按源IP地址分组 ORDER BY accept_count + reject_count DESC -- 按照“安全组允许+拒绝”的总次数倒序排列
效果预览
srcaddr列显示访问80端口的源IP，accept_count和reject_count列分别统计每个源IP被安全组允许和拒绝的流日志条目数，即在查询时间内：
访问80端口来源IP有5个，分别为120.26.XX.XX、121.43.XX.XX、154.212.XX.XX、176.65.XX.XX、198.235.XX.XX。
来自120.26.XX.XX的请求全部被允许，其他公网IP的请求全部被拒绝。
