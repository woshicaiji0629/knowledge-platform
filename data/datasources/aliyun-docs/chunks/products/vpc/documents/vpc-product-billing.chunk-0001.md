## VPC对等连接计费说明
同地域VPC对等连接：两端VPC属于同账号或跨账号，均不收取任何费用。
跨地域VPC对等连接：统一由[云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)按出向流量收取[流量传输费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers)。
计费单价根据地域到地域粒度、链路类型来确定。支持铂金、金两种链路类型，提供不同质量的流量传输服务。
铂金（服务可用性承诺：99.995%）：适用于对链路抖动、链路时延非常敏感，对链路质量要求较高的业务。例如证券交易、在线语音、视频会议、实时游戏等。
金（服务可用性承诺：99.95%）：适用于对链路质量不敏感的业务。例如数据同步、文件传输等。
计费周期为每小时。如果在计费周期内切换链路类型，将按照较高服务等级的单价进行计费。
