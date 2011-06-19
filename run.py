import sys, os
import setting
from ims import app
app.config.from_object(setting)

if __name__ == '__main__':
    app.run()
