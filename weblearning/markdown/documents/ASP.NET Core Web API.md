# ASP.NET Core Web API

## はじめに
本ページではWebAPIについて、ASP.NETを使って解説していく

## 文献
[チュートリアル: ASP.NET Core を使って最小 API を作成する](https://learn.microsoft.com/ja-jp/aspnet/core/tutorials/min-web-api?view=aspnetcore-8.0&tabs=visual-studio-code)


## 準備
Visual StudioであればGUIで完結できるが、Macで開発しているので、.NET CLI+VS Codeを使って開発を行う（Visual Studio for Macは2024年8月にサポート終了）

### VS Code
公式ページからインストーラーをダウンロードしてインストールするか、brewが導入済みであれば以下のコマンドでインストールする

```bash
brew install --cask visual-studio-code
```

### .NET8 SDK
brewだと公式で提供されているものが.NET9しかなかったため、公式サイトからインストーラーをダウンロードし、インストール。以下のコマンドでインストール先が確認できる
```bash
% dotnet --list-sdks
8.0.411 [/usr/local/share/dotnet/sdk]
```
何らかの理由でアンインストールする場合は[アンインストールツール](https://learn.microsoft.com/ja-jp/dotnet/core/additional-tools/uninstall-tool-overview?pivots=os-macos)があるので、そちらを利用するのが確実（公式サイトに手動でアンインストールする方法も掲載されている）

## dotnetコマンド
今回はCLIからdotnetコマンドを使用してプロジェクト管理をしていくため、よく使うオプションを以下に記載する

### メモ

```bash
dotnet tool install --global dotnet-ef

mkdir SynNet
cd SynNet
dotnet new webapi -o SynNet.API
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet add package Microsoft.EntityFrameworkCore.Tools
code .
dotnet new xunit -o SynNet.API.Tests
dotnet sln add SynNet.API.Tests
dotnet add package Microsoft.AspNetCore.Mvc.Testing --version 8.0.17
dotnet add package FluentAssertion

# Modelが定義できたらマイグレーション
dotnet ef migrations add InitialCreate
dotnet ef database update

```