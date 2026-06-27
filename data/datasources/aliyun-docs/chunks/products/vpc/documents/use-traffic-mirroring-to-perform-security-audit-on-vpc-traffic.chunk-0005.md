8)[Kibana](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)[配置页面获取](https://help.aliyun.com/zh/es/user-guide/configure-kibana-public-network-or-private-network#task-2444468)，格式为<Kibana公网地址>:5601。
修改Elasticsearch output配置。
output.elasticsearch: # 配置存储日志的Elasticsearch实例 hosts: ["http://es-cn-8ly**********r7ln.elasticsearch.aliyuncs.com:9200"] username: "elastic" password: "<your_password>"
host：Elasticsearch的访问地址，[可在实例的基本信息页面获取](https://help.aliyun.com/zh/es/user-guide/view-the-basic-information-of-a-cluster-1#task-2449896)，格式为<实例的私网或公网地址>:9200。
username：Elasticsearch实例的访问用户名，默认为elastic。
password：创建实例时设定的密码，若遗忘，可选择[重置实例访问密码](https://help.aliyun.com/zh/es/user-guide/reset-the-access-password-for-an-elasticsearch-cluster#task-2458093)。
按下Esc键，输入:wq并回车，以保存并关闭文件。
执行以下命令，将Dashboard等信息上传到Elasticsearch和Kibana中，并启用Filebeat服务。
sudo filebeat setup sudo service filebeat start
