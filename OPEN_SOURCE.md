# 开放范围

Yelor Launcher 采用“发行资料与通用工具开放、核心产品代码保留”的发布方式。

## 本仓库开放的内容

- 玩家可下载的公开预览制品。
- SHA-256 校验清单和机器可读发布清单。
- 不包含 Yelor 业务逻辑的通用文件校验脚本。
- 安装、排错和公开版本说明。
- GitHub Issue 模板。

`tools/` 下的通用校验脚本使用 MIT License，详见 [`tools/LICENSE`](tools/LICENSE)。文档允许在保留来源的情况下引用。

## 不开放的内容

- Launcher 的完整 Vue、Tauri 与 Rust 产品实现。
- Microsoft、Yelor 账号和凭据保护实现细节。
- 更新签名、Apple 公证、生产发布和服务端部署基础设施。
- Yelor Web、管理后台、数据库与生产安全配置。
- 密钥、证书、Token、生产环境变量、玩家资料和日志。

公开仓库不构成对 Yelor 品牌、Logo、视觉资产或完整产品源码的再授权。
