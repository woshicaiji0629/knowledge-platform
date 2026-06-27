## 云端节点池
执行以下命令查询集群的GPU共享能力。
kubectl inspect cgpuNAME IPADDRESS GPU0(Allocated/Total) GPU1(Allocated/Total) GPU Memory(GiB) cn-shanghai.192.168.0.4 192.168.0.4 0/7 0/7 0/14 --------------------------------------------------------------------- Allocated/Total GPU Memory In Cluster: 0/14 (0%)
说明
您可以执行命令kubectl inspect cgpu -d，查询GPU共享能力详细信息。
部署共享GPU示例应用，该示例应用申请3 GiB显存。
apiVersion: batch/v1 kind: Job metadata: name: gpu-share-sample spec: parallelism: 1 template: metadata: labels: app: gpu-share-sample spec: nodeSelector: alibabacloud.com/nodepool-id: npxxxxxxxxxxxxxx # 此处需替换为您创建的云端节点池ID。 containers: - name: gpu-share-sample image: registry.cn-hangzhou.aliyuncs.com/ai-samples/gpushare-sample:tensorflow-1.5 command: - python - tensorflow-sample-code/tfjob/docker/mnist/main.py - --max_steps=100000 - --data_dir=tensorflow-sample-code/data resources: limits: # 单位为GiB，该Pod总共申请了3 GiB显存。 aliyun.com/gpu-mem: 3 # 设置GPU显存大小。 workingDir: /root restartPolicy: Never
