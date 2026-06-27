| 监控指标名称 | 监控指标含义 | 单位 | MetricName | Dimensions | Statistics |
| --- | --- | --- | --- | --- | --- |
| （ECS）CPU 使用率 | CPU 使用率 | % | CPUUtilization | userId、instanceId | Maximum、Minimum、Average |
| （ECS）经典网络公网流入带宽 | 公网入流量平均速率 | bit/s | InternetInRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）内网流入带宽 | 私网入流量平均速率 | bit/s | IntranetInRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）经典网络公网流出带宽 | 公网出流量平均速率 | bit/s | InternetOutRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）内网流出带宽 | 私网出流量平均速率 | bit/s | IntranetOutRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘读取 BPS | 系统磁盘每秒读取字节总数 | Byte/s | DiskReadBPS | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘写入 BPS | 系统磁盘每秒写入字节总数 | Byte/s | DiskWriteBPS | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘每秒读取次数 | 所有磁盘读 IOPS | 次/秒 | DiskReadIOPS | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘每秒写入次数 | 所有磁盘写 IOPS | 次/秒 | DiskWriteIOPS | userId、instanceId | Average、Minimum、Maximum |
| （ECS）IP 维度公网流入带宽 | 公网流入带宽 | bit/s | VPC_PublicIP_InternetInRate | userId、instanceId、ip | Maximum、Minimum、Average |
| （ECS）IP 维度公网流出带宽 | 公网流出带宽 | bit/s | VPC_PublicIP_InternetOutRate | us
