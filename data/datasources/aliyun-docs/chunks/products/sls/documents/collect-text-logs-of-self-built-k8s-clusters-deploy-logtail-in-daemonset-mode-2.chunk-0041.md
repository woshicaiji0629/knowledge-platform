### 场景二：采集并处理多行日志
日志服务默认为单行模式，按行进行日志的切分与存储，导致含堆栈信息的多行日志被逐行切分，每一行作为独立日志存储和展示，不利于分析。
针对上述问题，可通过开启多行模式来改变日志服务的切分方式，并通过配置正则表达式匹配日志起始行，从而将原始日志按照起始行规则进行切分和存储。示例如下：
完整YAML示例
apiVersion: telemetry.alibabacloud.com/v1alpha1 kind: ClusterAliyunPipelineConfig metadata: name: multiline-config spec: config: aggregators: [] global: {} inputs: - Type: input_file FilePaths: - /root/log/text1.log MaxDirSearchDepth: 0 FileEncoding: utf8 Multiline: StartPattern: '\[\d+-\d+-\w+:\d+:\d+,\d+]\s\[\w+]\s.*' Mode: custom UnmatchedContentTreatment: single_line EnableContainerDiscovery: true processors: [] flushers: - Type: flusher_sls Logstore: my-log-logstore sample: |- [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) project: name: my-log-project logstores: - name: my-log-logstore
