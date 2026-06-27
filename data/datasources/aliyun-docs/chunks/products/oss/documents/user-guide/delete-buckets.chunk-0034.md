### 删除时提示“权限不足”怎么办？
删除Bucket前需先清理内部资源，清理过程中涉及列举（list）和删除（delete）等多项权限，建议联系管理员一次性为您的RAM身份授予[AliyunOSSFullAccess](https://ram.console.aliyun.com/policies/detail?policyType=System&policyName=AliyunOSSFullAccess)权限，避免因权限点遗漏导致删除失败。
