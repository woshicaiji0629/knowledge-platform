## 方案介绍
工作流集群构建CI Pipeline时，主要使用[BuildKit](https://github.com/moby/buildkit)实现容器镜像的构建和推送，并使用[BuildKit Cache](https://github.com/moby/buildkit?tab=readme-ov-file#cache)加速镜像的构建。使用NAS存储Go mod cache，可加速go test和go build运行过程，最终大幅加速CI Pipeline的流程。
