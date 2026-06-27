ror-production-traffic-to-a-staging-environment.md)：通过ALB提供的流量镜像功能可以实现在线流量仿真，将在线流量镜像到测试环境的后端服务器，同时ALB自动丢弃镜像后端服务器返回的响应数据，保证镜像后端服务器的测试业务不会影响到线上业务。
[使用](use-alb-to-implement-canary-releases.md)[ALB](use-alb-to-implement-canary-releases.md)[实现灰度发布](use-alb-to-implement-canary-releases.md)：通过配置基于特定条件或不同服务器组流量权重的监听转发规则，将部分请求转发至新版本应用，逐步验证新版本稳定性，实现灰度发布。
该文章对您有帮助吗？
反馈
