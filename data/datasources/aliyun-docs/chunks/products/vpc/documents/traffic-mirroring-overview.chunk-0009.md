### API
创建流量镜像初次使用时，需调用[OpenTrafficMirrorService](developer-reference/api-vpc-2016-04-28-opentrafficmirrorservice.md)开通流量镜像功能。
调用[CreateTrafficMirrorFilter](developer-reference/api-vpc-2016-04-28-createtrafficmirrorfilter.md)创建流量镜像筛选条件。
调用[CreateTrafficMirrorFilterRules](developer-reference/api-vpc-2016-04-28-createtrafficmirrorfilterrules.md)创建筛选条件的入方向或出方向规则。
调用[CreateTrafficMirrorSession](developer-reference/api-vpc-2016-04-28-createtrafficmirrorsession.md)创建镜像会话。
调用[UpdateTrafficMirrorSessionAttribute](developer-reference/api-vpc-2016-04-28-updatetrafficmirrorsessionattribute.md)调整Enabled为true，启动镜像会话。
变更流量镜像
调用[AddSourcesToTrafficMirrorSession](developer-reference/api-vpc-2016-04-28-addsourcestotrafficmirrorsession.md)/[RemoveSourcesFromTrafficMirrorSession](developer-reference/api-vpc-2016-04-28-removesourcesfromtrafficmirrorsession.md)为镜像会话增加/删除镜像源。
调用[UpdateTrafficMirrorSessionAttribute](developer-reference/api-vpc-2016-04-28-updatetrafficmirrorsessionattribute.md)修改镜像会话的配置或变更镜像目的、筛选条件。
修改/删除筛选条件
调用[CreateTrafficMirrorFilterRules](developer-reference/api-vpc-2016-04-28-createtrafficmirrorfilterrules.md)创建筛选条件的入方向或出方向规则。
调用[DeleteTrafficMirrorFilterRules](developer-reference/a
