STATUS RESTARTS AGE tf-smoke-gpu-ps-0 1/1 Running 0 6m43s tf-smoke-gpu-worker-0 1/1 Running 0 6m43s tf-smoke-gpu-worker-1 1/1 Running 0 6m43s tf-smoke-gpu-worker-2 0/1 Pending 0 6m43s tf-smoke-gpu-worker-3 0/1 Pending 0 6m43s
执行以下命令查看其中正在运行的Worker类型Pod的日志。
kubectl logs -f tf-smoke-gpu-worker-0
系统输出类似以下结果，表示已启动的两个Worker类型的Pod处于等待剩余两个Worker类型的Pod启动的状态，已启动的两个Worker类型的Pod占用GPU却没有使用。
INFO|2020-05-19T07:02:18|/opt/launcher.py|27| 2020-05-19 07:02:18.199696: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:3 INFO|2020-05-19T07:02:28|/opt/launcher.py|27| 2020-05-19 07:02:28.199798: I tensorflow/core/distributed_runtime/master.cc:221] CreateSession still waiting for response from worker: /job:worker/replica:0/task:2
使用Gang scheduling功能
执行以下命令查看Pod状态。
kubectl get pods
系统输出以下结果，表示因为集群的资源无法满足设定的最小数要求，PodGroup无法正常调度，所有的Pod一直处于Pending状态。
NAME READY STATUS RESTARTS AGE tf-smoke-gpu-ps-0 0/1 Pending 0 43s tf-smoke-gpu-worker-0 0/1 Pending 0 43s tf-smoke-gpu-worker-1 0/1 Pending 0 43s tf-smoke-gpu-worker-2 0/1 Pending 0 43s tf-smoke-gpu-worker-3 0/1 Pending 0 43s
当集群中新增4个GPU卡的资源时，当前集群的资源满足设定的最小数要求。此时PodGroup正常调度，4
