abels: app: deployment-stdout cluster_label: CLUSTER-LABEL-A spec: containers: - args: - >- while true; do date '+%Y-%m-%d %H:%M:%S'; echo 1; echo 2; echo 3; echo 4; echo 5; echo 6; echo 7; echo 8; echo 9; sleep 10; done command: - /bin/sh - '-c' - '--' env: - name: cluster_id value: CLUSTER-A - name: aliyun_logs_log-stdout value: stdout image: 'mirrors-ssl.aliyuncs.com/busybox:latest' imagePullPolicy: IfNotPresent name: timestamp-test resources: {} terminationMessagePath: /dev/termination-log terminationMessagePolicy: File dnsPolicy: ClusterFirst restartPolicy: Always schedulerName: default-scheduler securityContext: {} terminationGracePeriodSeconds: 30
通过环境变量来创建您的采集配置和自定义Tag，所有与配置相关的环境变量都采用aliyun_logs_作为前缀。
创建采集配置的规则如下：
- name: aliyun_logs_log-varlog value: /var/log/*.log
示例中创建了一个采集配置，格式为aliyun_logs_{key}，对应的{key}为log-varlog。
aliyun_logs_log-varlog：该env表示创建一个Logstore名为log-varlog，日志采集路径为/var/log/*.log的配置，对应的日志服务采集配置名称也是log-varlog，目的是将容器的/var/log/*.log文件内容采集到log-varlog这个Logstore中。
创建自定义Tag的规则如下：
- name: aliyun_logs_mytag1_tags value: tag1=v1
配置Tag后，当采集到该容器的日志时，会自动附加对应的字段到日志服务。其中mytag1为任意不包含'_'的名称。
如果您的采集配置中指定了非stdout的采集路径，需要在此部分创建相应的volumeMounts。
示例中采集配置添加了对/var/log/*.log的采集，因此相应地添
