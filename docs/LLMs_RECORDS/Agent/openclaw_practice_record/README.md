# OpenClaw使用流程

## Reference

- https://docs.openclaw.ai/install/docker
- https://dev.to/bdougieyo/setting-up-openclaw-on-exedev-with-discord-27n

## 租服务器

1. 在[vast.ai](https://cloud.vast.ai/create/)选择一张RTX2080 Ti

2. 模板选择Ubuntu 22.04 VM，磁盘大小选择 100G

3. 进入容器，安装openclaw

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

4. 选择`openrouter`的模型，选择`discord`作为channel

5. 添加`bot key`，[方法](https://www.youtube.com/watch?v=u22_aE1Bbt8)

## openclaw 和 claude code 互相对话配置

