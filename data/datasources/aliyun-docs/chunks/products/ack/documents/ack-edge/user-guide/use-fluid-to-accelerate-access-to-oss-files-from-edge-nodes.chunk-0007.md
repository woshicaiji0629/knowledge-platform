## 步骤三：创建应用容器体验加速效果
您可以通过创建应用容器使用JindoFS加速服务，或提交机器学习作业来体验其相关功能。本文将以创建一个应用容器多次访问同一数据为例，通过对比访问时间，展示JindoRuntime的加速效果。
使用以下YAML文件样例，创建名为app.yaml 的文件。
apiVersion: v1 kind: Pod metadata: name: demo-app spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxx containers: - name: demo image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 volumeMounts: - mountPath: /data name: hadoop volumes: - name: hadoop persistentVolumeClaim: claimName: hadoop
说明
在ACK Edge集群中，您需要通过nodeSelector将测试Pod部署到[步骤二](use-fluid-to-accelerate-access-to-oss-files-from-edge-nodes.md)指定的节点池中。
执行以下命令，创建应用容器。
kubectl create -f app.yaml
执行以下命令，查看文件大小。
kubectl exec -it demo-app -- bash du -sh /data/spark-3.0.1-bin-hadoop2.7.tgz
预期输出：
210M /data/spark-3.0.1-bin-hadoop2.7.tgz
执行如下命令，查看文件的拷贝时间。
time cp /data/spark-3.0.1-bin-hadoop2.7.tgz /dev/null
预期输出：
real 0m18.386s user 0m0.002s sys 0m0.105s
从上述输出信息，可以知道文件拷贝时间消耗了18s。
执行以下命令，查看此时Dataset的缓存情况。
kubectl get dataset hadoop
预期输出：
NAME UFS TOTAL SIZE CACHED CACHE CAPACITY CACHED PERCENTAGE PHASE AGE hadoop 210.00MiB 210.00MiB 4.00GiB 100.0% Bound 1h
从上述输出信息，可以知道210 MiB的数据已经都缓存到了本地。
执行以下命令，删除之前的应用容器，新建相同的应用容器。
说明
这样做的目的是为了避免其他因素（例如：Page Cache
