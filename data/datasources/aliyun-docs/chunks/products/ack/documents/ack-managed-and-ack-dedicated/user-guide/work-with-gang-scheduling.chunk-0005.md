### 声明GangGroup
使用Gang scheduling时，部分任务可能存在多种不同角色，例如PyTorch任务中的PS与Worker，这些角色对min-available的需求可能存在差异。使用单一的PodGroup时可能导致多个角色各自的min-available无法得到满足，使用多个PodGroup时又会导致整体失去Gang的保证。此情况下推荐您使用GangGroup功能，该功能允许您将多个Gang合并为一组。调度器在进行调度时只在多个Gang的min-available条件均满足时允许任务执行，保证任务的多个角色均满足min-available特性。
当您使用Label方式时，可以在Pod上使用以下Label。
pod-group.scheduling.sigs.k8s.io/groups: "[\"default/gang-example1\", \"default/gang-example2\"]"
当您使用PodGroup方式时，可以在PodGroup自定义资源上使用以下Label。
pod-group.scheduling.sigs.k8s.io/groups: "[\"default/gang-example1\", \"default/gang-example2\"]"
当您使用Annotation方式时，可以在Pod上使用以下Annotation。
gang.scheduling.koordinator.sh/groups: "[\"default/gang-example1\", \"default/gang-example2\"]"
