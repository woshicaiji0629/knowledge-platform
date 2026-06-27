try.cn-hangzhou.aliyuncs.com/log-service/docker-log-test:latest' env: # 配置环境变量 - name: aliyun_logs_log-varlog value: /var/log/*.log - name: aliyun_logs_mytag1_tags value: tag1=v1 # 配置volume mount volumeMounts: - name: volumn-sls-mydemo mountPath: /var/log # 如果Pod不断重启，启动参数可以添加sleep command: ["sh", "-c"] # 使用 shell 来运行命令 args: ["sleep 3600"] # 设置休眠时间为 1 小时（3600 秒） volumes: - name: volumn-sls-mydemo emptyDir: {}
通过环境变量来创建采集配置和自定义Tag，所有与配置相关的环境变量都采用aliyun_logs_作为前缀。
创建采集配置的规则如下：
- name: aliyun_logs_log-varlog value: /var/log/*.log
示例中创建了一个采集配置，格式为aliyun_logs_{key}，对应的{key}为log-varlog。
aliyun_logs_log-varlog：该env表示创建一个Logstore名为log-varlog，日志采集路径为/var/log/*.log的配置，对应的日志服务采集配置名称也是log-varlog，目的是将容器的/var/log/*.log文件内容采集到log-varlog这个Logstore中。
创建自定义Tag的规则如下：
- name: aliyun_logs_mytag1_tags value: tag1=v1
配置Tag后，当采集到该容器的日志时，会自动附加对应的字段到日志服务。其中mytag1为任意不包含'_'的名称。
如果采集配置中指定了非stdout的采集路径，需要在此部分创建相应的volumeMounts。
示例中采集配置添加了对/var/log/*.log的采集，因此相应地添加了/var/log的volumeMounts。
当YAML编写完成后，单击创建，即可将相应的配置交由Kubernetes集群执行。
配置环境变量的高级参数。
通过容器环境变量配置采集支持多种配置参数。您可以根据实际需求设置高级参数，以满足日志采集的特殊需求。
重要
通过容器环境变量配置采集日志的方式不适用于边缘场景。
