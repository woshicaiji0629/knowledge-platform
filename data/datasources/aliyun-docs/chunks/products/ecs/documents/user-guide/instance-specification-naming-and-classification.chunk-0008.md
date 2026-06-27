* 4 = 128 vCPU，7表示采用Ampere架构，GPU类型为A10且GPU显存为24 GB。
重要
hpc规格族仅提供物理内核，为优化性能不支持开启超线程配置，即不支持vCPU。例如ecs.hpc8i.32xlarge表示物理内核为64。
规格的命名主要在于规格族的差异，下方表格详细介绍了规格族的组成部分。

| 规格族主体（小写字母） | 规格族后缀（小写字母+数字） |
| --- | --- |
| gn：表示搭载 NVIDIA GPU 的计算型实例 vgn：表示采用 NVIDIA GRID vGPU 加速的独享型实例 sgn：表示采用 NVIDIA GRID vGPU 加速的共享型实例 gi：表示搭载 Intel GPU 的计算型实例 f：表示 FPGA 计算型实例 ebm（c/g/r/gn/hf）：表示弹性裸金属服务器（elastic bare metal） scc（c/g/h/gn/hf）：表示超级计算集群（super computing cluster） hpc：表示高性能计算型实例（High-performance Computing ） | 6v：6 表示采用 Volta/Turing 架构；v 表示 GPU 类型为 V100 且 GPU 显存为 16 GB。 例如，gn6v 表示采用 Volta/Turing 架构，显存为 16 GB，且搭载 NVIDIA V100 GPU 的计算型实例。 6e：6 表示采用 Volta/Turing 架构；e（extend）表示第 2 代 GPU 类型为 V100 且显存为 32 GB。 例如，gn6e 表示采用 Volta/Turing 架构，显存为 32 GB，且搭载 NVIDIA V100 GPU 的计算型实例。 6i：6 表示采用 Volta/Turing 架构；i（inference）表示 GPU 类型为 T4。 例如，gn6i 表示采用 Volta/Turing 架构且搭载 NVIDIA 的 T4 GPU 计算型实例。 6s：6 表示采用 Volta/Turing 架构；s 表示第 6 代 SG-1。 例如，ebmgi6s 表示采用 Intel ® Server GPU 卡和第 6 代 SG-1 芯片的视觉计算型实例。 7：表示采用 Ampere 架构。 7i：7 表示采用 Ampere 架构；i（inference）表示 GPU 类型为 A10 且显存为 24 GB。 7e：7 表示采用 Ampere 架构；ｅ表示同一款 GPU 的大显存版本，例如 V100 的 32 GB（相对 V100 16 GB 来说）。 7s：7 表示采用 Ampere 架构；s 表示用于第 7 代 A30 GPU。 说明 一些特殊规格（例如 ecs.gn7i-c8g1.2xlarge）后缀中 c8g1 表示 vCPU:GPU=8:1. c：core，即 vCPU。 g：GPU。 |
