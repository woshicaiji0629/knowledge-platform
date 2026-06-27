## 异常返回值说明

| 错误信息 | 说明 |
| --- | --- |
| WRONGTYPE Operation against a key holding the wrong kind of value | 对象类型错误：Key 不是 TairRoaring 对象。 |
| ERR bad arguments, must be unsigned 32-bit integer | 参数类型错误：无法按照 32-bit 整型进行转换。 |
| ERR invalid arguments, maybe out of range or illegal | 参数非法： 非 32-bit 整型的 offset 不符合规则。 参数的[start,end]不符合规则。 参数超过 Roaring Bitmap 的元素个数。 |
| ERR key already exist | Roaring Bitmap 对象已存在，且不支持覆盖。 说明 V2.2 版之后将不会产生该报错。 |
| ERR key not found | Roaring Bitmap 对象不存在, 不支持操作。 说明 V2.2 版之后将不会产生该报错。 |

该文章对您有帮助吗？
反馈
