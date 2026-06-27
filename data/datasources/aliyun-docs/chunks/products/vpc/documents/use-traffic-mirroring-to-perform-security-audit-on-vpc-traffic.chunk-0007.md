### 步骤五：告警验证
登录ECS1，执行curl http://testmynids.org/uid/index.html命令，模仿ID命令的输出，以触发警报。
curl http://testmynids.org/uid/index.html uid=0(root) gid=0(root) groups=0(root)
Suricata规则集中包含如下规则，当数据包的内容具有字符串值uid=0|28|root|29|并且流量被分类为未知流量时，将丢弃数据包并生成警报。
alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root"; content:"uid=0|28|root|29|"; classtype:bad-unknown; sid:2100498; rev:7; metadata:created_at 2010_09_23, updated_at 2010_09_23;)
在Kibana页面，添加GPL筛选条件，即可查看匹配到Suricata IDS特征规则“GPL ATTACK_RESPONSE id check returned root”的告警事件。在 Kibana 日志检索界面搜索关键词GPL，可查看到一条 Suricata IDS 告警命中记录。展开日志详情，event_type为alert，源 IP 为18.155.192.120，目的 IP 为192.168.0.201，协议为 TCP（源端口 80，目的端口 57978），signature为GPL ATTACK_RESPONSE id check returned root，category为Potentially Bad Traffic，severity 为 2，表明告警已成功触发。
