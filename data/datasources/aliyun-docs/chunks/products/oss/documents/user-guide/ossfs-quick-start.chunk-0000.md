# 使用ossfs将OSS的Bucket挂载到Linux系统中
ossfs是一款能够将对象存储OSS中的Bucket挂载到本地Linux系统的工具。您的应用程序可以通过文件系统操作（例如open和read）访问存储在OSS中的对象。ossfs会自动将这些操作转换为OSS的API调用。
说明
ossfs分为1.0和2.0两个版本。2.0版本是面向新形态计算密集型应用进行了全面重构的版本，实现了性能的全面升级，但对POSIX语义进行了部分限制，是未来的主线演进版本。如果您正在开展AI训练、推理、自动驾驶仿真等新型应用，且不方便使用OSS SDK和[使用](../developer-reference/oss-connector-overview.md)[OSS Connector for AI/ML](../developer-reference/oss-connector-overview.md)[加速模型训练](../developer-reference/oss-connector-overview.md)，强烈建议使用[ossfs 2.0](../developer-reference/ossfs-2-0.md)。相较之下，[ossfs 1.0](../developer-reference/ossfs-overview.md)对POSIX语义支持更为全面，适合对性能无特殊需求的场景日常使用。
