from config.env import env

urlapi = ''
if env('ENVIRONMENT') == 'production':
    urlapi = env('URL_API_PROD')
else:
    urlapi = env('URL_API_DEV')

apilogin = urlapi + '/auth/login'