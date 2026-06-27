### 启动参数设置
在安装Logtail的服务器上，打开/usr/local/ilogtail/ilogtail_config.json文件。
此步骤适用于主机环境。
在容器或Kubernetes环境下，您需要通过修改daemonset环境变量来修改Logtail启动参数。部分环境引用configmap，configmap路径为configmap>kube-system>alibaba-log-configuration
根据需求设置启动参数。
启动参数示例如下：
{ ... "cpu_usage_limit" : 0.4, "mem_usage_limit" : 384, "max_bytes_per_sec" : 20971520, "process_thread_count" : 1, "send_request_concurrency" : 15, "buffer_file_num" : 25, "buffer_file_size" : 20971520, "buffer_file_path" : "", ... }
说明
下表中只列出您需要关注的常用启动参数，未列出的启动参数，保持默认配置即可。
您可以根据需要新增或修改指定启动参数。
表 1. Logtail启动参数
