会话级下钻：从高风险会话到完整行为链
典型场景：审计大盘的“高风险会话”列表标记了一个高危 Session，安全团队需要还原该会话的完整交互过程，确认威胁是否属实。
多实例部署环境下，各 OpenClaw 实例的日志集中写入同一 SLS Logstore。自定义探索的第一步是按 Session ID 隔离，将视野收敛到单个会话，明确“谁在何时触发了哪些请求、调用了哪些工具、模型如何响应”，为合规举证提供清晰边界。
登录[日志服务控制台](https://sls.console.aliyun.com/)，在Project列表中选择目标Project。
在日志存储中目标LogStore中通过查询 / 分析进行数据探索，使用* and __tag__:__session_id__:<Session_Id>进行过滤，替换<Session_Id>为真实Session ID。
完成会话过滤后，在原始日志的原始页签下，找到目标日志，单击图标，可进行上下文预览，按原始顺序还原该会话内的完整行为链——用户输入、模型推理、工具调用请求、工具执行结果，先后关系一目了然。这一能力在审计场景中尤为关键：它不仅能帮助识别异常调用顺序（如敏感文件读取紧接外发操作），还为安全事件的复现与证据留存提供了完整的上下文视图。
运行时排障：关键词检索与聚合分析
典型场景：运行指标大盘告警提示错误率突增，需要从海量 Runtime 日志中快速定位故障模块与根因。
SLS 支持全文检索与结构化字段检索的组合，配合时间范围可逐层收敛排查范围。典型的排障路径分为两步——先缩小范围，再量化分布：
第一步：逐层过滤，锁定问题
按日志级别过滤：使用_meta.logLevelName: ERROR or _meta.logLevelName: WARN or _meta.logLevelName: FATAL过滤所有错误与警告日志，将注意力集中到异常事件。
按子系统下钻：在错误日志中叠加字段条件，例如0.subsystem: plugins，则分析语句为(_meta.logLevelName: ERROR or _meta.logLevelName: WARN or _meta.logLevelName: FATAL) and 0.subsystem: plugins，将范围收敛到具体子系统，两步过滤即可快速定位到错误日志。
第二步：SQL 聚合，量化全局分布
关键词筛选定位的是单条事件，而SQL 聚合分析则将单条日志上升为全局统计视图。例如，对subsystem字段做分组聚合，则分析语句为_meta.logLevelName: ERROR or _meta.logLevelName: WARN or _meta.logLevelName: FATAL | select "0.subsystem" as sub
