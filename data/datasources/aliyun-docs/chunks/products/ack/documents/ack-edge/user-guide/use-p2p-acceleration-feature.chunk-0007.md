### 访问方式
P2P YAML中关于exporter字段定义了Metrics的端口。
ExporterConfig: enable: true # 是否开启 port: 65006 # 监听端口 standaloneExporterPort: true # 是否采用独立端口暴露，如果为false，则通过http服务端口吐出
curl 127.0.0.1:$port/metrics可以得到Metrics结果如下。
