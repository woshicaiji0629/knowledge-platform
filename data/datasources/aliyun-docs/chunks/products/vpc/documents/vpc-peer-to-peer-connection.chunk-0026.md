### 计费说明
同地域VPC对等连接：两端VPC属于同账号或跨账号，均不收取任何费用。
跨地域VPC对等连接：统一由[云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)按出向流量收取[流量传输费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers)。
计费单价根据地域到地域粒度、链路类型来确定。支持铂金、金两种链路类型，提供不同质量的流量传输服务。
计费周期为每小时。如果在计费周期内切换链路类型，将按照较高服务等级的单价进行计费。
如图，跨地域跨账号的VPC1和VPC2建立了对等连接。若 VPC1 和 VPC2 通过对等连接流出的流量分别为200GB和100GB，链路类型选择金，华北5（呼和浩特）到华南3（广州）的[跨地域流量费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers)单价为0.48元/GB。依据出向流量计费规则：
账号A需要支付的费用为：0.48元/GB × 200GB = 96元
账号B需要支付的费用为：0.48元/GB × 100GB = 48元
