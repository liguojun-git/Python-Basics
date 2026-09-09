# app.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]




# 命令行启动
# waitress-serve --host=127.0.0.1 --port=8080 app:application