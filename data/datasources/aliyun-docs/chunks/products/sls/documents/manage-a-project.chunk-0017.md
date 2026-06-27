## API
首先使用[配置传输加速](developer-reference/api-sls-2020-12-30-putprojecttransferacceleration.md)。
在后续使用时将endpoint配置为传输加速域名才能获得加速效果。传输加速域名仅支持HTTP/HTTPS协议的API接入，暂不支持Kafka、GRPC等协议接入。在不需要传输加速的场景中，建议使用[服务接入点](developer-reference/api-sls-2020-12-30-endpoint.md)以减少传输费用。
/** * 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 */String accessId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"); String accessKey = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"); /** * 日志服务的服务接入点，使用传输加速域名。 */String endpoint = "log-global.aliyuncs.com"; /** * 创建日志服务Client。 */static Client client = new Client(host, accessId, accessKey);
