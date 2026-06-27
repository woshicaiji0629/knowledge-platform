## 鉴权机制
OSS根据请求类型采用不同的鉴权流程：
签名请求：OSS验证签名有效性后，分别评估Control Policy（如有）、RAM Policy、Bucket Policy、ACL，综合判定是否允许访问。
匿名请求：OSS评估Control Policy（如有）、Bucket Policy和ACL是否允许公开访问。
鉴权结果分为三类：Allow（策略明确授权）、Explicit Deny（策略明确拒绝，优先级最高）、Implicit Deny（无授权则拒绝）。
完整的鉴权流程请参见[鉴权流程详解](authentication.md)。
