### 数据大于内存场景

| 实例规格 | YCSB 配置 | 工作负载 | QPS（次/秒） | Average Latency（微秒） | 99th Percentile Latency（微秒） |
| --- | --- | --- | --- | --- | --- |
| tair.localssd.c1m4.2xlarge | recordcount=1280000000 run_operationcount=1280000000 threads=64 | Load | 50396 | 1258 | 4463 |
| Uniform-Read | 74611 | 842 | 1745 |  |  |
| Zipfian-Read | 106366 | 588 | 1406 |  |  |
| Uniform-50%Read-50%Update | 47833 | READ：1232 | READ：4049 |  |  |
| WRITE：1402 | WRITE：4583 |  |  |  |  |
| tair.localssd.c1m4.4xlarge | recordcount=2560000000 run_operationcount=2560000000 threads=128 | Load | 81097 | 1573 | 4119 |
| Uniform-Read | 118141 | 1071 | 3085 |  |  |
| Zipfian-Read | 194704 | 634 | 1595 |  |  |
| Uniform-50%Read-50%Update | 75625 | READ：1562 | READ：4999 |  |  |
| UPDATE：1795 | UPDATE：5419 |  |  |  |  |
| tair.localssd.c1m4.8xlarge | recordcount=5120000000 run_operationcount=5120000000 threads=256 | Load | 115660 | 2210 | 5235 |
| Uniform-Read | 202365 | 1252 | 3985 |  |  |
| Zipfian-Read | 309019 | 804 | 2551 |  |  |
| Uniform-50%Read-50%Update | 122318 | READ：1861 | READ：5603 |  |  |
| UPDATE：2307 | UPDATE：6415 |  |  |  |  |
