
# SearchEngine for JSON
* json形式のデータから指定の型を持つkeyとvalueを再起的に取得します


# install
```bash
git clone https://github.com/aoimaru/rest_demo
cd rest_demo
docker-compose up -d
docker inspect "databaseのコンテナID"
rest_demo_defaultネットワーク内でのdatabaseコンテナのIPアドレスをrun.pyでの
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
    **{
      'user': os.getenv('DB_USER', 'root'),
      'password': os.getenv('DB_PASSWORD', 'root'),
      'host': os.getenv('DB_HOST', '172.26.0.2'), <-ここに適用
      'database': os.getenv('DB_DATABASE', 'sample01'),
    })
```
