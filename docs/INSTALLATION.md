# 安装 Yelor Launcher

只从本仓库的 [GitHub Releases](https://github.com/Z1urRr/Yelor-Launcher-Downloads/releases) 下载公开版本。下载后先按 [`VERIFY_DOWNLOAD.md`](VERIFY_DOWNLOAD.md) 校验 SHA-256。

## Windows 10 / 11 x64

1. 下载 `Yelor-Launcher-0.1.4.exe`。
2. 将 EXE 放入拥有写入权限的独立文件夹，不要放入 Windows 系统目录。
3. 校验 SHA-256 后运行 Launcher。
4. 第一次进入后检查游戏目录。Launcher 会依次尝试便携目录、系统 Minecraft 目录和用户数据目录。
5. 保持 Java 为“自动匹配游戏版本”，除非你明确知道目标 Minecraft 与 Loader 需要的 Java 范围。

当前公测 EXE 未签署 Authenticode。若 Windows 显示未知发布者，请先核对下载来源和 SHA-256；校验不一致时不要运行。

## macOS Apple Silicon

1. 下载 `Yelor-Launcher-0.1.4-macos-arm64.dmg`。
2. 校验 SHA-256。
3. 打开 DMG，将 Yelor Launcher 拖入“应用程序”。
4. `.app.zip` 仅作为备用手动归档；`.app.tar.gz` 不是首次安装包。

当前公测包的 Apple 签名与公证状态尚未独立确认。不要为运行公测包而关闭 Gatekeeper 或系统完整性保护；无法正常打开时请等待后续正式签名版本。

## 不要混用的文件

- `.dmg`：macOS 首次安装。
- `.app.zip`：macOS 备用手动归档。
- `.app.tar.gz`：Tauri 更新归档，当前缺少公开 updater `.sig`。
- `.exe`：Windows x64 便携版本。
