## 自建集群安装方式
登录[日志服务控制台](https://sls.console.aliyun.com)，创建Project。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。建议创建一个以k8s-log-custom-开头的Project，例如k8s-log-custom-sd89ehdq。
登录您的Kubernetes集群，根据地域选择命令下载Logtail及其他依赖组件。
#中国地域 wget https://logtail-release-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/kubernetes/0.5.5/alibaba-cloud-log-all.tgz; tar xvf alibaba-cloud-log-all.tgz; chmod 744 ./alibaba-cloud-log-all/k8s-custom-install.sh #海外地域 wget https://logtail-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/kubernetes/0.5.5/alibaba-cloud-log-all.tgz; tar xvf alibaba-cloud-log-all.tgz; chmod 744 ./alibaba-cloud-log-all/k8s-custom-install.sh
修改配置文件./alibaba-cloud-log-all/values.yaml。
