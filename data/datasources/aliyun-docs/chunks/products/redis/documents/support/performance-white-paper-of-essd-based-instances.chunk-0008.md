| 实例规格 | YCSB 配置 | 工作负载 | QPS（次/秒） | Average Latency（微秒） | 99th Percentile Latency（微秒） |
| --- | --- | --- | --- | --- | --- |
| tair.essd.standard.xlarge | recordcount=640000000 run_operationcount=20000000 threads=32 | Load | 25561 | 1245 | 3497 |
| Uniform-Read | 25727 | 1239 | 2042 |  |  |
| Zipfian-Read | 47559 | 667 | 1217 |  |  |
| Uniform-50%Read-50%Update | 19731 | Read：1576 | Read：6383 |  |  |
| Update：1639 | Update：6487 |  |  |  |  |
| tair.essd.standard.2xlarge | recordcount=1280000000 run_operationcount=40000000 threads=50 | Load | 42287 | 1179 | 3465 |
| Uniform-Read | 35794 | 1394 | 1880 |  |  |
| Zipfian-Read | 77759 | 637 | 1219 |  |  |
| Uniform-50%Read-50%Update | 28656 | Read：1716 | Read：8863 |  |  |
| Update：1761 | Update：8951 |  |  |  |  |
| air.essd.standard.4xlarge | recordcount=2560000000 run_operationcount=80000000 threads=100 | Load | 65923 | 1514 | 6615 |
| Uniform-Read | 44753 | 2232 | 7903 |  |  |
| Zipfian-Read | 120337 | 826 | 1382 |  |  |
| Uniform-50%Read-50%Update | 38470 | Read：2577 | Read：8535 |  |  |
| Update：2617 | Update：8583 |  |  |  |  |
| tair.essd.standard.8xlarge | recordcount=5120000000 run_operationcount=160000000 threads=120 | Load | 8
