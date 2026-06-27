## 注意事项
目前 ACS 镜像缓存功能在白名单邀测阶段，可[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请开通。
创建镜像缓存会为用户创建Service Linked Role，因此需要确保调用创建的子账号具有ram:CreateServiceLinkedRole权限。
制作完成后会显示镜像缓存大小，该数值为容器镜像解压缩后完整文件和容器镜像缓存额外索引文件的总大小。镜像缓存目前支持解压前不超过500GiB的镜像制作。
镜像缓存单地域默认配额为200，可[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请提升。
镜像缓存单地域支持最多50个镜像缓存同时进行创建，已创建完成的镜像缓存不计入其中。
目前镜像缓存支持的地域：华北2（北京）、华东2（上海）、华东1（杭州）、华北6（乌兰察布）、华南1（深圳）、中国香港、新加坡。
目前镜像缓存支持的镜像类型：linux/amd64。
目前 GPU 场景镜像缓存支持的卡型：G59、G49E、L20（GN8IS）。
在使用已创建的镜像缓存时，请确保 Pod 和镜像仓库之间的网络连通性。
