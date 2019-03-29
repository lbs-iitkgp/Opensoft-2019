from endpoints import *

from endpoints.act import *
from endpoints.case import *
from endpoints.catchword import *
from endpoints.judge import *
from endpoints.keyword import *
from endpoints.search import *
from endpoints.misc import *
from endpoints.years import *

if __name__ == '__main__':
    app.run("0.0.0.0" ,port=5000, debug=True)
    
