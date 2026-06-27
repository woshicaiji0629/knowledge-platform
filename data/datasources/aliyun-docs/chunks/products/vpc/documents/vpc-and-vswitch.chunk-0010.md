### 使用附加网段扩充网段地址
当专有网络的可用IP地址数不足以满足扩展的业务规模，或者前期网络规划不当导致地址不足时，可以使用附加网段扩充VPC地址空间。
附加网段与主网段同时生效，可用于创建交换机、部署ECS等云产品资源。
1、不能使用100.64.0.0/10、224.0.0.0/4、127.0.0.0/8或169.254.0.0/16网段作为IPv4附加网段。2、附加网段的地址块不能与主网段重叠。3、每个专有网络默认支持添加[5](understanding-vpc-quotas-in-alibaba-cloud.md)[个](understanding-vpc-quotas-in-alibaba-cloud.md)[IPv4](understanding-vpc-quotas-in-alibaba-cloud.md)[附加网段，5](understanding-vpc-quotas-in-alibaba-cloud.md)[个](understanding-vpc-quotas-in-alibaba-cloud.md)[IPv6](understanding-vpc-quotas-in-alibaba-cloud.md)[附加网段](understanding-vpc-quotas-in-alibaba-cloud.md)。
