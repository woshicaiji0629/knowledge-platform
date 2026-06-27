## 使用限制
开启P2P加速后，P2P加速套件会将您的容器镜像地址通过Webhook替换为P2P的镜像地址，例如，您的原始镜像地址为test****vpc.cn-hangzhou.cr.aliyuncs.com/docker-builder/nginx:latest，替换后的P2P加速镜像地址为test****vpc.distributed.cn-hangzhou.cr.aliyuncs.com:65001/docker-builder/nginx:latest。
同时，Webhook会帮您自动生成一个用于加速镜像地址的镜像拉取密钥（基于原始镜像的镜像拉取密钥复制生成），由于该P2P镜像拉取密钥的创建和P2P镜像地址的替换是异步逻辑，因此建议您在下发工作负载前优先下发容器镜像拉取需要的镜像拉取密钥，或手动创建一个用于P2P镜像拉取（domain为test-registry-vpc.distributed.cn-hangzhou.cr.aliyuncs.com:65001）的镜像拉取密钥，然后再下发工作负载，避免由于镜像地址的替换而导致镜像拉取失败。
