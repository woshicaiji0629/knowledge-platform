## 定位Project来源
日志服务与其他云产品关联时，可能会自动创建Project。当Project数量较多时，您可能会希望进行Project溯源，了解各个Project来源，保存的数据内容，费用等信息。
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域查看目标Project。
可通过云产品标记或注释列查看Project创建来源说明：
若Project名称前有图标，可将鼠标移至图标处，会显示该Project关联的云产品名称。
若注释列中包含内容，描述了Project的来源。
若不符合上述两种情况，说明该Project是由用户自行手动创建。
系统自动创建的默认 Project 类型
部分 Project 是由系统或其他云产品自动创建的，用于支撑特定云服务功能。此类 Project 通常有固定的命名规则和用途，常见类型包括：
云监控元数据 Project：名称格式为aliyun-metadata-{用户ID}-{地域ID}，由云监控（Cloud Monitor Service，CMS）2.0 自动创建，用于存储云监控元数据等信息。此类 Project 免费且不产生费用。如需删除，目前仅支持通过云命令行（CloudShell）执行删除命令，控制台操作可能受限。
其他云产品自动创建的 Project：
应用实时监控服务（ARMS）：自动创建 Project 用于存储链路追踪数据。
操作审计（ActionTrail）：自动创建 Project 用于存储操作日志。
日志审计服务（Log Audit Service）：自动创建区域级或中心化的 Project 用于集中管理日志。
当明确Project关联的云产品后，若想了解更多信息，如存储的数据内容等，请参考[云产品日志采集](collection-of-alibaba-cloud-service-logs.md)。
判断 Project 是否正在使用：建议检查关联云产品（如云防火墙、WAF 等）是否仍在运行。若 Project 基础信息中无数据，且 Logtail 配置中无数据，可能暂无业务关联。但删除前务必确认对应云产品不再需要日志服务。若云产品仍在使用中，关联云产品从而自动创建的Project不建议删除。
若希望分析Project的资源用量与计费，可以参考[使用](use-cloudlens-for-sls-to-analyze-resource-usage.md)[CloudLens for SLS](use-cloudlens-for-sls-to-analyze-resource-usage.md)[分析资源用量](use-cloudlens-for-sls-to-analyze-resource-usage.md)进行查看与预估。
