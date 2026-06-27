## 工作负载
Load：100%的String SET操作（写操作）。
Uniform-Read：采用Workload A，100%均匀随机String GET操作（读操作），主要测试严苛条件下的读性能。
Zipfian-Read：采用Workload C，数据分布方法为zipfian，测试大部分读请求访问小部分数据的性能，符合大部分的读场景。
Uniform-50%Read-50%Update：采用Workload A，50%的String SET操作（更新操作）与50%的String GET操作，主要测试随机更新的性能。
关于Workload的详细介绍，请参见[Core Workloads](https://github.com/brianfrankcooper/YCSB/wiki/Core-Workloads)。
