### Bucket Policy、RAM Policy与Control Policy区别

| 维度 | Bucket Policy | RAM Policy | Control Policy |
| --- | --- | --- | --- |
| 配置位置 | Bucket 上 | RAM 身份主体上 | 资源目录的各级资源结构（资源夹、成员）上 |
| 管理视角 | 以资源为中心：谁可以访问此资源 | 以身份为中心：身份主体可访问哪些资源 | 以组织治理为中心：在整个资源目录范围内统一限制权限边界 |
| 匿名访问 | 支持 | 不支持 | 不支持 |

选择建议：授权多个用户访问同一资源时Bucket Policy更高效；管理单个用户的所有资源权限时RAM Policy更直观；需要匿名访问时只能用Bucket Policy；在多账号场景下，可使用Control Policy统一限制权限边界。三者可同时使用，OSS会综合评估，都允许时请求才通过。
