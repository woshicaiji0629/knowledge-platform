## 通过Argo UI访问日志服务
无论工作流Pod是否被删除，您都可以通过Argo UI访问Pod的日志。如果Pod被删除，则访问SLS获取日志并显示到Argo UI。
在 Argo Workflows 的Logs页面中，选择目标工作流（如hello-world）及对应容器后，即可查看 Pod 的运行日志。若暂未获取到日志数据，页面底部会提示尝试通过 Artifacts 获取日志。
