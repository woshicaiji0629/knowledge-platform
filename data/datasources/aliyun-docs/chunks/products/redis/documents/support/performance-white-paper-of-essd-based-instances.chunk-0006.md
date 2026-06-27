| 实例规格 | YCSB 配置 | 工作负载 | QPS（次/秒） | Average Latency（微秒） | 99th Percentile Latency（微秒） |
| --- | --- | --- | --- | --- | --- |
| tair.essd.standard.xlarge | recordcount=20000000 run_operationcount=20000000 threads=32 | Load | 36740 | 851 | 1595 |
| Uniform-Read | 103890 | 294 | 907 |  |  |
| Zipfian-Read | 106357 | 288 | 865 |  |  |
| Uniform-50%Read-50%Update | 46610 | Read：530 | Read：1108 |  |  |
| Update：795 | Update：1684 |  |  |  |  |
| tair.essd.standard.2xlarge | recordcount=40000000 run_operationcount=40000000 threads=50 | Load | 54670 | 911 | 1528 |
| Uniform-Read | 150796 | 314 | 995 |  |  |
| Zipfian-Read | 151110 | 314 | 977 |  |  |
| Uniform-50%Read-50%Update | 69137 | Read：537 | Read：948 |  |  |
| Update：878 | Update：1479 |  |  |  |  |
| air.essd.standard.4xlarge | recordcount=80000000 run_operationcount=80000000 threads=100 | Load | 90703 | 1099 | 1697 |
| Uniform-Read | 285833 | 339 | 1196 |  |  |
| Zipfian-Read | 288750 | 335 | 1162 |  |  |
| Uniform-50%Read-50%Update | 110316 | Read：757 | Read：1114 |  |  |
| Update：1041 | Update：1536 |  |  |  |  |
| tair.essd.standard.8xlarge | recordcount=160000000 run_operationcount=160000000 threads=120 | Load | 117581 | 1011 |
