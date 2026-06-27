DD/SSD/MEM 中的其中一种缓存类型。 |
| path | 表示存储路径，暂时只支持单个路径。当选择 MEM 做缓存时，需指定一个本地路径来存储 Log 等文件。 |
| quota | 表示缓存最大容量，单位 GB。 |
| high | 表示存储容量上限大小。 |
| low | 表示存储容量下限大小。 |

执行以下命令，创建JindoRuntime和Dataset。
kubectl create -f resource.yaml
执行以下命令，查看Dataset的部署情况。
kubectl get dataset hadoop
预期输出：
NAME UFS TOTAL SIZE CACHED CACHE CAPACITY CACHED PERCENTAGE PHASE AGE hadoop 210MiB 0.00B 4.00GiB 0.0% Bound 1h
执行以下命令，查看JindoRuntime的部署情况。
kubectl get jindoruntime hadoop
预期输出：
NAME MASTER PHASE WORKER PHASE FUSE PHASE AGE hadoop Ready Ready Ready 4m45s
执行以下命令，查看PV和PVC的创建情况。
kubectl get pv,pvc
预期输出：
NAME CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM STORAGECLASS REASON AGE persistentvolume/hadoop 100Gi RWX Retain Bound default/hadoop 52m NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS AGE persistentvolumeclaim/hadoop Bound hadoop 100Gi RWX 52m
从上述输出的查询信息，可以知道Dataset和JindoRuntime已创建成功。
