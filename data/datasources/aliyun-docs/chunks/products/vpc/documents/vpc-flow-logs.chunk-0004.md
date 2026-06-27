### API
创建流日志前，请确保已开通流日志功能，且已在日志服务产品中创建了Project和Logstore：
调用[OpenFlowLogService](developer-reference/api-vpc-2016-04-28-openflowlogservice.md)开通流日志功能。
调用[CreateProject](../../sls/documents/developer-reference/api-sls-2020-12-30-createproject.md)创建Project，调用[CreateLogStore](../../sls/documents/developer-reference/api-sls-2020-12-30-createlogstore.md)创建Logstore。
确保满足上述条件后，您可以：
调用[CreateFlowLog](developer-reference/api-vpc-2016-04-28-createflowlog.md)创建流日志，可选调用[CreateIndex](../../sls/documents/developer-reference/api-sls-2020-12-30-createindex.md)创建索引。
调用[DeactiveFlowLog](developer-reference/api-vpc-2016-04-28-deactiveflowlog.md)停止流日志。
调用[ActiveFlowLog](developer-reference/api-vpc-2016-04-28-activeflowlog.md)启动流日志。
调用[DeleteFlowLog](developer-reference/api-vpc-2016-04-28-deleteflowlog.md)删除流日志。
