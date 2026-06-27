### 通过阿里云Argo CLI开启
阿里云Argo CLI完全兼容开源Argo CLI，增强了日志能力，可以获取工作流已删除Pod的日志。
执行以下命令，配置日志服务参数。
argo config sls Please input log retention days. Default is 7 days. 10
预期输出：
Start to config SLS for your cluster. Created AliyunLogConfig CR workflow-sls-config in default namespace. Created SLS logstore workflow-logstore in SLS project k8s-log-<clusterid>, log retention days is 10 days
预期输出表明，日志服务配置成功。所有工作流日志将被收集到名为workflow-logstore的日志库（Logstore）中。
您可以登录[日志服务控制台](https://sls.console.aliyun.com/)，查找名为k8s-log-<clusterid>的Project，然后查看对应的workflow-logstore。
