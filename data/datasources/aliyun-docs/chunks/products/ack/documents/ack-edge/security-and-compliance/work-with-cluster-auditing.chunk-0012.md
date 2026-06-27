### 示例2：API Server公网访问失败告警
某集群开启了公网访问，为防止恶意攻击，需要监控公网访问的次数以及失败率。当访问次数达到一定阈值（10次）且失败率高于一定阈值（50%）时，告警需要立即被发送，并在告警信息中包含用户的IP所属区域、操作源IP、是否高危IP等信息。
查询语句为：
* | select ip as "源地址", total as "访问次数", round(rate * 100, 2) as "失败率%", failCount as "非法访问次数", CASE when security_check_ip(ip) = 1 then 'yes' else 'no' end as "是否高危IP", ip_to_country(ip) as "国家", ip_to_province(ip) as "省", ip_to_city(ip) as "市", ip_to_provider(ip) as "运营商" from (select CASE WHEN json_array_length(sourceIPs) = 1 then json_format(json_array_get(sourceIPs, 0)) ELSE sourceIPs END as ip, count(1) as total, sum(CASE WHEN "responseStatus.code" < 400 then 0 ELSE 1 END) * 1.0 / count(1) as rate, count_if("responseStatus.code" = 403) as failCount from log group by ip limit 10000) where ip_to_domain(ip) != 'intranet' and ip not LIKE '%,%' ORDER by "访问次数" desc limit 10000
条件表达式为：源地址 =~ ".*"。
