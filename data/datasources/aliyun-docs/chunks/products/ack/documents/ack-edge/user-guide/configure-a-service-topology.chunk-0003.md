## 注意事项
v1.26.3-aliyun.1以下版本：创建Service时，需要同步配置Service的流量拓扑注解，流量拓扑功能才能生效。如果Service创建完成后，再增加注解配置，流量拓扑功能无法生效，此时需要删除该Service，重新创建。
v1.26.3-aliyun.1及以上版本：Service拓扑注解支持创建后修改，修改后Service拓扑功能会立即生效。
