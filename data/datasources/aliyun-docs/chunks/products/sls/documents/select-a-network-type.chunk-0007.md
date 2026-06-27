| send_request_concurrency | 15 | 20 | 40 | 80 |
| resources.limits.cpu | 500M | 1000M | 2000M | 4000M |
| resources.limits.memory | 2 Gi | 2 Gi | 3 Gi | 5 Gi |

容器或Kubernetes环境中的Logtail启动参数修改说明如下：
如果Logtail部署在阿里云Kubernetes集群中，且为Logtail-ds 1.7.3及以上版本，则推荐通过[容器服务管理控制台](https://cs.console.aliyun.com)修改，即在组件管理页面，修改logtail-ds组件中对应的各个参数。
如果Logtail部署在自建容器或Kubernetes环境中，且为Logtail-ds 1.7.3及以上版本，则需要通过修改daemonset环境变量来修改Logtail启动参数。部分环境引用configmap，configmap路径为configmap>kube-system>alibaba-log-configuration。
如果Logtail为Logtail-ds 1.7.3之前版本，则需要通过修改daemonset环境变量来修改Logtail启动参数。部分环境引用configmap，configmap路径为configmap>kube-system>alibaba-log-configuration。同时还需调整daemonset>kube-system>logtail-ds中的resources.limits.cpu和resources.limits.memory，避免Container资源超限。
按照上述表格中的采集速率大于40 MB/s列配置Logtail启动参数时，Logtail的采集性能接近极限，继续增加线程对性能提升效果不显著。采集端的性能极限说明如下表所示。
说明
因测试环境与生产环境不同，实际采集性能可能存在差异。

| 采集模式 | 性能极限 |
| --- | --- |
| 极简模式 | 440 MB/s |
| 完整正则模式 | 70 MB/s |
| 分隔符模式 | 75 MB/s |
| JSON 模式 | 75 MB/s |
