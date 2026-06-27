tes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,srcaddr,dstaddr -- 以时间、源ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
效果预览
查询结果的可视化配置方式与场景二类似，选择面积图类型，设置聚合列为srcaddr。
在ECS到NAT网关的这段路径上，10.0.0.1（ECS1）发送到公网IP地址120.26.XX.XX的流量速率最高，约12Kbps。
