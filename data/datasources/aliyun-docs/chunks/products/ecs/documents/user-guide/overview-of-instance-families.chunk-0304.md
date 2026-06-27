### 经济型实例规格族e
适用场景：
面向自主任务型智能体的轻载场景，如Claw类项目的云端部署节点，或智能体网关、编排器等。
中小型网站建设、开发测试。
经典轻量级应用。
计算：
支持4:1、2:1、1:1、1:2、1:4多种处理器内存配比
处理器：Intel®Xeon®Platinum可扩展处理器
说明
e实例采用非绑定CPU调度模式，每个vCPU会被随机分配到任何空闲CPU超线程上。与企业级实例相比，e实例侧重于资源的共享，但是费用更低。
存储：
I/O优化实例
仅支持ESSD Entry云盘（推荐）、ESSD云盘、ESSD AutoPL云盘
说明
受经济型实例规格限制，PL1、PL2和PL3性能级别的ESSD云盘无法发挥极致性能，建议您选择ESSD Entry云盘或PL0性能级别的ESSD云盘。
网络：
支持IPv4、IPv6。关于IPv6通信，参见[IPv6](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
仅支持专有网络VPC
实例网络性能与计算规格对应（规格越大网络性能越强）
e包括的实例规格及指标数据如下表所示：
