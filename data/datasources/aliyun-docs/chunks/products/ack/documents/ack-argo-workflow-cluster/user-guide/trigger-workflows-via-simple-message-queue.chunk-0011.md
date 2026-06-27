## 步骤五：清除Event相关资源
清除相关资源。
清除Event Sensor
kubectl delete sensor ali-mns
清除Event Source
kubectl delete eventsource ali-mns
清除Event Bus
kubectl delete eventbus default
查看Pod状态，确认所有资源已清除。
kubectl get pod
该文章对您有帮助吗？
反馈
