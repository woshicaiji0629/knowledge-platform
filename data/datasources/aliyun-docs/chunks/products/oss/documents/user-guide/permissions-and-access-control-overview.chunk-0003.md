### ACL
ACL（访问控制列表）通过预定义的权限等级控制资源的公开或私有状态，是最简单的权限控制方式。
[Bucket ACL](bucket-acl-2.md)控制存储空间的默认访问权限，[Object ACL](object-acl.md)控制单个对象的权限（优先级更高），Object ACL未指定时默认继承Bucket ACL。支持以下权限等级：

| 权限等级 | 效果 |
| --- | --- |
| 私有（private） | 数据私有，仅资源拥有者或被授权用户可访问 |
| 公共读（public-read） | 任何人可读取，仅资源拥有者或被授权用户可写入 |
| 公共读写（public-read-write） | 任何人可公开读取和写入 |

ACL仅支持预定义等级，无法指定授权对象或条件限制。如需精细控制，请使用Bucket Policy或RAM Policy。
