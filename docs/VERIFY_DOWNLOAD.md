# 校验下载文件

校验 SHA-256 可以确认下载文件与 Yelor Studio 发布的公开清单一致。校验值不一致时，请删除文件并从本仓库 Release 重新下载。

## Windows PowerShell

在下载目录打开 PowerShell：

```powershell
(Get-FileHash -Algorithm SHA256 -LiteralPath ".\Yelor-Launcher-0.1.4.exe").Hash
```

或使用仓库脚本：

```powershell
.\tools\verify-release.ps1 `
  -File ".\Yelor-Launcher-0.1.4.exe" `
  -ExpectedSha256 "69092AB7C3D198B076F4A411603E337487C7CAE189D1BE4CDDF7959C593E41C9"
```

## macOS

```sh
shasum -a 256 Yelor-Launcher-0.1.4-macos-arm64.dmg
```

或使用仓库脚本：

```sh
./tools/verify-release.sh \
  ./Yelor-Launcher-0.1.4-macos-arm64.dmg \
  2AC7E2ADC22F773E77DF22F7809F44C6C43D0CE15592D14FA0C50ABDFD6F7C55
```

## 0.1.4 Public Preview 校验值

完整清单位于仓库根目录的 [`SHA256SUMS.txt`](../SHA256SUMS.txt)，机器可读信息位于 [`release-manifest.json`](../release-manifest.json)。两处记录应保持一致。

不要使用第三方转载页面提供的校验值，也不要只根据文件名判断安装包是否可信。
