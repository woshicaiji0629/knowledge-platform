### DAG工作流（MapReduce）
真实的批处理场景中，往往需要多个Job配合完成，所以需要指定Job间的依赖关系，DAG是指定依赖关系的最佳方式。
但主流的Batch批处理系统，需要通过Job ID指定Job依赖，由于Job ID需要在Job提交后才能获取，因此需要编写脚本实现Job间依赖（伪代码如下），Job较多时，依赖关系不够直观，维护成本较高。
//Batch批处理系统Job间依赖，JobB依赖JobA，在JobA完成后运行。 batch submit JobA | get job-id batch submit JobB --dependency job-id (JobA)
Argo工作流可以通过DAG定义子任务之间的依赖关系，示例如下：
Task B和Task C依赖Task A运行
Task D依赖Task B和Task C运行
