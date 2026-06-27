## 步骤二：创建并配置日志采集规则
定义 LoongCollector 采集哪些日志、如何解析日志结构、如何过滤内容，并将配置绑定到已注册的机器组。
在日志库页面，单击目标LogStore名称前的展开。
单击接入数据后的，在快速数据接入弹框中，根据日志源选择接入模板，并单击立即接入：
Docker 标准输出：选择Docker标准输出-新版
容器标准输出采集支持新版与旧版两种模板，推荐使用新版。如需了解新、旧版本差异，请参考[附录：容器标准输出新旧版本对比](collect-docker-container-text-logs.md)。使用旧版采集参考[采集](collect-docker-container-standard-output.md)[Docker](collect-docker-container-standard-output.md)[容器的标准输出（旧版）](collect-docker-container-standard-output.md)。
Docker 文件日志：选择Docker文件-容器
机器组配置，完成后单击下一步：
使用场景：选择Docker场景。
将[步骤一](collect-docker-container-text-logs.md)中创建好的机器组从源机器组列表添加至右侧应用机器组。
在Logtail配置页面，完成如下配置，并单击下一步。
