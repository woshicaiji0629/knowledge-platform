## 控制台
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，在页面右上角单击重启。
在弹窗中，选择重启模式。
不勾选强制重启实例（默认）：操作系统会尝试正常关闭所有进程后，执行重启操作。
勾选强制重启实例：相当于执行断电操作，存在丢失内存数据和文件系统损坏的风险，建议仅在实例无法响应非强制重启时使用。
执行重启操作：
立即重启：单击确定即可。
定时执行重启：可以通过勾选设置定时执行，指定未来某一时刻开始执行实例重启操作，根据页面提示完成时间配置及角色选择后，单击确定生成定时重启实例任务。任务创建后可前往[系统运维管理](https://oos.console.aliyun.com/cn-hangzhou/trigger/time)[OOS](https://oos.console.aliyun.com/cn-hangzhou/trigger/time)[控制台-定时运维](https://oos.console.aliyun.com/cn-hangzhou/trigger/time)修改任务配置。
重启实例时，实例内部操作系统需释放进程、CPU、内存等资源，同时虚拟化层也需释放相关资源，整个操作所需的时间可能较长，请耐心等待，预计耗时为3~5分钟，最长不超过20分钟。
