from os.path import abspath, dirname, join
DEBUG = True
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
# google storage config
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = join(dirname(abspath(__file__)), 'dev_keys/google_storage_configuration.json')  # path to private json key file obtained by Google.
