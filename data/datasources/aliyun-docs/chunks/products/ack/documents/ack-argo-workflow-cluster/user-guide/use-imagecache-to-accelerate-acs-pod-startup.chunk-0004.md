## 控制台
登录[容器计算服务控制台](https://acs.console.aliyun.com)，在左侧导航栏选择镜像缓存。
在镜像缓存页面，单击页面左上角的创建镜像缓存。
参考页面提示完成地域、镜像缓存与访问凭证、网络连通性配置，并确认创建。
创建镜像缓存后，可以通过其制作事件了解镜像缓存的制作过程。

| 配置项 | 说明 | 示例值 |
| --- | --- | --- |
| 地域 | 目前镜像缓存支持的地域。 | 华北 2（北京） |
| 镜像缓存与访问凭证 | 镜像缓存名 ：长度为[2, 128]个英文小写字母、数字或者连字符（-），不能以连字符开始或结尾。 镜像 ：支持从容器镜像服务企业版、容器镜像服务个人版、制品中心选择目标镜像和版本。 访问凭证 ：同账号 ACR 仓库支持自动免密，无需填写访问凭证。若使用非阿里云容器镜像服务 ACR 托管的镜像，需指定 Server 为镜像仓库域名地址，并配置对应的镜像仓库用户名和镜像仓库密码。 | 镜像缓存名： image-cache-***** 镜像： egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.9.0.1-pytorch2.7-cu128-20250612 |
| 网络连通性配置 | 选择以下方式拉取需要被缓存的容器镜像。 公网方式： 为 专有网络 绑定 [公网 NAT 网关](https://vpcnext.console.aliyun.com/nat/cn-hangzhou/nats) ，并为所选 交换机 配置 SNAT 规则。 自动创建或者使用已有的 弹性公网 IP 。 自动创建的弹性公网 IP 将按照实际产生的流量收费，并在镜像缓存创建完成后自动释放，具体收费细则请参见 [计费概述](../../../../eip/documents/billing-overview.md) 。 VPC 内网方式：推荐将容器镜像上传到相应地域的 [容器镜像服务](https://cr.console.aliyun.com/cn-hangzhou/repositories) [ACR](https://cr.console.aliyun.com/cn-hangzhou/repositories) 企业版实例，通过内网 VPC 地址拉取镜像。 | 请按实际网络信息配置。 |
