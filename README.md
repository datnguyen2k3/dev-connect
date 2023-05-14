1. pip install -r requirements.txt
2. install elastic search, config its password in /web_backend/src/settings.py, turn on elastic sever
3. install redis, turn on redis server
4. cd web_backend
5. python manage.py search_index --rebuild (first time)
6. python -m celery -A src worker -l info -P gevent
