- 定制需求1：将多个应用数据采集到同一Logstore
如果您需要将多个应用数据采集到同一Logstore，可以设置aliyun_logs_{key}_logstore参数，例如以下配置将2个应用的stdout采集到stdout-logstore中。
示例中应用1的{key}为app1-stdout，应用2的{key}为app2-stdout。
应用1设置的环境变量为：
