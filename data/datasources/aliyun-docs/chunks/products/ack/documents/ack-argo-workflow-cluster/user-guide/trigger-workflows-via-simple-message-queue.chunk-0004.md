/../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[AccessKey](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)[信息](../../../../ram/documents/user-guide/view-the-accesskey-pairs-of-a-ram-user.md)。
创建Secret用于存储AK和SK。
kubectl create secret generic mns-secret\ --from-literal=accesskey=*** \ --from-literal=secretkey=***
创建event-bus-mns.yaml文件，将示例中的参数修改为实际使用的参数值。
topic：需替换为[步骤](trigger-workflows-via-simple-message-queue.md)[2](trigger-workflows-via-simple-message-queue.md)中创建的轻量消息队列（原 MNS）中的主题名称。
endpoint：需替换为[步骤](trigger-workflows-via-simple-message-queue.md)[2](trigger-workflows-via-simple-message-queue.md)中获取的Endpoint。
apiVersion: argoproj.io/v1alpha1 kind: EventBus metadata: name: default spec: alimns: accessKey: key: accesskey name: mns-secret secretKey: key: secretkey name: mns-secret topic: argoeventbus # 对应轻量消息队列（原 MNS）中的主题名称。 endpoint: http://165***368.mns.<region>.aliyuncs.com # 对应轻量消息队列（原 MNS）的Endpoint。
应用event-bus-mns.yaml文件创建Event Bus资源。
kubectl apply -f event-bus-mns.yaml
