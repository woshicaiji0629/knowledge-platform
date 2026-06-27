### GPU规格说明
当前ECI GPU支持的驱动版本为NVIDIA 460.73.01，可支持的CUDA Tookit版本为11.2。关于CUDA Toolkit的更多信息，请参见[NVIDIA CUDA](https://hub.docker.com/r/nvidia/cuda)。
ECI支持通过指定ECS GPU规格来进行实例的创建。运行工作流支持的ECS GPU规格如下所示。
GPU计算型实例规格族gn6v（NVIDIA V100)，例如ecs.gn6v-c8g1.2xlarge。
GPU计算型实例规格族gn6i（NVIDIA T4)，例如ecs.gn6i-c4g1.xlarge。
GPU计算型实例规格族gn5（NVIDIA P100)，例如ecs.gn5-c4g1.xlarge。
GPU计算型实例规格族gn5i（NVIDIA P4)，例如ecs.gn5i-c2g1.large。
关于完整的ECS GPU规格定义，请参见[实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md)。
