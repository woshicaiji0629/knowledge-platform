/ossfs2.conf
填写挂载信息。以只读方式挂载整个Bucket的配置为例。
说明
查看Bucket的Endpoint请进入[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，选择目标Bucket并进入，接着单击左侧导航栏的概览选项，在概览页的访问端口栏中即可查看目标Bucket所处的地域节点。以杭州地域Bucket为例。
杭州地域 Bucket 的 Endpoint 信息：外网访问对应oss-cn-hangzhou.aliyuncs.com，ECS 经典网络及 VPC 内网访问对应oss-cn-hangzhou-internal.aliyuncs.com，传输加速域名（全地域上传下载加速）对应oss-accelerate.aliyuncs.com，OSS 加速器对应cn-hangzhou-internal.oss-data-acc.aliyuncs.com，所有端口均支持 HTTPS。
打开已创建的ossfs 2.0配置文件，参照以下示例（以杭州地域内网Endpoint为例）配置并保存。内网和OSS加速器Endpoint仅支持同地域VPC内实例挂载，数据传输更快速、稳定；不建议使用外网Endpoint访问ossfs，受高延迟和不稳定的Internet网络连接影响，可能会出现各种卡顿问题。
