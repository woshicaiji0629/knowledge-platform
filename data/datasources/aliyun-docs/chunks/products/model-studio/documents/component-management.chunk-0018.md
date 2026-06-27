# 示例代码仅供参考，请勿直接在生产环境中使用 # 示例：NGINX负载均衡配置片段 upstream dashscope_app_cluster { server 192.168.1.10:8000; server 192.168.1.11:8000; } server { listen 80; location / { proxy_pass http://dashscope_app_cluster; } }
在后端应用层，您可以运行多个gunicorn或uvicorn进程，每个进程都加载 DashScope SDK，并处理部分请求。
4.2.2 任务排队与异步处理
对于可能触发大模型高负载或长时任务的场景，可以引入消息队列（如 RabbitMQ、Kafka）或异步任务执行器（如 Celery）将用户请求排队或分发给工作进程。此举可以防止瞬时高并发导致服务崩溃，也能提高系统的可观察性和容错率。
