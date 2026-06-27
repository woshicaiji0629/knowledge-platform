### 步骤三：采集并存储Suricata日志
您可以使用Filebeat将Suricata日志数据传输至阿里云Elasticsearch进行索引存储，并通过Kibana进行可视化展示与分析。
登录ECS2服务器，执行如下命令，安装Filebeat。
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.10.0-x86_64.rpm sudo rpm -vi filebeat-7.10.0-x86_64.rpm
修改Suricata模块配置，指定待采集的Suricata流量日志文件。
执行sudo filebeat modules enable suricata命令，启用Suricata模块。
执行sudo vim /etc/filebeat/modules.d/suricata.yml命令，按照以下内容修改Suricata模块配置。
- module: suricata # 配置采集的流量日志文件 eve: enabled: true var.paths: ["/var/log/suricata/eve.json"]
按下Esc键，输入:wq并回车，以保存并关闭文件。
执行sudo vim /etc/filebeat/filebeat.yml配置filebeat.yml文件，设置连接信息。
修改Filebeat modules配置。
filebeat.config.modules: # 全局加载 path: /etc/filebeat/modules.d/suricata.yml # 允许动态地重新加载和应用新的配置文件或设置 reload.enabled: true # 在设定的时间周期内系统自动检查指定路径下的文件是否有任何更改 reload.period: 1s
修改Kibana配置。
setup.kibana: host: "https://es-cn-8l**********2r7ln-kibana.cn-hangzhou.elasticsearch.aliyuncs.com:5601"
host：Kibana的访问地址，可[在](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)[Kibana](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)[配置页面获取](https://help.aliyun.com/zh/es/user-
