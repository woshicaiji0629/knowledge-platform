### 1. 修改业务Pod YAML配置
定义共享卷
在spec.template.spec.volumes中添加三个共享卷（与containers同级）：
volumes: # 共享日志目录（业务容器写入，Sidecar 读取） - name: ${shared_volume_name} # <-- 名称需与volumeMounts中的name一致 emptyDir: {} # 容器间通信信令目录（用于优雅启停） - name: tasksite emptyDir: medium: Memory # 使用内存作为介质，性能更高 sizeLimit: "50Mi" # 共享主机时区配置：同步Pod内所有容器的时区 - name: tz-config # <-- 名称需与volumeMounts中的name一致 hostPath: path: /usr/share/zoneinfo/Asia/Shanghai # 请按需修改时区
配置业务容器挂载
在业务容器（如your-business-app-container）的volumeMounts中添加以下挂载项：
确保业务容器将日志写入${shared_volume_path}目录，LoongCollector 才能正确采集。
volumeMounts: # 挂载共享日志卷到业务日志输出目录 - name: ${shared_volume_name} mountPath: ${shared_volume_path} # 例如：/var/log/app # 挂载通信目录 - name: tasksite mountPath: /tasksite # 与 Loongcollector容器通信的共享目录 # 挂载时区文件 - name: tz-config mountPath: /etc/localtime readOnly: true
注入LoongCollector Sidecar容器
在spec.template.spec.containers数组中追加以下 Sidecar 容器定义：
- name: loongcollector image: aliyun-observability-release-registry.cn-shenzhen.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sle
