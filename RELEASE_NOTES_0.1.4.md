# Yelor Launcher 0.1.4 Public Preview

这是面向玩家的 Windows x64 与 Apple Silicon macOS 公测候选版本。

## 下载

- Windows：`Yelor-Launcher-0.1.4.exe`
- macOS 首次安装：`Yelor-Launcher-0.1.4-macos-arm64.dmg`
- macOS 备用归档：`Yelor-Launcher-0.1.4-macos-arm64.app.zip`
- macOS Tauri 归档：`Yelor-Launcher-0.1.4-macos-arm64.app.tar.gz`

## 本次重点

- 下载任务显示真实字节进度与下载速度。
- 修复首次启动游戏目录创建和可写目录回退。
- Java 自动选择按照 Minecraft 版本与 Loader 兼容范围匹配。
- 修复 Steve / Alex 默认皮肤及皮肤页面流畅度。
- 修复主题色、Java 长路径与收藏图标状态。

## 发布状态

- Windows EXE 未签署 Authenticode，Windows 可能显示未知发布者提示。
- macOS 包为 Apple Silicon 构建；签名与 Apple 公证状态尚未在本仓库完成独立确认。
- `.app.tar.gz` 没有配套公开 updater `.sig`，不能作为正式自动更新制品。

本 Release 标记为 **Pre-release / Public Preview**，不表示已完成所有生产账号与在线更新联调。

## SHA-256

```text
69092AB7C3D198B076F4A411603E337487C7CAE189D1BE4CDDF7959C593E41C9  Yelor-Launcher-0.1.4.exe
2AC7E2ADC22F773E77DF22F7809F44C6C43D0CE15592D14FA0C50ABDFD6F7C55  Yelor-Launcher-0.1.4-macos-arm64.dmg
40CE1A71DCA6513F2062A2BB171D8C37CE8A209EEF83A56F89DBDB4D25C9F34C  Yelor-Launcher-0.1.4-macos-arm64.app.zip
C64FD77B5E4F6C1C400BA04974D1A04A53EC279F02E549A13D4E005C2EADF4B9  Yelor-Launcher-0.1.4-macos-arm64.app.tar.gz
```
