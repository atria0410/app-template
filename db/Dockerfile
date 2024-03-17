FROM postgres:16.2

COPY postgresql.conf /etc/postgresql/
COPY create-multiple-databases.sh /docker-entrypoint-initdb.d/

# イメージ実行時に起動させるプロセスを設定
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
