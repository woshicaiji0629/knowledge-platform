# 为ECS实例配置应用性能加速-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/booster-extensions

# 为ECS实例配置应用性能加速
在购买ECS实例时，可以使用应用性能加速类扩展程序获取特定类型应用的开机即用性能调优服务（某些应用也为ECS存量实例提供性能加速类扩展程序）。本文主要介绍如何安装性能加速应用、应用的性能收益、如何卸载应用以及如何关闭性能加速能力。
非GPU类型实例：购买部分Alibaba Cloud Linux 3操作系统的倚天实例、AMD实例或Intel实例时，如果勾选特定应用类型（例如Nginx、MySQL、Redis等）的应用性能加速扩展程序，系统会在实例上自动安装所选应用，并同步安装[KeenTune](https://openanolis.cn/sig/KeenTune)工具对应用进行性能调优，使应用获得平均20%左右的性能提升。（Nginx、Spark、视频流x264/265应用场景也在存量ECS实例的详情页提供了安装指定扩展程序的功能）
GPU类型实例：购买部分Ubuntu 22.04/24.04操作系统的GPU类型实例时，如果勾选AI增强应用性能加速扩展程序，系统会安装AI增强组件，并同步安装[KeenTune](https://openanolis.cn/sig/KeenTune)工具对应用进行性能调优，在某些AI框架（例如bevformer，openclip等）的训练场景能带来15%左右性能提升。
在GPU场景提供的调优涉及到init_on_alloc=0相关的配置，可能会给多租产品客户带来一定的安全风险。
## 非GPU类型ECS实例
### 功能说明
创建实例时部署支持性能加速的应用后，KeenTune会根据应用的业务特点进行全栈性能调优。调优集合了阿里云的经验，不仅优化CPU、内存、I/O、网络等领域，还会对应用本身进行调优，保障业务在最佳性能环境中运行。Nginx、MySQL、Redis、PostgreSQL等应用可获得平均20%左右的性能提升，助力您实现降本增效。默认安装的应用版本及性能收益，请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
### 适用实例
性能加速类扩展程序，仅适用于部分Alibaba Cloud Linux 3操作系统的倚天实例、AMD实例和Intel实例。
| 实例类型 | 规格族 | 操作系统 |
| --- | --- | --- |
| 倚天实例 | [通用型实例规格族](general-purpose-instance-families.md) [g8y](general-purpose-instance-families.md) [计算型实例规格族](compute-optimized-instance-families.md) [c8y](compute-optimized-instance-families.md) [内存型实例规格族](memory-optimized-instance-families-1.md) [r8y](memory-optimized-instance-families-1.md) | [Alibaba Cloud Linux 3](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview) |
| AMD 实例 | [通用型实例规格族](general-purpose-instance-families.md) [g8a](general-purpose-instance-families.md) [计算型实例规格族](compute-optimized-instance-families.md) [c8a](compute-optimized-instance-families.md) [内存型实例规格族](memory-optimized-instance-families-1.md) [r8a](memory-optimized-instance-families-1.md) |  |
| Intel 实例 | [通用型实例规格族](overview-of-instance-families.md) [g8i](overview-of-instance-families.md) [计算型实例规格族](overview-of-instance-families.md) [c8i](overview-of-instance-families.md) [实例规格族](overview-of-instance-families.md) |  |
### 新购ECS实例
如果您是新购ECS实例，可以在创建ECS实例过程中安装应用并配置性能加速。购买实例之后，只能通过命令行方式关闭性能加速能力或卸载已安装的应用。
安装应用性能加速
前往[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)。
购买倚天实例、AMD实例或Intel实例时，安装性能加速类扩展程序。
购买时，请注意以下配置。其他参数配置，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。
倚天实例
实例：选择倚天实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：选择需要安装的应用（如Nginx、MySQL、Redis等），默认版本及性能提升请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
说明
支持安装的应用，以页面实际呈现为准。
Spark性能加速扩展不支持在创建实例时安装，仅支持在创建实例后在实例详情页安装。
启用eRDMA透明替换（可选）：选择Redis且内核版本≥5.10.134-16时，可启用eRDMA透明替换，将传输协议从TCP切换到RDMA，提升网络性能。
重要
eRDMA透明替换技术基于共享内存通信（SMC）实现，启用后，部分用户运维工具将不可用。更多信息，请参见[共享内存通信（SMC）常见问题](https://help.aliyun.com/zh/alinux/user-guide/faq-about-smc)和[共享内存通信（SMC）使能和配置说明](https://help.aliyun.com/zh/alinux/user-guide/use-smc)。
请勿同时选中eRDMA驱动和启动eRDMA透明替换，否则会卸载并安装新的eRDMA驱动，从而导致eRDMA透明替换失效。
关闭eRDMA透明替换：购买实例后，如不再需要该功能，关闭性能加速即可。具体操作请参见[关闭性能加速能力](booster-extensions.md)。
弹性网卡（条件必选）：若选中启用eRDMA透明替换，需在弹性网卡处，勾选弹性RDMA接口。
AMD实例
实例：选择AMD实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：选择需要安装的应用（如Nginx、MySQL、Memcached等），默认版本及性能提升请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
说明
支持安装的应用，以页面实际呈现为准。
Intel实例
实例：选择Intel实例。具体规格请参见[适用实例](booster-extensions.md)。
镜像：选择Alibaba Cloud Linux 3镜像。
扩展程序：
驱动：如需配置eRDMA，请选中eRDMA驱动，系统会自动安装。
性能加速：仅支持选择安装MySQL应用。
默认安装的应用版本及性能提升说明请参见[默认安装的应用版本及性能提升](booster-extensions.md)。
实例创建成功后，系统会自动安装选择的应用，并使用KeenTune针对该应用的业务特点进行全栈性能调优。
关闭性能加速能力
购买实例之后，如果不需要性能加速能力，可以单独卸载KeenTune关闭性能加速，保留已安装的应用。
重要
性能加速主要针对单一应用部署场景，如果您是混合部署场景，建议您在使用混合部署方式之前，参考如下命令关闭性能加速能力。
关闭性能加速能力后，会同步关闭eRDMA透明替换能力。
sudo bash /etc/keentune/target/scripts/set_xps_rps.sh eth0 rps disable sudo keentune profile rollback sudo systemctl stop keentune-target keentuned sudo yum remove keentune-target keentuned
卸载默认安装的应用
购买实例后，如果不需要默认安装的应用程序，可以卸载它们，性能加速能力将保留。重新安装后，程序仍具有性能加速能力。
sudo systemctl stop <APP_Name> sudo yum remove <APP_Name>
说明
<APP_Name>请替换为实际的应用名称（如Nginx）。
### 存量ECS实例
如果您是存量的Alibaba Cloud Linux 3操作系统的倚天实例（g8y、c8y、r8y），可以在实例详情页面选择安装或卸载应用性能加速。
支持安装的应用性能加速：x264/x265、Nginx、Spark性能加速扩展。
重要
Spark性能加速扩展功能在邀测中，如需使用，请联系您的商务经理开通。
Spark性能加速扩展仅支持ecs.g8y.8xlarge及以上规格和ecs.r8y.8xlarge及以上规格。
Spark性能加速扩展不会安装Spark，只提供调优包安装和配置。配置Spark性能加速扩展后，还需修改配置文件，具体操作，请参见[配置](booster-extensions.md)[Spark](booster-extensions.md)[性能加速扩展](booster-extensions.md)。
Spark性能加速扩展仅支持对Spark 3.3版本进行加速，如需支持其他版本，请您的商务经理开通。
具体操作，请参见[安装扩展程序](oos-extension.md)、[卸载扩展程序](oos-extension.md)。
### 默认安装的应用版本及性能提升
默认安装的应用版本及性能提升的说明如下表所示。
倚天实例
| 应用 | 默认安装应用版本 | 测试工具 | 主要指标 | 性能提升比例 |
| --- | --- | --- | --- | --- |
| Nginx | 1.20.1 | wrk | rps（requests per second） | HTTP/HTTPS 小包场景：30% 大包+Gzip 场景：12% |
| MySQL | 8.0.26 | sysbench | qps（queries per second） | 20%（纯读、纯写、混合读写） |
| Redis | 6.0.2 | memtier-benchmark | rps（requests per second） | 25%（单 pipeline 小包场景） |
| PostgreSQL | 13.10-1.0.1 | sysbench | qps（queries per second） | 20%（纯读、纯写、混合读写） |
| Memcached | 1.5.22-2.1 | memtier-benchmark | rps（requests per second） | 10% ~ 20%（单 pipeline 小包场景） |
| x264/x265 | ffmpeg 5.0.1+ x264 0.164.x+ x265 3.5+ | ffmpeg/x264/x265 | fps (frames per second) | x264 编码：20%~30% x265 编码：20%~30% |
| Spark 性能加速扩展 | 3.3 说明 不安装 Spark，仅支持对 Spark 3.3 进行加速。 | TPC-DS | s（second） | 20%~60% |
AMD实例
| 应用 | 默认安装应用版本 | 测试工具 | 主要指标 | 性能提升比例 |
| --- | --- | --- | --- | --- |
| Nginx | 1.20.1 | wrk | rps（requests per second） | HTTP/HTTPS 小包场景：10% |
| MySQL | 8.0.26 | sysbench | qps（queries per second） | 5%（纯读、纯写、混合读写） |
| Memcached | 1.5.22-2.1 | memtier-benchmark | rps（requests per second） | 7%（单 pipeline 小包场景） |
Intel实例
| 应用 | 默认安装应用版本 | 测试工具 | 主要指标 | 性能提升比例 |
| --- | --- | --- | --- | --- |
| MySQL | 8.0.26 | sysbench | qps（queries per second） | 7%（纯读、纯写、混合读写） |
说明
推荐使用默认安装的应用版本，如果后续您自选应用版本，可能无法获取部分优化。优化范围说明如下：
应用本身性能收益（不使用默认安装的应用版本无法获取），包括应用二进制编译和应用配置的优化。
OS相关的性能收益（不使用默认安装的应用版本仍然可以获取），包括boot cmdline、内存配置、网络优化（绑核、XPS、RPS、RFS等）。
### 配置Spark性能加速扩展
在Spark的Master节点和所有Worker节点配置Spark性能加速扩展的详细步骤如下：
在Spark的Master节点和所有Worker节点安装Spark性能加速扩展。
在实例详情页，选择定时与自动化任务>安装 / 卸载扩展程序，单击安装扩展程序。
在安装扩展程序对话框中，公共扩展选择Spark性能加速扩展，配置如下参数，然后单击下一步，按照界面提示完成操作。
worker_number：指Spark集群中Worker节点的数量。
worker_type：指Worker节点的实例规格，当前仅支持ecs.g8y.8xlarge及以上规格和ecs.r8y.8xlarge及以上规格。
在Spark所有Worker节点配置ZSTD。
替换jar包。
for jar in $SPARK_HOME/jars/zstd-*.jar; do sudo mv "$jar" "${jar}.bak"; done sudo cp /opt/keentune/compress/zstd-*.jar $SPARK_HOME/jars/
修改/opt/keentune/spark.conf配置。
如配置parquet文件写入过程的压缩方式，请修改以下参数：
spark.sql.parquet.compression.codec zstd spark.hadoop.parquet.compression.codec.zstd.level 1
重要
如果您的Parquet为1.13以下版本，建议您参考以下步骤升级到1.13及以上版本，以默认启用ZSTD的buffer pool。关于ZSTD JNI BufferPool的说明，请参见[Support ZSTD JNI BufferPool](https://github.com/apache/parquet-java/commit/279255df0c050aa95b5f5eb5963cf7eae5b8d180)。
wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-column/1.13.1/parquet-column-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-common/1.13.1/parquet-common-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-encoding/1.13.1/parquet-encoding-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-format-structures/1.13.1/parquet-format-structures-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.13.1/parquet-hadoop-1.13.1.jar wget https://repo1.maven.org/maven2/org/apache/parquet/parquet-jackson/1.13.1/parquet-jackson-1.13.1.jar for file in $SPARK_HOME/jars/parquet-*.jar; do sudo mv "$file" "$file.bak"; done sudo cp -rf parquet-*.jar $SPARK_HOME/jars
如配置shuffle过程的数据压缩方式，请修改以下参数：
spark.io.compression.zstd.level 1 spark.io.compression.codec zstd
使用Spark存算分离时，需要配置OSS的Endpoint和AccessKey。
使用OSS存储时，必须在/opt/keentune/spark.conf文件中配置s3a相关参数。
spark.hadoop.fs.s3a.endpoint <OSS的Endpoint> spark.hadoop.fs.s3a.access.key <AccessKey ID> spark.hadoop.fs.s3a.secret.key <AccessKey Secret>
在Spark的Master节点使用新的配置启动Spark集群。
您可以使用以下两种方式来启动Spark集群：
直接使用/opt/keentune/spark.conf来重启Spark。
# 任务提交方式一： spark-submit --properties-file=/opt/keentune/spark.conf # 任务提交方式二： spark-sql --properties-file=/opt/keentune/spark.conf
参考优化后的配置修改您自己的spark.conf后重启Spark。
# 任务提交方式一： spark-submit --properties-file=${your_spark.conf} # 任务提交方式二： spark-sql --properties-file=${your_spark.conf}
## GPU类型ECS实例
### 功能说明
创建实例时部署了支持“AI增强”性能加速后，会安装KeenTune会针对AI训练的业务特点进行OS上CPU、内存、网络等相关的调优，并且提供CPFS FUSE加速等能力。在某些AI框架的训练场景能带来15%+性能提升，具体的框架、模型版本及性能收益，请参见[框架、模型版本及性能](a.md)
### 适用实例
| 实例类型 | 实例规格族 | 操作系统 |
| --- | --- | --- |
| [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [云服务器（gn/vgn/sgn](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [系列）](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) | [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn8v](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn8is](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7e](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7i](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [GPU](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [计算型实例规格族](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) [gn7s](gpu-accelerated-compute-optimized-and-vgpu-accelerated-instance-families-1.md) | 阿里云公共镜像 Ubuntu 22.04 阿里云公共镜像 Ubuntu 24.04 |
| [弹性裸金属服务器规格](elastic-bare-metal-server-overview.md) | [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8is](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn8v](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7i](elastic-bare-metal-server-overview.md) [GPU](elastic-bare-metal-server-overview.md) [计算型弹性裸金属服务器实例规格族](elastic-bare-metal-server-overview.md) [ebmgn7e](elastic-bare-metal-server-overview.md) |  |
### 新购ECS实例
如果为新购ECS实例，可以在创建ECS实例过程中安装应用并配置性能加速。购买实例之后，可以在ECS实例详情页的相关位置进行卸载。
安装AI增强扩展程序
前往[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)。
购买适用的GPU实例时，安装性能加速类扩展程序。购买时，请注意以下配置。其他参数配置，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。
实例创建成功后，系统会使用KeenTune针对该应用的业务特点进行全栈性能调优，并且提供CPFS FUSE加速等能力。
安装AI增强扩展程序将使能FUSE加速，对使用[文件存储](https://help.aliyun.com/zh/cpfs/)[CPFS](https://help.aliyun.com/zh/cpfs/)的场景非常重要，当前仅支持阿里云公共镜像Ubuntu 24.04版本。
重要
系统需要重启后才能保证所有调优项都能够正常生效。
AI增强性能加速扩展可以与GPU、eRDMA扩展一起使用。
卸载AI增强扩展程序
在ECS实例详情页的已安装扩展列表的操作列，单击卸载按钮。
### 模型、框架版本及性能提升
在主流GPU实例上进行了openclip和bevformer模型应用优化前后的性能测试，测试环境和优化效果如下
测试环境
| 测试环境 | 说明 |
| --- | --- |
| 操作系统 | 阿里云公共镜像 Ubuntu 22.04、阿里云公共镜像 Ubuntu 24.04 |
| 内核版本 | 5.15.0-144-generic |
| gcc 版本 | 11.4.0 |
| glibc 版本 | 2.35 |
| keentune | 3.2.61 |
| python | 3.10.12 |
| pytorch | 2.7.0a0+ecf3bae40a.nv25.2 |
| nccl | 2.26.2 |
| mmcv-full | 1.7.2 |
| mmdet3d | 1.0.0rc4 |
优化效果
| 实例规格 | 模型 | 训练/推理 | 平均吞吐提升（samples/s） |
| --- | --- | --- | --- |
| ebmgn8v.48xlarge | Bevformer | bevformer_base 训练 | FP32（10%+） FP16（8%+） |
| Openclip | RN50 推理 | 20%+ |  |
| RN50 训练 | 25%+ |  |  |
CPFS FUSE加速效果如下表所示：
CPFS FUSE加速当前仅支持阿里云公共镜像Ubuntu 24.04版本，以下测试数据基于该操作系统版本得出。
| 性能场景分类 | 用例场景 | 性能数据 | 性能提升 | 备注 |
| --- | --- | --- | --- | --- |
| 带宽 | Buffer 读（1M IO） | 40GB/s | 2.5 倍 | 原生 FUSE 约为 15GB/s |
| 带宽 | Buffer 写（1M IO） | 40GB/s | 10 倍 | 原生 FUSE 约为 4GB/s |
| IOPS | Direct 读（4k IO） | 1,000,000 | 2.5 倍 | 原生 FUSE 约为 400,000 |
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
