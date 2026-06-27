## 限制说明
地域支持说明：仅中国内地地域支持 Windows 和 Linux 系统间的互相更换，其他地域仅支持同类型系统间的更换（如Linux换Linux，Windows换Windows）。
主机名：在跨类型系统更换前，需确保实例主机名（Hostname）符合目标操作系统的规范。例如，Windows 系统的主机名为2～15 个字符。
非 I/O 优化实例：在实例详情页面下方其他信息区域可查看实例类型，若为非I/O优化，则该实例不支持在控制台更换为 Windows 系统，仅支持通过调用 API[ReplaceSystemDisk](../api-replacesystemdisk.md)更换为下列Windows Server公共镜像。
Windows Server公共镜像
Windows Server 2012 R2数据中心版中文：win2012r2_64_dtc_17196_zh-cn_40G_alibase_20170915.vhd
Windows Server 2012 R2数据中心版英文：win2012r2_64_dtc_17196_en-us_40G_alibase_20170915.vhd
Windows Server 2008 R2企业版中文：win2008r2_64_ent_sp1_zh-cn_40G_alibase_20170915.vhd
Windows Server 2008 R2企业版英文：win2008r2_64_ent_sp1_en-us_40G_alibase_20170915.vhd
目标系统盘容量要求：当更换为Windows操作系统时，系统盘需预留至少1GiB空间，否则更换后实例将无法启动。
镜像限制说明：Alibaba Cloud Linux 3 Pro实例，暂不支持更换为其他操作系统。
