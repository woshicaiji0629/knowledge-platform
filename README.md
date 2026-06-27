# Knowledge Platform

前后端分离的 AI 项目骨架。当前目标是先接入阿里云智能客服能力，后续保留扩展其他数据源和服务 Provider 的空间。

## 目录结构

```text
backend/              Python + FastAPI 后端
  src/knowledge_platform/
    api/              HTTP API 路由
    config/           应用配置
    datasources/      数据源抽象与实现
    providers/        外部 AI/云服务 Provider
    services/         业务编排层
frontend/             React + TypeScript 前端
  src/
    api/              后端 API 调用
    App.tsx           客服对话页面
```

## 当前范围

- 后端 FastAPI 应用入口
- 后端配置加载与 `.env` 示例
- 阿里云官方文档采集计划骨架
- 文档模型、切块器、向量库抽象
- 会话管理、上下文消息存储骨架
- 规则型意图识别骨架
- RAG 问答 API 骨架
- AI Provider 抽象和阿里云智能客服 Provider 占位实现
- Data Source 抽象与内存数据源示例
- React + TypeScript 问答页面
- 前端 loading、错误态和空输入处理

当前不会真实爬取阿里云文档、调用 embedding/LLM 或写入真实向量数据库。真实采集、文本清洗、embedding、向量库和模型调用需要在确认方案后补充。

## 后端运行

```bash
cd backend
uv sync --extra dev
uv run uvicorn knowledge_platform.main:app --reload
```

健康检查：

```bash
curl http://127.0.0.1:8000/health
```

客服会话占位接口：

```bash
curl -X POST http://127.0.0.1:8000/api/v1/customer-service/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"你好","session_id":"demo-session"}'
```

RAG 会话问答骨架接口：

```bash
curl -X POST http://127.0.0.1:8000/api/v1/chat/sessions/demo-session/messages \
  -H "Content-Type: application/json" \
  -d '{"message":"阿里云智能客服如何配置？"}'
```

阿里云官方文档采集计划接口：

```bash
curl -X POST http://127.0.0.1:8000/api/v1/ingestion/aliyun-docs/plan \
  -H "Content-Type: application/json" \
  -d '{"seed_urls":["https://help.aliyun.com/"],"max_pages":20,"max_depth":1}'
```

后端校验：

```bash
make backend-check
```

## 前端运行

```bash
cd frontend
npm install
npm run dev
```

前端默认请求 `http://127.0.0.1:8000`。如需调整，复制环境变量示例：

```bash
cp .env.example .env
```

前端校验：

```bash
make frontend-check
```

前端构建：

```bash
make frontend-build
```

## 统一命令

```bash
make install-backend
make install-frontend
make check
make test
make build
```

后端依赖使用 `uv` 管理，`make install-backend` 会执行 `uv sync --extra dev`。

## 后端配置

复制后端 `.env.example` 为 `.env`，按实际阿里云产品和接口补齐配置。

```bash
cd backend
cp .env.example .env
```

## 后续建议

1. 确认第一批允许爬取的阿里云官方文档 URL。
2. 确认爬虫频率、robots、缓存和版权边界。
3. 确认 embedding/LLM 供应商。
4. 确认向量数据库选型。
5. 补充真实采集、清洗、切块、入库、检索和回答生成实现。

详细设计见 [docs/rag-architecture.md](docs/rag-architecture.md)。
