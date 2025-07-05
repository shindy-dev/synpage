# About WebLearning
『WebLearning』は **Webアプリケーションを作成する上で必要な技術を学ぶための初学者向けのアプリケーション**になります。Webアプリケーション開発の基礎となる「HTML/CSS」、「JavaScript」等のドキュメントもご用意しております。  


なお『WebLearning』は OSS（Open Source Software）であり、GitHubでソースコードを公開しています。  
ソースコード：[GitHub | synpage](https://github.com/shindy-dev/synpage)


以降では、『WebLearning』の  

- [アーキテクチャ](#architecture)
- [ホスティングサービス](#hosting)
- [マネージドRDBサービス](#rdb)
- [開発環境](#dev)
- [Webアプリケーションフレームワーク](#framework)
- [ディレクトリ構造](#dir)

について解説していきます。

PCがあれば 「誰でも」、「簡単に」、「無料で」構築できる構成ですので、興味のある方はぜひご一読ください。（といいつつも具体的な手順は記載しておりませんので、各自で調査いただけますとより、理解が深まると思います。）

---

## アーキテクチャ {#architecture}
『WebLearning』は 「Docker」を使用した**シンプルなDjango製のWebアプリケーション**であり、以下のアーキテクチャ図に基づいて構築しています。なお構築、開発、運用においてPC、電気代以外の**費用はかかりません**🎉  

<figure>
  <img src="/static/images/architecture.png" alt="アーキテクチャ図 - 全体" width="1000px" >
  <figcaption>アーキテクチャ図</figcaption>
</figure>

Microsoft製の生成AI「M365 Copilot」から本アーキテクチャ図について、ほどほどの評価をいただいております🎉  
※セキュリティの観点から、セキュリティについてはアーキテクチャ図内に記載しておりません。
```
Q.  このアーキテクチャ図についての点数（100点満点）付きの評価を5行以内で要約してください。

A.  評価（100点満点）: 85点
    要約（5行以内）:

    デプロイメントフローが明確で、GitHubからRenderまでの流れが整理されている。
    開発環境の多様性（Windows, macOS, Ubuntu）とDocker活用が好印象。
    本番環境とデータベースの連携も明示されており、実用性が高い。
    ただし、セキュリティやCI/CDの詳細が省略されている点が惜しい。
    全体としては、実践的で理解しやすい構成。
```

次章では『WebLearning』で利用しているホスティングサービスについて解説いたします。

---

## ホスティングサービス {#hosting}

<img src="/static/images/logo/Render_logo_Black.svg" alt="Render_logo" width="380px" style="background-color:#FFFFFF;">

<figure>
  <img src="/static/images/architecture1.png" alt="アーキテクチャ図 - 本番環境" width="1000px" >
  <figcaption>アーキテクチャ図 - 本番環境</figcaption>
</figure>

**「[Render](https://render.com/)」は軽量な構成のWebアプリを無料で簡単に公開できるクラウドホスティングサービス（PaaS:Platform as a Service）**です。インフラのことはサービスに委譲できるため、開発者は提供するWebアプリケーションの開発に注力することができます。PaaSの代表例としては、「Microsoft Azure App Service」、「AWS Elastic Beanstalk」、「Google Cloud - Google App Engine」、「Fly.io」などが挙げられます。「Render」の採用理由と無料プランにおける特徴を以下に記載します。(2025/6/23時点の情報です。)  

### Renderの[無料プラン](https://render.com/docs/free)の特徴
- **クレジットカード登録不要で利用可能**  
無料プラン利用者は課金を心配することなく利用することができます。類似サービスは多数ありますが、『WebLearning』の開発者は節約家なこともあり、**クレジットカード不要で利用できる点**で「Render」を採用しております。

- **Webサーバ**  
無料プランの場合、**「512MB RAM / 0.1 CPU」**のサーバを利用できます。また、各ワークスペースにつき月750時間（約31日間）、インスタンスを稼働させられますので、アプリ（インスタンス）1つのみの運用であれば永続的に稼働させることができます。注意点として、**15分間アクセスが無いとWebサービスがスピンダウン（スリープ）する制約**があります。再度アクティブになるまでは1～3分程度かかるため、サービス停止を防ぐには　bot（外部サービス）などを利用して、定期的にリクエストを送信する等の対応が必要になります。  
[UptimeRobot: Free Website Monitoring Service](https://uptimerobot.com/)

- **「PostgreSQL」のマネージドサービス（[Postgres](https://render.com/docs/postgresql)）**  
無料プランの場合、**「256 MB RAM / 0.1 CPU / 1 GB Storage」**のRDBサーバを利用できます。「PostgreSQL」のバージョンは 13 ～ 16 をサポートしています。注意点として、**1つのワークスペースで動かせるデータベースが1つでやることや、無料でアクセスできる期間がデータベース作成後30日間であること等の制約**がありますので、無料で本格的に運用する場合は「[Neon](https://console.neon.tech/)」の利用をおすすめします。こちらも無料（クレカ登録不要）で利用できるマネージドなRDBサービスとなっており、『WebLearning』でも本番環境、開発環境共に「Neon」を利用しております。  
※AWSのRDSに対応するサービスです。  

- **Dockerコンテナごとデプロイ**  
Webアプリケーション開発では、コンテナという仮想環境を用いて開発することがあります。「VirtualBox」や「Hyper-V」等の仮想環境は通常、仮想マシン毎にOSを導入する必要がありますが、コンテナはホストOS上で動く仮想環境のため、より軽量で高速な仮想環境を構築することができます。「Docker」はコンテナのマネジメントサービスの一つです。**「Render」では「Dockerfile」（Dockerイメージ（コンテナの設計図）の作成手順書）を基に、Dockerイメージをビルドし、Webサーバ内で開発環境と同等のコンテナを実行することができます。**コンテナの利用により、本番環境と開発環境の環境の差を最小限にすることで、環境依存による不具合を予防することができます。コンテナ起動時にコンテナ内部に格納したアプリケーションを起動するように設定しておけば、すぐにサービスを開始することができるわけです。  
※AWSのECSに対応するサービスです。

- **GitHubやGitLabのリポジトリとの連携**  
Webアプリケーションのソースコードや「Dockerfile」を管理している**リポジトリ（public/privateのリポジトリの可視性は問いません）と対象のブランチを指定することで自動でコンテナとアプリケーションのビルド＆デプロイまで行います。**「Auto-Deploy」機能により、指定したブランチに対し変更があった（pushした）場合や、変更後「GitHub」や「GitLab」で設定しているCI/CDが完了した場合に自動で再ビルド＆デプロイを実施することもできます。

- **無料でビルドできる時間が限られている**  
1月毎に無料でビルドできる時間500分までとなっているため、「Auto-Deploy」機能がOnの場合、大量のpushにより**無料のビルド可能時間を超過すると、最新のアプリケーションをデプロイできなくなります。**対応策としては、「Auto-Deploy」機能をOffにするか、デプロイするブランチとは別のブランチで主な開発を行い、公開したいときにデプロイ対象のブランチにマージする対応が考えられます。

- **SSH接続ができない**  
無料プランでは**WebサーバへSSH接続ができない**ため、利用する場合は有料プランに加入する必要があります。（ログの確認はできます。）また、どうしても無料で利用したい場合は、類似サービスの「[Fly.io](https://fly.io/)」で代替可能です。（基本機能は「Render」と同等で、無料で利用できますが、クレカの登録が必須です。）

次章では『WebLearning』で利用しているマネージドRDBサービスについて解説いたします。

---

## マネージドRDBサービス {#rdb}

<img src="/static/images/logo/neon_logo_color.svg" alt="neon_logo" width="380px" style="background-color:#FFFFFF;">

「[Neon](https://console.neon.tech/)」は**サーバーレスなPostgresデータベースを提供するDBaaS（Database as a Service）**です。「Neon」の特徴として、ブランチ機能が挙げられます。本番環境と開発環境を切り替えることもできますし、例えば本番環境からブランチを作成した場合、本番環境のデータをコピーしてくれるので、本番環境のデータを変更せずに検証したい場合にも非常に有用です。Webアプリケーションや開発環境との接続方法も簡単で、URL形式の接続情報を環境変数として「Render」や開発環境に登録することで簡単に接続することができます。（DBeaverやA5M2等のSQLクライアントツールからも接続可能です。）また、無料プランのサーバスペックは **「1.0 GB RAM / 0.25 CPU / 0.5 GB Storage」** です。もちろん**クレジットカード登録不要**で利用することができます。料金体系詳細については[こちら](https://neon.com/pricing)をご確認ください。『WebLearning』では「PostgreSQL」のバージョンには 17 を採用しており、プロバイダーには「AWS」、リージョンにはレイテンシを抑えるため「Render」のWebサーバのリージョンに近いリージョンを採用しています。

次章では『WebLearning』の開発環境について解説いたします。

---

## 開発環境 {#dev}

<figure>
  <img src="/static/images/architecture2.png" alt="アーキテクチャ図 - 開発環境" width="1000px" >
  <figcaption>アーキテクチャ図 - 開発環境</figcaption>
</figure>

『WebLearning』ではコンテナや様々なサービスを用いて開発しているため、事前に準備することが多く、インストールするツールも多いことから、一見複雑そうに感じる方もいるかもしれません。ただ一度構築してしまえば、各種利用サービスの形態が改悪されない限り、高い作業効率でWebアプリケーションの開発やデプロイ等作業が行えると思います。（開発版QOL爆上がりってやつです。）

### 開発用端末
「Docker」が利用できればOSは問いませんが、実際に利用していてRAMは8GB以上は必要に感じました。システム要件の詳細は以下を参照してください。  
[Windows に Docker Desktop をインストール — Docker-docs-ja 24.0 ドキュメント](https://docs.docker.jp/desktop/install/windows-install.html#id2)  
[Mac に Docker Desktop をインストール — Docker-docs-ja 24.0 ドキュメント](https://docs.docker.jp/desktop/install/mac-install.html#mac-system-requirements)  
[Linux に Docker Desktop をインストール — Docker-docs-ja 24.0 ドキュメント](https://docs.docker.jp/desktop/install/linux-install.html#desktop-linux-system-requirements)  

### Docker Desktop

<img src="/static/images/logo/docker-logo-blue.svg" alt="docker_logo" width="380px" style="background-color:#FFFFFF;">

Dockerイメージのビルドを行うために利用します。利用にはDockerアカウントの作成と開発端末へ「Docker Desktop」をインストールする必要があります。  
[Windows | Docker Docs](https://docs.docker.com/desktop/setup/install/windows-install/)  

### Visual Studio Code（任意）

<img src="/static/images/logo/vscode.svg" alt="vscode_logo" width="128px" style="background-color:#FFFFFF;">

コンテナで開発を行う場合、コンテナ内部にテキストエディタをインストールして開発をしても良いのですが、GUIのあるコンテナは少なく、なるべく本番環境で不要なものをコンテナ内部にインストールしたくないことから、ローカルのテキストエディタからのリモート接続でコーディングすることが多いです。『WebLearning』ではテキストエディタに拡張機能が豊富な「Visual Studio Code」を採用しています。  
[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)  

### Git

<img src="/static/images/logo/Git-Logo-1788C.svg" alt="git" width="380px" style="background-color:#FFFFFF;">

プロジェクト内のドキュメントやソースコードをバージョン管理するために利用します。管理単位は「リポジトリ」と呼ばれ、本構成ではリモートリポジトリをGitHub上にホストしています。  
[Git - Gitのインストール](https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)  

### Gitクライアント（任意）
Gitの操作をGUIから行うための支援ツールです。「GitHub Desktop」、「SourceTree」、「Gitkraken」、「Visual Studio Codeの拡張機能」等様々なツールがあります。現状『WebLearning』ではGitの基本操作しかしていないためテキストエディタとしても利用している「Visual Studio Codeの拡張機能」を採用しています。

### GitHub

<img src="/static/images/logo/GitHub_Logo.png" alt="GitHub_Logo" width="380px" style="background-color:#FFFFFF;">

リモートリポジトリの管理を行うためのサービスです。現在多くのOSS（Open Source Software）がGitHubで管理・公開されています。またリポジトリ管理以外にも「GitHub Packages」と呼ばれるコンテナイメージ等をパッケージ管理するサービスや、「GitHub Actions」と呼ばれるリポジトリに対して変更があった場合に、必要な作業を自動化するサービスがあり、『WebLearning』では 「リポジトリ内のDockerfile等コンテナに関わるファイルに対し変更があった場合に自動でDockerイメージをビルドする」トリガーを「GitHub Actions」に設定し、「GitHub Packages」で管理しているコンテナイメージを自動更新するといったワークフローを採用しています。  
[GitHub Japan | GitHub](https://github.co.jp/)  

### PostgreSQL

<img src="/static/images/logo/slonik_with_black_text_and_tagline.gif" alt="PostgreSQL_Logo" width="380px" style="background-color:#FFFFFF;">

オープンソースなリレーショナルデータベース管理システム（RDBMS）です。主に高性能でありながら商用利用可能な点で人気なようです。DjangoはORM（Object-Relational Mapping）設計のため、簡単なWebアプリケーションであれば、複雑なSQLを組む必要がないのでRDBMSは何でも良いのですが、シェア率の高いメジャーなものを利用してみたかったため採用しています。『WebLearning』ではユーザー管理、セッション管理、アプリケーションデータベース目的で利用しておりますが、[前述](#rdb)のDBaaS「Neon」を採用しているため、クラウド上でデータベース管理しております。  
[PostgreSQL: The world's most advanced open source database](https://www.postgresql.org/)

次章では『WebLearning』で採用している、Webアプリケーションフレームワークについて解説いたします。

---

## Webアプリケーションフレームワーク {#framework}

### バックエンド

<img src="/static/images/logo/django-logo-positive.svg" alt="django_logo" width="380px" style="background-color:#FFFFFF;">

「セキュリティ機能の充実」、「拡張性の高さ」、「活発なコミュニティによるサポート体制の充実」等々良いところは沢山ありますが、
結局のところ『WebLearning』の開発者がPythonが好きなのでDjangoを採用しています。  
[Django documentation](https://docs.djangoproject.com/ja/5.2/)

### フロントエンド
バックエンドと同じくDjangoを採用しています。
※フロントエンドフレームワークについては開発者の学習状況により、今後変更される可能性があります。


次章では『WebLearning』で採用している、ディレクトリ構造について解説いたします。

---

## ディレクトリ構造 {#dir}

以下は『WebLearning』のリポジトリ「[GitHub | synpage](https://github.com/shindy-dev/synpage)」のディレクトリ構造です。（プロジェクトやアプリ内部の構成は変更する可能性があるため省略しています。）

```
synpage/
├─ .devcontainer/
│   └─ .devcontainer.json            # VSCodeを起動したときに自動でコンテナに接続＆拡張機能をインストールしてくれるファイル
├─ .github/
│  └─ workflows/
│     └─ docker-duild.yml            # Dockerfile等pushで自動でDockerイメージをビルドするCI/CD設計書（格納しておくとGitHub Actionsで自動実行）
├─ .venv/                            # プロジェクト用Python仮想環境 ※Git監視対象外
├─ docs/                             # 開発者用ドキュメント
├─ docker/                           # dockerコンテナに格納するファイルを格納
│  └─ scripts/
│     ├─ entrypoint.sh               # コンテナ起動時の処理（DockerfileのENTRYPOINTで呼び出すスクリプト）
│     └─ postprocessing.sh           # entrypoint.sh のメイン処理後～サービス起動までの間にコンテナで実行したい処理を記述（任意）
│  └─ requirements.txt               # コンテナ内のPythonにインストールしたいライブラリを記載（Dockerイメージをビルドする際に使用）
├─ synpageproject/                   # 『WebLearning』用のDjangoプロジェクト
├─ weblearning/                      # 『WebLearning』本体
├─ .gitattributes                    # Gitリポジトリ内のファイルに対して特定の属性を設定するためのファイル（普段は意識しなくていい）
├─ .gitignore                        # Gitの監視対象外としたいファイルやディレクトリを記載（機密情報は絶対に監視対象外とすること）
├─ docker-compose.yaml               # コンテナを起動するための手順書（イメージ、ポート、起動モード、.envファイルパスの指定）
├─ docker-recompose.bat              # コンテナの再作成・起動（コンテナの停止＆削除＆イメージのpull＆コンテナのデーモン起動）
├─ docker-recompose.sh               # 同上（bash用）
├─ Dockerfile                        # Dockerイメージの作成手順書
├─ .env                              # 環境変数設定用ファイル（コンテナの環境変数として設定したい値を記述） ※Git監視対象外 ※ホストOSにのみ格納
├─ LICENSE                           # リポジトリ内のソースコードのライセンス
├─ manage.py                         # Djangoサーバ起動用スクリプト
├─ README.md                         # プロジェクトの説明を記述
├─ setup.bat                         # .venv環境＆必要なPythonライブラリをインストールするスクリプト（Dockerが利用できない環境で開発したい場合に使用する）
├─ setup.sh                          # 同上（bash用）
└─ todo.md                           # タスク管理用のメモ（任意）
```

以上『WebLearning』の構成についてのご紹介でした！必ずしもこの構成でないといけないというわけではないので、ご自身の環境や好みに合わせて学習用の環境を構築してみてください。

---





