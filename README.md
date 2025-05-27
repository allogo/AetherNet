# AetherNet - 去中心化 AI Agent 分布式算力网络

AetherNet 是一个实验性项目，旨在连接多个本地 Linux 容器或机器，将其算力整合为一个自组织的 AI 网络。每个节点运行一个 AI Agent，可接收任务、协作执行并通过 P2P 网络共享结果。

## 🌐 核心功能

- 本地 AI Agent 容器化部署（Docker + FastAPI）
- 节点发现与 P2P 通信（ZeroMQ / gRPC）
- AI 推理任务（如文本生成）分发与执行
- 可扩展的模块结构与任务插件系统

## 📦 快速开始（本地模式）

```bash
# 安装依赖
pip install -r requirements.txt

# 启动本地 Agent（默认使用CPU）
python api/server.py
```

或使用 Docker：

```bash
docker build -t aether-agent ./docker
docker run -p 8000:8000 aether-agent
```

## 📁 目录结构简述

- `agents/`：Agent 运行逻辑与任务定义
- `api/`：HTTP 控制接口（FastAPI）
- `network/`：P2P 通信模块
- `config/`：配置文件（YAML格式）
- `scripts/`：部署与调试脚本
- `examples/`：任务调用演示脚本

## ✅ TODO

- [ ] 多节点任务协作测试
- [ ] P2P 网络发现机制
- [ ] 模型热加载与本地缓存
- [ ] 安全机制（签名、身份认证）

## 📄 License
MIT