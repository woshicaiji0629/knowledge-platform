## 授权策略语法
Bucket Policy、RAM Policy、Control Policy和AP Policy均使用JSON格式定义，核心元素包括：

| 元素 | 说明 |
| --- | --- |
| Effect | 授权效果： Allow 或 Deny |
| Principal | 授权对象（RAM Policy 和 Control Policy 不需要） |
| Action | 授权操作，如 oss:GetObject |
| Resource | 授权资源范围 |
| Condition | 生效条件（可选） |

完整的语法说明和Action列表请参见[授权语法与元素](authorization-syntax-and-elements.md)。
