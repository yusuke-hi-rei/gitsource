# yusuke-hi-rei add start
'''
  開発環境固有の設定ファイル
'''
from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#! Django公式サイト: https://docs.djangoproject.com/ja/2.2/topics/logging/
#! Python.orgロギングハンドラ: https://docs.python.org/ja/3/library/logging.handlers.html
#! ロギング設定
LOGGING = {
    'version': 1, # 1固定
    'disable_existing_loggers': False, #! False: 既存ロガーの無効化
    #! ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        #! diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
    #! ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', #! StreamHandler: コンソールへ出力
            'formatter': 'dev'
        },
    },
    #! フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

#! 開発時のメール配信先設定(コンソール)
#! バックエンド定義
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# yusuke-hi-rei add end
