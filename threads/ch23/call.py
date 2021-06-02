#import simple
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

logging.warning('Watch out!')
logging.info("start OS update")
#x = 42
#y[0] = 42

# print(simple.x)
# print(simple.y)

shadow = {
    "readerVersion": "old"
}

if(shadow["readerVersion"] == "new"):
    print("new")
else:
    print("old")
