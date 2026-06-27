### 通过创建日志服务CR开启
执行以下命令，创建阿里云日志配置CR。日志服务控制器会自动创建一个名为k8s-log-<clusterid>的Project和一个名为workflow-logstore的日志库（Logstore）。
cat << EOF | kubectl apply -f - apiVersion: log.alibabacloud.com/v1alpha1 kind: AliyunLogConfig metadata: name: workflow-sls-config namespace: default spec: # log will store for 5 days lifeCycle: 5 logstore: workflow-logstore logtailConfig: inputType: plugin configName: workflow-sls-config inputDetail: plugin: inputs: - detail: Stderr: true Stdout: true type: service_docker_stdout EOF
