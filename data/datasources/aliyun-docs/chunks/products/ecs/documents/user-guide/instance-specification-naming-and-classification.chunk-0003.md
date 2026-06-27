## 实例规格命名说明
实例规格族名称格式为ecs.<规格族>，实例规格名称为ecs.<规格族>.<规格大小>。具体命名规则说明如下所示：
ecs：云服务器ECS的产品代号。
<规格族>：由规格族主体+规格族后缀组成。
<规格大小>：由small、large或<nx>large组成，表示vCPU核数。small表示1 vCPU，large表示2 vCPU，xlarge表示4 vCPU。<n>中的n越大，表示vCPU核数越多，如2xlarge代表2 * 4 = 8 vCPU，3xlarge代表3 * 4 = 12 vCPU等等，以此类推。
