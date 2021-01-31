# https://docs.gunicorn.org/en/latest/settings.html#settings

bind = "0.0.0.0:8080"
keepalive = 5
workers = 5
max_requests = 1000
max_requests_jitter = 200
loglevel = "INFO"
accesslog = "-"
errorlog = "-"
access_log_format = (
    '%({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
)
