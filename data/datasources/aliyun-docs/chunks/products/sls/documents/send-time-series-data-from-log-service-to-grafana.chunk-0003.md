## 导入日志服务Grafana模板
您可以在Grafana模板市场中查找日志服务提供的可视化模板并一键导入到您的Grafana中，进行可视化展示。
复制Grafana模板ID。
登录[Grafana](https://grafana.com/grafana/dashboards?search=SLS)[模板市场](https://grafana.com/grafana/dashboards?search=SLS)。
单击您要导入的模板。
在页面右侧，单击Copy ID to Clipboard。
登录Grafana。
在左侧导航栏中，选择Create>Import。
在Grafana.com Dashboard文本框中输入您在[步骤](send-time-series-data-from-log-service-to-grafana.md)[1](send-time-series-data-from-log-service-to-grafana.md)中复制的Grafana模板ID。
配置完成后，单击空白处，即可进入配置页面，配置数据源。
配置数据源。
此处需配置为您在[对接](send-time-series-data-from-log-service-to-grafana.md)[Grafana](send-time-series-data-from-log-service-to-grafana.md)中添加的数据源。不同仪表盘对应的数据源参数不同，可能为telegraf、host等。
单击Import。
