# 配置环境变量 - name: aliyun_logs_app2-stdout value: stdout - name: aliyun_logs_app2-stdout_logstore value: stdout-logstore
- 定制需求2：将不同应用数据采集到不同的Project
如果需要将不同应用的数据采集到多个Project中，需要进行以下操作：
在每个Project中创建一个机器组，选择自定义标识，标识名为k8s-group-{cluster-id}，其中{cluster-id}为集群ID，机器组名称可以自定义配置。
在每个应用的环境变量中配置project、logstore、machinegroup信息，其中机器组名称为上一步创建的机器组名称。
如下示例中应用1的{key}为app1-stdout，应用2的{key}为app2-stdout。其中如果两个应用在同一个K8s集群中，对应的machinegroup可以使用同一个machinegroup。
应用1设置的环境变量为：
