# Содержимое этого файла необходимо скопировать в config.py и изменить под себя

TOKEN = '542255798:AAGLKRHK4ehyMGBE6Oz2HED9Dd0TU3wV91w' # Токен телеграмбота (получается у @BotFather)
DB = 'mysql://be7e037166f6fd:9120268b@eu-cdbr-west-01.cleardb.com/heroku_2628e0f251e73f5?reconnect=true' # Строчка подключения к базе данных (поддерживается только MySql, о формате можно прочитать тут http://docs.sqlalchemy.org/en/latest/dialects/mysql.html)
API_PORT = 88 # Порт, по которому будет доступен внешний апи бота (REST)
GOVERNMENT_CHAT =  # Чат, в который бот будет слать отчёты
SUPER_ADMIN_ID = 272348732 # id супер админа
# вербовочный функционал:
CASTLE_CHAT_ID = None # id замкового чата (для поиска новых игроков в замке - если None - функционал отключен)
ACADEM_CHAT_ID = None # id чата академии (для уведомления о новых игроках в замке - если None - функционал отключен)
CASTLE = None # Флаг замка, который вы хотите обслуживать (например '🇮🇲'), оставьте None, чтобы не было ограничений
WEB_LINK = 'Please change it. {}'
