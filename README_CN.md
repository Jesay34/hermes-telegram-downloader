<h1 align="center">Hermes Telegram Downloader</h1>

<p align="center">
<strong>Telegram 媒体下载 + 转发工具，带现代化 Web 管理界面</strong>
</p>

<p align="center">
<a href="https://github.com/MangoIsIllegal/hermes-telegram-downloader/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://github.com/MangoIsIllegal/hermes-telegram-downloader/releases"><img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue"></a>
</p>

<h3 align="center">
  <a href="./README.md">English</a>
  <span> · </span>
  <a href="#features">功能特性</a>
  <span> · </span>
  <a href="#quick-start">快速开始</a>
  <span> · </span>
  <a href="#configuration">配置说明</a>
</h3>

## 概述

基于 [telegram_media_downloader](https://github.com/tangyoha/telegram_media_downloader) 深度改造的 Telegram 媒体下载工具。

支持从 Telegram 频道/群组/个人对话中下载媒体文件（图片、视频、文档等），并提供现代风格的 Web 管理界面进行任务管理。

### 核心功能

- **Telegram 媒体下载** — 支持 audio / document / photo / video / voice / animation 等类型
- **消息转发** — 跨频道/群组的消息转发功能
- **现代化 Web UI** — 重写的浅色主题管理界面，实时任务状态监控
- **任务持久化** — 下载/转发任务持久化存储，崩溃后自动恢复，不丢任务
- **并发控制** — 可配置的最大下载任务数，避免资源耗尽
- **FLOOD_WAIT 智能处理** — 非阻塞式等待，不卡死整个下载队列
- **暂停/恢复** — WebUI 一键暂停/恢复单个任务
- **实时进度通知** — 任务完成/失败时 WebUI 即时更新，通知到 100%
- **OCR 支持** — 集成图片文字提取功能（可选）

### 相比上游的改动

| 改动 | 说明 |
|------|------|
| **版本号** | 从 v2.2.6 改为 v1.0.0（独立版本线） |
| **Web UI 重写** | 移除 layui，现代浅色主题，响应式设计 |
| **任务持久化** | 新增 task_store.py，任务持久化 + 崩溃恢复 |
| **任务 ID 格式** | 改为 MMDD-序号 格式（如 0531-1），更直观 |
| **并发优化** | FLOOD_WAIT 非阻塞处理，不阻塞队列 |
| **暂停/恢复** | WebUI 新增任务暂停/恢复功能 |
| **日志拆分** | tdl.log + download.log 分离，保留 30 天 |
| **跳过检测修复** | 文件大小 >= 95% 即判定为已跳过 |
| **端口变更** | 默认端口从 5000 改为 15555 |
| **本地开发模式** | 新增 run_local.py，独立 Mock 调试 |
| **精简代码库** | 移除测试文件、多余 CI 配置、捐赠二维码等 |
| **OCR 集成** | 接入 PaddleOCR / Qwen-VL 图片文字提取 |

## Quick Start

### Docker 部署（推荐）

```bash
git clone https://github.com/MangoIsIllegal/hermes-telegram-downloader.git
cd hermes-telegram-downloader

cp config.yaml.example config.yaml
# 编辑 config.yaml，填入 api_id / api_hash / chat_id

# 首次运行（前台登录 Telegram）
docker-compose run --rm telegram_media_downloader

# 后续后台运行
docker-compose up -d
```

### 手动安装

```bash
git clone https://github.com/MangoIsIllegal/hermes-telegram-downloader.git
cd hermes-telegram-downloader
pip install -r requirements.txt

cp config.yaml.example config.yaml
# 编辑配置...

python media_downloader.py
```

### 本地开发模式

```bash
# 无需 Telegram 账号，直接启动 WebUI
python run_local.py
# 访问 http://localhost:15555
```

## 配置说明

### 基础配置

| 参数 | 说明 |
|------|------|
| api_id / api_hash | Telegram API 密钥（从 my.telegram.org 获取） |
| chat.chat_id | 要下载的频道/群组 ID |
| media_types | 下载的媒体类型列表 |
| save_path | 文件保存路径 |
| web_port | Web 管理界面端口（默认 15555） |

详细配置参考 [config.yaml.example](./config.yaml.example) 和原项目 [wiki](https://github.com/tangyoha/telegram_media_downloader/wiki)。

## License

[MIT](./LICENSE)

## 致谢

- 原项目：[tangyoha/telegram_media_downloader](https://github.com/tangyoha/telegram_media_downloader)