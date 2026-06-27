## 方式二：手动下载安装
从[GitHub Release](https://github.com/aliyun/alibabacloud-aiops-skills/releases/tag/alibabacloud-sls-query-0.0.1)下载 alibabacloud-sls-query 安装包，解压后将文件复制到对应 Agent 的 skills 安装目录中。
复制完成后，确保 skills 目录下存在alibabacloud-sls-query目录，然后重启 Agent 以加载该 Skill。
常见 Agent 的 skills 安装目录如下：

| Agent | 项目级安装目录 | 用户级安装目录 |
| --- | --- | --- |
| Claude Code | .claude/skills | ~/.claude/skills |
| Codex | .agents/skills | ~/.agents/skills |
| Qoder | .qoder/skills | ~/.qoder/skills |
| QwenCode | .qwen/skills | ~/.qwen/skills |
| OpenClaw | .openclaw/skills | ~/.openclaw/skills |
