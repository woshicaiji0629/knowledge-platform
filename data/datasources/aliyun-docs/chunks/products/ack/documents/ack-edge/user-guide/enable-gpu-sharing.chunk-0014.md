## 云端节点池
登录目标Master节点。
执行以下命令，查看已部署应用的日志，验证cGPU显存隔离是否部署成功。
kubectl logs gpu-share-sample --tail=1
预期输出：
2023-08-07 09:08:13.931003: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1326] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 2832 MB memory) -> physical GPU (device: 0, name: Tesla T4, pci bus id: 0000:00:07.0, compute capability: 7.5)
预期输出表明，容器申请的显存为2832 MB。
执行以下命令，登录容器查看容器被分配显存总量。
kubectl exec -it gpu-share-sample nvidia-smi
预期输出：
Mon Aug 7 08:52:18 2023 +-----------------------------------------------------------------------------+ | NVIDIA-SMI 418.87.01 Driver Version: 418.87.01 CUDA Version: 10.1 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | |===============================+======================+======================| | 0 Tesla T4 On | 00000000:00:07.0 Off | 0 | | N/A 41C P0 26W / 70W | 3043MiB / 3231MiB | 0% Default | +-------------------------------+----------------------+----------------------+ +-------------------------------------------------------------------------
