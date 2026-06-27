u-worker-1 0/1 Pending 0 43s tf-smoke-gpu-worker-2 0/1 Pending 0 43s tf-smoke-gpu-worker-3 0/1 Pending 0 43s
当集群中新增4个GPU卡的资源时，当前集群的资源满足设定的最小数要求。此时PodGroup正常调度，4个Worker类型Pod开始运行。执行以下命令查看Pod状态。
kubectl get pods
预期输出：
NAME READY STATUS RESTARTS AGE tf-smoke-gpu-ps-0 1/1 Running 0 3m16s tf-smoke-gpu-worker-0 1/1 Running 0 3m16s tf-smoke-gpu-worker-1 1/1 Running 0 3m16s tf-smoke-gpu-worker-2 1/1 Running 0 3m16s tf-smoke-gpu-worker-3 1/1 Running 0 3m16s
执行以下命令查看其中一个Worker类型Pod的日志。显示训练任务已经开始。
kubectl logs -f tf-smoke-gpu-worker-0
系统输出类似以下结果，表示训练任务已经开始。
INFO|2020-05-19T07:15:24|/opt/launcher.py|27| Running warm up INFO|2020-05-19T07:21:04|/opt/launcher.py|27| Done warm up INFO|2020-05-19T07:21:04|/opt/launcher.py|27| Step Img/sec loss INFO|2020-05-19T07:21:05|/opt/launcher.py|27| 1 images/sec: 31.6 +/- 0.0 (jitter = 0.0) 8.318 INFO|2020-05-19T07:21:15|/opt/launcher.py|27| 10 images/sec: 31.1 +/- 0.4 (jitter = 0.7) 8.343 INFO|2020-05-19T07:21:25|/opt/launcher.py|27| 20 images/sec: 31.5 +/- 0.3 (jitter = 0.7) 8.142
