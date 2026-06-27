,G,L 的所有记录 | select * from ossobject where _5 in ('N', 'M', 'G', 'L') |
| 返回第 2 列乘以第 3 列比第 5 列大 100 以上的所有记录 | select * from ossobject where _2 * _3 > _5 + 100 |

JSON
假设JSON文件如下：
{ "contacts":[ { "firstName": "John", "lastName": "Smith", "isAlive": true, "age": 27, "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" }, { "type": "mobile", "number": "123 456-7890" } ], "children": [], "spouse": null }，…… #此处省略其他类似的节点 ]}
SQL用例如下：

| 应用场景 | SQL 语句 |
| --- | --- |
| 返回所有 age 是 27 的记录 | select * from ossobject.contacts[*] s where s.age = 27 |
| 返回所有的家庭电话 | select s.number from ossobject.contacts[*].phoneNumbers[*] s where s.type = "home" |
| 返回所有单身的记录 | select * from ossobject s where s.spouse is null |
| 返回所有没有孩子的记录 | select * from ossobject s where s.children[0] is null 说明 目前没有专用的空数组的表示方法，用以上语句代替。 |
