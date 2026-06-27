若默认的RRSA鉴权不满足需求（如使用非默认ServiceAccount或第三方OIDC），可通过修改PV配置来指定具体的ARN或ServiceAccount，详见[如何在](faq-about-oss-volumes-1.md)[RRSA](faq-about-oss-volumes-1.md)[鉴权方式中使用指定的](faq-about-oss-volumes-1.md)[ARNs](faq-about-oss-volumes-1.md)[或](faq-about-oss-volumes-1.md)[ServiceAccount？](faq-about-oss-volumes-1.md)。
创建PV。
kubectl create -f pv-oss-rrsa.yaml
