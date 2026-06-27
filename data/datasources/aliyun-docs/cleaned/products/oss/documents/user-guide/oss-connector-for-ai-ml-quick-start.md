# 使用OSS Connector for AI/ML读取OSS数据训练PyTorch模型-对象存储-阿里云-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/oss-connector-for-ai-ml-quick-start?spm=a2c4g.11186623.help-menu-31815.d_1_6.23aa535dEv4tws

# 使用OSS Connector for AI/ML高效完成数据训练任务
本文将为您详细介绍如何快速使用OSS Connector for AI/ML来高效配合数据模型的创建以及训练工作。
## 部署环境
操作系统：Linux x86-64
glibc：>=2.17
Python：3.8-3.12
PyTorch： >=2.0
使用OSS Checkpoint功能需Linux内核支持userfaultfd
说明
以Ubuntu系统为例，您可以执行sudo grep CONFIG_USERFAULTFD /boot/config-$(uname -r)命令确认Linux是否支持userfaultfd，当返回结果中显示CONFIG_USERFAULTFD=y时，则表示内核支持。返回结果显示CONFIG_USERFAULTFD=n时，则表示内核不支持，即无法使用OSS Checkpoint功能。
## 快速安装
以下内容为Python3.12版本安装OSS Connector for AI/ML示例：
在Linux操作系统或基于Linux操作系统构建镜像所生成容器空间内，执行pip3.12 install osstorchconnector命令安装OSS Connector for AI/ML。
pip3.12 install osstorchconnector
执行pip3.12 show osstorchconnector命令查看是否安装成功。
pip3.12 show osstorchconnector
当返回结果中显示osstorchconnector的版本信息时表示OSS Connector for AI/ML安装成功。
Name: osstorchconnector Version: 1.0.0rc1 Summary: OSS connector for AI/ML Home-page: Author: Author-email: License: Location: /usr/local/lib/python3.12/dist-packages Requires: torch Required-by:
## 配置
创建访问凭证配置文件。
mkdir -p /root/.alibabacloud && touch /root/.alibabacloud/credentials
添加访问凭证配置并保存。
示例中的<Access-key-id>、<Access-key-secret>请分别替换为RAM用户的AccessKey ID、AccessKeySecret。关于如何创建AccessKey ID和AccessKeySecret，请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)，配置项说明以及使用临时访问凭证配置请参见[配置访问凭证](../developer-reference/oss-connector-configuration.md)。
{ "AccessKeyId": "LTAI************************", "AccessKeySecret": "At32************************" }
创建OSS Connector配置文件。
mkdir -p /etc/oss-connector/ && touch /etc/oss-connector/config.json
添加OSS Connector相关配置并保存。配置项说明请参见[配置](../developer-reference/oss-connector-configuration.md)[OSS Connector](../developer-reference/oss-connector-configuration.md)。
正常情况下使用以下默认配置即可。
{ "logLevel": 1, "logPath": "/var/log/oss-connector/connector.log", "auditPath": "/var/log/oss-connector/audit.log", "datasetConfig": { "prefetchConcurrency": 24, "prefetchWorker": 2 }, "checkpointConfig": { "prefetchConcurrency": 24, "prefetchWorker": 4, "uploadConcurrency": 64 } }
## 示例
以下示例旨在使用PyTorch创建一个手写数字识别模型。该模型使用由[OssMapDataset](../developer-reference/ossmapdataset.md)构建的MNIST数据集，同时借助[OssCheckpoint](../developer-reference/checkpoint.md)来实现模型检查点的保存和加载。
import io import torch import torch.nn as nn import torch.optim as optim import torchvision.transforms as transforms from PIL import Image from torch.utils.data import DataLoader from osstorchconnector import OssMapDataset from osstorchconnector import OssCheckpoint # 定义超参数。 EPOCHS = 1 BATCH_SIZE = 64 LEARNING_RATE = 0.001 CHECKPOINT_READ_URI = "oss://you_bucketname/epoch.ckpt" # 读取OSS中检查点的地址。 CHECKPOINT_WRITE_URI = "oss://you_bucketname/epoch.ckpt" # 保存检查点到OSS的地址。 ENDPOINT = "oss-cn-hangzhou-internal.aliyuncs.com" # 访问OSS的内网地域节点地址，使用此地址需ECS实例与OSS实例处于同一地域。 CONFIG_PATH = "/etc/oss-connector/config.json" # OSS Connector配置文件路径。 CRED_PATH = "/root/.alibabacloud/credentials" # 访问凭证配置文件路径。 OSS_URI = "oss://you_bucketname/mnist/" # OSS中Bucket资源路径地址。 # 创建OssCheckpoint对象，用于训练过程中将检查点保存到OSS以及从OSS中读取检查点。 checkpoint = OssCheckpoint(endpoint=ENDPOINT, cred_path=CRED_PATH, config_path=CONFIG_PATH) # 定义简单的卷积神经网络。 class SimpleCNN(nn.Module): def __init__(self): super(SimpleCNN, self).__init__() self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1) self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1) # 使用自适应池化简化尺寸处理 self.adaptive_pool = nn.AdaptiveAvgPool2d((7, 7)) self.fc1 = nn.Linear(64 * 7 * 7, 128) self.fc2 = nn.Linear(128, 10) def forward(self, x): x = nn.ReLU()(self.conv1(x)) x = nn.MaxPool2d(2)(x) x = nn.ReLU()(self.conv2(x)) x = nn.MaxPool2d(2)(x) x = self.adaptive_pool(x) x = x.view(x.size(0), -1) x = nn.ReLU()(self.fc1(x)) x = self.fc2(x) return x # 数据预处理。 trans = transforms.Compose([ transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), transforms.Normalize(mean=[0.5], std=[0.5]) ]) def transform(object): try: img = Image.open(io.BytesIO(object.read())).convert('L') val = trans(img) except Exception as e: raise e # 从对象路径中提取标签，假设路径格式为 oss://bucket/mnist/label/filename # 根据实际数据集组织结构调整标签提取逻辑 try: label = int(object.key.split('/')[-2]) # 提取倒数第二个路径段作为标签 except (ValueError, IndexError): label = 0 # 默认标签，实际使用时需根据数据集结构调整 return val, torch.tensor(label) # 加载OssMapDataset数据集。 train_dataset = OssMapDataset.from_prefix(OSS_URI, endpoint=ENDPOINT, transform=transform, cred_path=CRED_PATH, config_path=CONFIG_PATH) train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, num_workers=32, prefetch_factor=2, shuffle=True) # 初始化模型、损失函数与优化器。 model = SimpleCNN() criterion = nn.CrossEntropyLoss() optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE) # 训练模型。 for epoch in range(EPOCHS): for i, (images, labels) in enumerate(train_loader): optimizer.zero_grad() outputs = model(images) loss = criterion(outputs, labels) loss.backward() optimizer.step() if (i + 1) % 100 == 0: print(f'Epoch [{epoch + 1}/{EPOCHS}], Step [{i + 1}/{len(train_loader)}], Loss: {loss.item():.4f}') # 使用OssCheckpoint对象保存检查点。 with checkpoint.writer(CHECKPOINT_WRITE_URI) as writer: torch.save(model.state_dict(), writer) print("-------------------------") print("检查点已保存") print(model.state_dict()) # 使用OssCheckpoint对象读取检查点。 try: with checkpoint.reader(CHECKPOINT_READ_URI) as reader: state_dict = torch.load(reader) # 加载模型。 model = SimpleCNN() model.load_state_dict(state_dict) model.eval() print("检查点加载成功") except Exception as e: print(f"检查点加载失败: {e}") # 可以选择从头开始训练或使用其他检查点
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
