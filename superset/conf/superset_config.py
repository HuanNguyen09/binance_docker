SECRET_KEY = '7f1d36b4baf29daa2cf9d36dc3f31c5a'
# Tắt SQLALCHEMY_ECHO trong môi trường sản xuất
SQLALCHEMY_ECHO = False

# Thiết lập timeout cho các truy vấn
SUPERSET_WEBSERVER_TIMEOUT = 10000

# Thiết lập đường dẫn lưu trữ file tạm
#UPLOAD_FOLDER = './upload/folder'
# Sử dụng Redis làm backend cach
FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_filter_cache',
    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}
DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "SupersetMetastoreCache",
    "CACHE_KEY_PREFIX": "superset_results",  # make sure this string is unique to avoid collisions
    "CACHE_DEFAULT_TIMEOUT": 86400,  # 60 seconds * 60 minutes * 24 hours
}
QUERY_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_query_cache',
#    'CACHE_REDIS_URL': 'redis://localhost:6379/0'
}
