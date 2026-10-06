# 常见问题排查

## Windows 显示未知发布者

当前 `0.1.4 Public Preview` 未签署 Authenticode。请确认文件来自本仓库 Release，并按 [`VERIFY_DOWNLOAD.md`](VERIFY_DOWNLOAD.md) 校验 SHA-256。校验不一致时不要运行。

## 无法创建 `.minecraft` 或游戏目录

1. 将 Launcher 放在当前用户可写的独立文件夹。
2. 不要放入 Windows、Program Files 或其他受保护目录。
3. 重新打开 Launcher，检查设置中的当前游戏目录。
4. 若自动回退仍失败，在 Launcher 中选择一个当前用户可写的目录。

提交问题时请说明失败阶段和目录类型，但不要公开完整用户名路径。

## Java 无法匹配或游戏启动失败

优先使用“自动匹配游戏版本”。Yelor 会按 Minecraft 版本、Loader、Java 主版本和架构选择兼容运行时，不应简单选择电脑上最高版本的 Java。

如果使用自定义 Java，请确认它仍然存在、架构正确，并与目标 Minecraft/Loader 兼容。反馈时提供 Java 主版本即可，不要公开完整本机路径。

## 下载速度显示 `0 B/s`

下载刚开始测量时会短暂显示 `0 B/s`。如果长时间不变化，请检查网络连接、任务阶段和失败提示，再尝试暂停/继续或重新创建任务。

## macOS 阻止打开

当前公测包的 Apple 签名与公证状态尚未独立确认。不要关闭 Gatekeeper、系统完整性保护或执行来源不明的绕过命令。请等待后续正式签名版本，或在 Issue 中提交已脱敏的系统提示截图。

## 提交 Issue

使用 [下载/安装问题模板](https://github.com/Z1urRr/Yelor-Launcher-Downloads/issues/new/choose)，提供平台、版本、文件名、SHA-256 是否匹配、复现步骤和已脱敏错误信息。
