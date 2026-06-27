## 可信软件供应链
镜像扫描
容器镜像服务支持所有基于Linux的容器镜像安全扫描，可以识别镜像中已知的漏洞信息。您可以收到相应的漏洞信息评估和相关的漏洞修复建议，为您大幅降低使用容器的安全风险。容器镜像服务也接入了云安全的扫描引擎，可支持镜像系统漏洞、镜像应用漏洞和镜像恶意样本的识别。关于镜像扫描的详细介绍，请参见[容器镜像安全扫描](https://help.aliyun.com/zh/acr/user-guide/scan-container-images#task-2458925)。
镜像签名
在容器镜像管理中，您可以通过内容可信的机制保障镜像来源的安全性及不被篡改。镜像的创建者可以对镜像做数字签名，数字签名将保存在容器镜像服务中。通过在部署前对容器镜像进行签名验证可以确保集群中只部署可信授权方签名的容器镜像，降低在您的环境中运行意外或恶意代码的风险，确保从软件供应链到容器部署流程中应用镜像的安全和可溯源性。关于镜像签名和验签的配置使用流程，请参见[使用](../../ack-managed-and-ack-dedicated/user-guide/use-kritis-validation-hook-to-automatically-verify-the-signatures-of-container-images.md)[kritis-validation-hook](../../ack-managed-and-ack-dedicated/user-guide/use-kritis-validation-hook-to-automatically-verify-the-signatures-of-container-images.md)[组件实现自动验证容器镜像签名](../../ack-managed-and-ack-dedicated/user-guide/use-kritis-validation-hook-to-automatically-verify-the-signatures-of-container-images.md)。
云原生应用交付链
在容器安全高效交付场景中，您可以使用容器镜像服务的云原生应用交付链功能，配置镜像构建、镜像扫描、镜像全球同步和镜像部署等，自定义细粒度安全策略，实现全链路可观测、可追踪的安全交付。保障代码一次提交，全球多地域安全分发和高效部署，将DevOps的交付流程全面升级成DevSecOps。关于云原生应用交付链的详细介绍，请参见[创建交付链](https://help.aliyun.com/zh/acr/user-guide/create-a-delivery-chain#task-2345265)。
