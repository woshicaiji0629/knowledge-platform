### 验证持久化存储
删除并重建Pod，在新建的Pod中查看文件是否存在，验证数据的持久化存储。
删除一个应用Pod以触发重建。
kubectl delete pod oss-workload-66fbb85b67-d****
查看Pod，等待新Pod启动并进入Running状态。
kubectl get pod -l app=nginx
查看/data路径下的文件。
以名为oss-workload-66fbb85b67-z****、挂载路径为data的Pod为例。
kubectl exec oss-workload-66fbb85b67-z**** -- ls /data | grep tmpfile
预期输出如下，tmpfile文件仍存在，表明数据可持久化存储。
tmpfile
