## ALB Ingress的优势
ALB Ingress为全托管模式，提供更强的Ingress流量管理能力。Nginx Ingress需要用户自行维护，适用于对网关定制有强烈需求的场景。Nginx Ingress和ALB Ingress在产品定位、架构、性能、安全等方面均存在差异。更多差异请参见[Nginx Ingress](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)[和](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)[ALB Ingress](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)[对比](../../../../ack/documents/serverless-kubernetes/user-guide/comparison-among-nginx-ingresses-alb-ingresses-and-mse-ingresses.md)。
在以下场景中，ALB Ingress相比Nginx Ingress具有明显优势：
使用长连接的场景
长连接适用于交互频繁的业务场景，如物联网IoT、互联网金融和在线游戏等。当用户进行配置变更时，Nginx Ingress由于需要Reload Nginx进程，会导致长连接闪断，ALB Ingress配置变更支持热更新，保持长连接稳定，有效避免此问题。
高并发连接场景
物联网业务由于终端设备数量大，往往具有高并发连接的特点。ALB Ingress依托洛神云网络平台，能高效管理会话（session），单个ALB实例即支持千万级连接数。Nginx Ingress支持的会话数有限，同时需要用户自行运维。Nginx Ingress扩容时需要消耗集群内的资源，并且还需要用户手动操作，扩容成本较高。
高QPS场景
互联网业务往往具有高QPS的特点，比如预期内的大促活动和突发的热点事件。ALB Ingress支持自动弹性，高QPS时会自动弹出更多VIP，通过一个ALB实例即可支持百万QPS，因此ALB Ingress拥有比Nginx Ingress更低的延迟。同时Nginx Ingress依赖集群内的资源，
