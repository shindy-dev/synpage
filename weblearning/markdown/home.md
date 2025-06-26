# About WebLearning
『WebLearning』は Webアプリケーションを作成する上で必要な技術を学ぶための初学者向けのアプリケーションになります。  
Webアプリケーション開発の基礎となるHTML/CSS、JavaScript等のドキュメントもご用意しております。  
以降では、『WebLearning』の  

- [アーキテクチャ](#architecture)
- [ホスティングサービス（Render）](#hosting)
- [開発環境](#dev)
- [Webアプリケーションフレームワーク](#framework)

について解説していきます。

---

## アーキテクチャ {#architecture}
『WebLearning』は Dockerを使用したシンプルなDjango製のWebアプリケーションであり、以下のアーキテクチャ図に基づいて構築しています。なお構築、開発、運用において電気代以外の**費用はかかりません**。  

<img src="/static/images/architecture.png" width="600px" >

※セキュリティの観点から、セキュリティについては記載しておりません。

生成AI M365 Copilot から本アーキについて好評いただいております🎉
```
Q.このアーキテクチャ図についての点数付きの評価を5行以内で要約してください。

A. このアーキテクチャ図は、DockerとGitHub Actionsを活用したモダンなWeb開発環境で、
   学習用途として非常に優れています。
   開発・本番環境の分離やCI/CDの導入により、実務に近い体験が可能です。
   セキュリティや運用面の補足があればさらに理想的です。
   評価：92点／100点
```

次章では『WebLearning』で利用しているホスティングサービスについて解説いたします。

---

## ホスティングサービス（[Render](https://render.com/)）<span style='font-size:1rem; font-weight: normal;'>2025/6/23時点</span> {#hosting}

<img src="/static/images/architecture1.png" width="600px" >

Render は軽量な構成のWebアプリを無料で簡単に公開できるクラウド型ホスティングサービス（PaaS:Platform as a Service）です。インフラのことはサービスに委譲できるため、開発者は提供するWebアプリケーションの開発に注力することができます。PaaSの代表例としては、「Microsoft Azure App Service」、「AWS Elastic Beanstalk」、「Google Cloud - Google App Engine」、「Fly.io」などが挙げられます。Renderの採用理由と無料プランにおける特徴を以下に記載します。

### Renderの[無料プラン](https://render.com/docs/free)の特徴
- **クレジットカード登録不要で利用可能**  
無料プラン利用者は課金を心配することなく利用することができます。類似サービスは多数ありますが、『WebLearning』の開発者は心配性な節約家なこともあり、クレジットカード不要で利用できる点でRenderを採用しております。

- **Webサーバ**  
無料プランの場合、「512MB RAM / 0.1 CPU」のサーバを利用できます。また、各ワークスペースにつき月750時間（約31日間）、インスタンスを稼働させられますので、アプリ（インスタンス）1つのみの運用であれば永続的に稼働させることができます。注意点として、15分間アクセスが無いとWebサービスがスピンダウン（スリープ）する制約があります。再度アクティブになるまでは1～3分程度かかるため、サービス停止を防ぐには　bot（外部サービス）などを利用して、定期的にリクエストを送信する等の対応が必要になります。  
[UptimeRobot: Free Website Monitoring Service](https://uptimerobot.com/)

- **「PostgreSQL 16」のマネージドサービス（[Postgres](https://render.com/docs/postgresql)）**  
無料プランの場合、「256 MB RAM / 0.1 CPU / 1 GB Storage」のRDBサーバを利用できます。「PostgreSQL」のバージョンは 13 ～ 16 をサポートしています。注意点として、1つのワークスペースで動かせるデータベースが1つでやることや、無料でアクセスできる期間がデータベース作成後30日間であること等の制約がありますので、無料で本格的に運用する場合は[Neon](https://console.neon.tech/)の利用をおすすめします。  
※AWSのRDSに対応するサービスです。  

- **Dockerコンテナのデプロイ**  
DockerfileによりWebサーバへコンテナをビルドし、コンテナ内のWebアプリケーションをデプロイすることができます。これにより開発環境と本番環境の環境の差を最小限にすることで、環境依存による不具合を予防することができます。  
※AWSのECSに対応するサービスです。  

- **GitHubやGitLabのリポジトリとの連携**  
WebアプリケーションのソースコードやDockerfileを管理しているリポジトリ（可視性は問いません）と対象のブランチを指定することで自動でコンテナとアプリケーションのビルド＆デプロイまで行います。Auto-Deploy機能により、指定したブランチに対し変更があった（pushした）場合に自動で再ビルド＆デプロイを実施することもできます。

- **無料でビルドできる時間が限られている**  
1月毎に無料でビルドできる時間が設けられているため、Auto-Deploy機能がOnの場合、大量のpushにより無料のビルド可能時間を超過すると、最新のアプリケーションをデプロイできなくなります。対応策としては、Auto-Deploy機能をOffにするか、デプロイするブランチとは別のブランチで主な開発を行い、公開したいときにデプロイ対象のブランチにマージする対応が考えられます。

- **SSH接続ができない**  
無料プランではWebサーバへSSH接続ができないため、利用する場合は有料プランに加入する必要があります。また、どうしても無料で利用したい場合は、類似サービスの[Fly.io](https://fly.io/)で代替可能です。（基本機能はRenderと同じで、無料で利用できますが、クレカの登録が必須です。）

次章では『WebLearning』の開発環境について解説いたします。

---

## 開発環境 {#dev}

<img src="/static/images/architecture2.png" width="600px" >

『WebLearning』ではコンテナ型の仮想環境や様々なサービスを用いて開発しているため、事前に準備することが多く、インストールするツールも多いことから、一見複雑そうに感じる方もいるかもしれません。ただ一度構築してしまえば、各種利用サービスの形態が改悪されない限り、高い作業効率でWebアプリケーションの開発やデプロイ等作業が行えると思います。（開発版QOL爆上がりってやつです。）

### 開発用端末
Dockerが利用できればOSは問いませんが、実際に利用していてRAMは8GB以上合った方がいいと思いました。システム要件の詳細は以下を参照してください。  
[Windows に Docker Desktop をインストール — Docker-docs-ja 24.0 ドキュメント](https://docs.docker.jp/desktop/install/windows-install.html#id2)  
[Mac に Docker Desktop をインストール — Docker-docs-ja 24.0 ドキュメント](https://docs.docker.jp/desktop/install/mac-install.html#mac-system-requirements)  
[Linux に Docker Desktop をインストール — Docker-docs-ja 24.0 ドキュメント](https://docs.docker.jp/desktop/install/linux-install.html#desktop-linux-system-requirements)  

### Docker Desktop
Dockerコンテナのビルドを行うために利用します。Dockerアカウントの作成と開発端末へ「Docker Desktop」をインストールする必要があります。  
[Windows | Docker Docs](https://docs.docker.com/desktop/setup/install/windows-install/)  

### Visual Studio Code（任意のテキストエディタ）
コンテナで開発を行う場合、コンテナ内部にテキストエディタをインストールして開発をしても良いのですが、なるべく本番環境で不要なものをコンテナ内部にインストールしたくないことから、ローカルのテキストエディタからのリモート接続によりコンテナ内部のソースコードを編集する開発手法があります。『WebLearning』ではテキストエディタに拡張機能が豊富な「Visual Studio Code」を採用しています。  
[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)  

### Git
プロジェクト内のドキュメントやソースコードをバージョン管理するために利用します。管理単位は「リポジトリ」と呼ばれ、本構成ではリモートリポジトリをGitHub上にホストしています。  
[Git - Gitのインストール](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)  

### （任意）Gitクライアント
Gitの操作をGUIから行うための支援ツールです。「GitHub Desktop」、「SourceTree」、「Gitkraken」、「Visual Studio Codeの拡張機能」等様々なツールがあります。現状『WebLearning』ではGitの基本操作しかしていないためテキストエディタとしても利用している「Visual Studio Codeの拡張機能」を採用しています。

### GitHub  
リモートリポジトリの管理を行うためのサービスです。多くのOSS（Open Source Software）をGitHubで管理・公開しています。またリポジトリ管理以外にも「GitHub Packages」と呼ばれるコンテナイメージ等をパッケージ管理するサービスや、「GitHub Actions」と呼ばれるリポジトリに対して変更があった場合に、必要な作業を自動化するサービスがあり、『WebLearning』では 「リポジトリ内のDockerfile等コンテナに関わるファイルに対し変更があった場合に自動でコンテナイメージをビルドする」トリガーを「GitHub Actions」に設定し、「GitHub Packages」で管理しているコンテナイメージを自動更新するといったワークフローを採用しています。  
[GitHub Japan | GitHub](https://github.co.jp/)  

### PostgreSQL 16
オープンソースなリレーショナルデータベース管理システム（RDBMS）です。高性能でありながら商用利用可能な点で人気なようです。DjangoはORM（Object-Relational Mapping）設計のため、簡単なWebアプリケーションであれば、複雑なSQLを組む必要がないのでRDBMSは何でも良いのですが、先述のRenderのサービス「Postgres」を使用できるため採用しています。  
[PostgreSQL: The world's most advanced open source database](https://www.postgresql.org/)

### Dockerfile  
Dockerコンテナの設計図（上の図ではDebian系のLinuxを採用）  
作成したコンテナは開発および実環境で使用する。Render等ホスティングサービスにデプロイする際はコンテナ作成後、自動でサービスが開始できるようEntrypointを記載すること。  
[Docker のベストプラクティス: RUN、CMD、および ENTRYPOINT の選択 | Docker](https://www.docker.com/ja-jp/blog/docker-best-practices-choosing-between-run-cmd-and-entrypoint/)
　
### 環境設定ファイル（ .envファイル ）
開発者によって異なる情報や非公開情報を記載することで  
コンテナ作成時、コンテナ内部に環境変数として保持してくれる。  
※必ずgitの監視対象から外す（ .gitignoreに記載する ）こと  
    - GitHubアカウントのユーザー/メールアドレス
    - Database接続情報
    - アプリケーション公開用秘密鍵　…　等々  
  
    ※実環境へはRenderのGUIから設定する

### ソースコード  
Webアプリケーションフレームワークや実行するプログラムのソースコード  
上の図ではWebアプリケーションフレームワークにDjangoを採用）

### データベース（上の図ではRenderで無料で利用可能なPostgreSQLを採用）  
今回はユーザー管理、セッション管理、アプリケーションデータベースとして使用  


⇒ソースコードとDockerfileをGitHubでリポジトリとして管理し、Renderに設定することで、  
　push（ソースコードやDockerfileを編集）した  
　ときに自動でRenderにデプロイまでしてくれる。

今回構成の元となるリポジトリ：[GitHub | synpage](https://github.com/shindy-dev/synpage)

---

## Webアプリケーションフレームワーク {#framework}
Pythonが好きなのと将来的にフルスタック開発ができるようになりたいという筆者の思いからDjangoを採用  
[Django documentation](https://docs.djangoproject.com/ja/5.2/)



