## マイグレーション

マイグレーションには [Alembic](https://alembic.sqlalchemy.org/en/latest/) を使用します。  
alembic コマンドは database/migration 直下で実行してください。

```sh
cd database/migration
```

以下のコマンドを実行するとモデル定義に従ってマイグレーションファイルが生成されます。

```sh
alembic revision --autogenerate -m "コメント"
```

以下のコマンドでマイグレートを実行します。

```sh
alembic upgrade head
```

## シーディング

以下のコマンドでデータベースにサンプル用のデータを登録できます

```sh
python database/seeds/seed.py
```

## テスト

下記コマンドでテストがユニットテストを実行できます。

```sh
pytest
```

## その他

その他、詳細は FastAPI の公式ドキュメントを参照してください。

[FastAPI 公式ドキュメント](https://fastapi.tiangolo.com/ja/)
