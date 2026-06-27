vent-queue # 对应轻量消息队列（原 MNS）中的队列名称。 waitTimeSeconds: 20 endpoint: http://165***368.mns.<region>.aliyuncs.com # 对应轻量消息队列（原 MNS）的Endpoint。
应用event-source.yaml文件创建Event Source。
kubectl apply -f event-source.yaml
查看Event Source Pod是否正常启动。
kubectl get pod
