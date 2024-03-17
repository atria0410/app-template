## 使用技術

<p>
  <img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker&style=plastic">
  <img src="https://img.shields.io/badge/-Vue.js-4FC08D.svg?logo=vue.js&style=plastic">
  <img src="https://img.shields.io/badge/-Nuxt.js-00C58E.svg?logo=nuxt.js&style=plastic">
  <img src="https://img.shields.io/badge/-Typescript-007ACC.svg?logo=typescript&style=plastic">
  <img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">
  <img src="https://img.shields.io/badge/-Postgresql-336791.svg?logo=postgresql&style=plastic">
</p>

## アーキテクチャ

![architecture](https://github.com/atria0410/myapp/assets/70093193/4b8ab7c6-15b4-4b17-a938-f9e2f4e747f6)

## クイックスタート

.env.example ファイルをコピーして.env ファイルを作成します。  
必要に応じてポート番号やデータベースのパスワードの設定を行ってください。

コンテナ起動（開発モード）

```
docker compose -f "docker-compose.dev.yml" up -d --build
```

コンテナ起動（本番モード）

```
docker compose -f "docker-compose.prod.yml" up -d --build
```

## 開発にあたって

本アプリケーションの開発は VSCode での開発を前提としています。  
下記手順に従いコーディングを行ってください。

### 手順

1. VSCode でプロジェクトを開きます。
2. 拡張機能タブの検索枠に「@recommended 」と入力し、表示された拡張機能を全てインストールします。
3. コンテナ起動後、Windows の場合は「Ctrl + P」、Mac の場合は「Cmd + P」でクイックオープンウィンドウを開きます。
4. 「> Open Folder in Container」と入力して実行します。
5. Windows の場合はエクスプローラ、Mac の場合は Finder が表示されるので「interface」または「api」フォルダを開いてください。  
   「interface」を開いた場合は interface コンテナの Nuxt.js ディレクトリを VSCode で開きなおします。  
   「api」を開いた場合は api コンテナの FastAPI ディレクトリを VSCode で開きなおします。
