.ixxx Ready <none> 22d v1.11.2 cn-hangzhou.ixxx Ready <none> 22d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready master 46d v1.11.2 cn-hangzhou.ixxx Ready <none> 46d v1.11.2 cn-hangzhou.ixxx Ready <none> 46d v1.11.2 [root@xxx ~]#
方法二：通过控制台
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面中，单击目标集群名称或者目标集群右侧操作列下的详情。
在集群管理页的左侧导航栏中，选择节点管理>节点获取Master个数和对应的名称、IP地址、实例ID。
执行以下命令替换job-master.yml文件中指定的变量${jobname}和${hostname}。
sed 's/${jobname}/cert-job-2/g; s/${hostname}/hostname/g' job-master.yml > job-master2.yml
其中：
${jobname}为Job的名称，此处设置为cert-job-2。
${hostname}为集群Master节点的名称，此处请将hostname替换为步骤2中查看到的Master名称。
执行以下命令创建Job。
kubectl create -f job-master2.yml
执行以下命令查看Job状态，当COMPLETIONS均为1时，证书完成更新。
kubectl get job -nkube-system
重复执行步骤3~5，完成所有Master节点的证书更新。
[root@xxx ~]# kubectl get job -nkube-system NAME COMPLETIONS DURATION AGE cert-job-2 1/1 46s 22m cert-job-3 1/1 28s 2m cert-job-4 1/1 26s 1m [root@xxx ~]#
