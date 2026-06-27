## 读写分离
实践教程：[体验读写分离](use-read-writing-splitting.md)
简介：如果您的业务是少写多读场景，随着业务的不断发展，主实例会面临越来越大的读请求压力，进而影响到主实例的整体性能。为了解决这个问题，您可以创建只读实例，通过数据库代理实现读写请求自动分发，将读请求分流到只读实例上，降低主实例负载。
涉及功能：[只读实例](../overview-of-read-only-apsaradb-rds-for-mysql-instances.md)、[数据库代理](database-proxy-introduction.md)、[SQL](use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)[洞察和审计](use-the-sql-explorer-and-audit-feature-on-an-apsaradb-rds-for-mysql-instance.md)
