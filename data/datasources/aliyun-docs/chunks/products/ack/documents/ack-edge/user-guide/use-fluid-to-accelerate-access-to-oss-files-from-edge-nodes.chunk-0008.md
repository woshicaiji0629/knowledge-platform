NTAGE PHASE AGE hadoop 210.00MiB 210.00MiB 4.00GiB 100.0% Bound 1h
从上述输出信息，可以知道210 MiB的数据已经都缓存到了本地。
执行以下命令，删除之前的应用容器，新建相同的应用容器。
说明
这样做的目的是为了避免其他因素（例如：Page Cache）对结果造成影响。
kubectl delete -f app.yaml && kubectl create -f app.yaml
执行如下命令，查看文件拷贝时间。
kubectl exec -it demo-app -- bash time cp /data/spark-3.0.1-bin-hadoop2.7.tgz /dev/null
预期输出：
real 0m0.048s user 0m0.001s sys 0m0.046s
从上述输出信息，可以知道进行文件的cp拷贝观察时间消耗48 ms，整个拷贝的时间缩短了300多倍。
说明
由于文件已经被JindoFS缓存，第二次访问所需时间远小于第一次。
