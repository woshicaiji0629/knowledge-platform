### 场景1：分组合并
按照规则所在项目、env标签和service标签，对告警进行合并。
告警事件
// 告警A { "alert_name": "Alert1", "project": "Project1", "labels": { "env": "test", "service": "service1" } } // 告警B { "alert_name": "Alert2", "project": "Project1", "labels": { "env": "prod", "service": "service2" } } // 告警C { "alert_name": "Alert3", "project": "Project1", "labels": { "env": "test", "service": "service1" } } // 告警D { "alert_name": "Alert4", "project": "Project1", "labels": { "env": "prod", "service": "service2" } }
配置
在分组合并配置面板中，将合并基准设置为自定义，告警属性选择规则所在项目，告警标签设置为自定义，在自定义标签中输入env,service，行动策略选择SLS内置行动策略，首次等待设置为30秒。
合并结果
告警A和告警C归到同一个合并集合中，告警B和告警D被归到同一个合并集合中。
