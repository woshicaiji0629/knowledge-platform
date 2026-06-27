### 内存大于数据场景

| 实例规格 | YCSB 配置 | 工作负载 | QPS（次/秒） | Average Latency（微秒） | 99th Percentile Latency（微秒） |
| --- | --- | --- | --- | --- | --- |
| tair.localssd.c1m4.2xlarge | recordcount=40000000 run_operationcount=40000000 threads=64 | Load | 59830 | 1066 | 2761 |
| Uniform-Read | 158221 | 389 | 891 |  |  |
| Zipfian-Read | 164233 | 379 | 873 |  |  |
| Uniform-50%Read-50%Update | 78099 | READ：651 | READ：2012 |  |  |
| UPDATE：974 | UPDATE：2731 |  |  |  |  |
| tair.localssd.c1m4.4xlarge | recordcount=80000000 run_operationcount=80000000 threads=128 | Load | 91991 | 1388 | 3077 |
| Uniform-Read | 302940 | 414 | 921 |  |  |
| Zipfian-Read | 305639 | 410 | 899 |  |  |
| Uniform-50%Read-50%Update | 124929 | READ：798 | READ：2231 |  |  |
| UPDATE：1234 | UPDATE：3013 |  |  |  |  |
| tair.localssd.c1m4.8xlarge | recordcount=160000000 run_operationcount=160000000 threads=256 | Load | 132865 | 1924 | 3323 |
| Uniform-Read | 489287 | 513 | 1313 |  |  |
| Zipfian-Read | 501847 | 499 | 1272 |  |  |
| Uniform-50%Read-50%Update | 187390 | READ：1069 | READ：2749 |  |  |
| UPDATE：1644 | UPDATE：3613 |  |  |  |  |
