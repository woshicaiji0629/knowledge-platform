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
- 阿里云官方文档采集、清洗、切块和索引脚本
- 文档模型、切块器、向量库抽象和 Qdrant 实现
- 会话管理、上下文消息存储骨架
- 规则型意图识别骨架
- RAG 问答 API，支持真实检索和可配置回答生成
- AI Provider 抽象和阿里云智能客服 Provider 占位实现
- Data Source 抽象与内存数据源示例
- React + TypeScript 问答页面
- 前端 loading、错误态和空输入处理

默认配置不会调用付费模型。设置 `VECTOR_STORE_PROVIDER=qdrant` 后，聊天接口会使用本地 Qdrant 索引和 DashScope embedding 做真实检索；设置 `ANSWER_GENERATOR_PROVIDER=dashscope` 后，会调用 DashScope 文本模型生成回答。

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

RAG 会话问答接口：

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

启用本地 Qdrant 检索和 DashScope 回答生成时，至少配置：

```bash
VECTOR_STORE_PROVIDER=qdrant
ANSWER_GENERATOR_PROVIDER=dashscope
DASHSCOPE_API_KEY=your-api-key
```

运行小规模 RAG 评测：

```bash
cd backend
uv run python -m knowledge_platform.scripts.evaluate_rag --limit 10
```

评测报告默认写入 `runtime-data/evals/`。如只想验证检索和报告生成、不调用文本生成模型，可以加 `--answer-provider skeleton`。

## 后续建议

1. 将会话存储从内存替换为 SQLite 或业务数据库。
2. 增加数据源管理、采集任务状态和索引状态页面。
3. 增加回答质量评测集，对比不同切块、召回和模型配置。
4. 将采集、清洗、切块、入库流程服务化。

详细设计见 [docs/rag-architecture.md](docs/rag-architecture.md)。
