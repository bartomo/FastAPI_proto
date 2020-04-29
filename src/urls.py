from controllers import *


# FastAPIルーティング用関数
app.add_api_route('/', index)
app.add_api_route('/admin', admin)

