import sys

from resources.concrete.handler.argument_handler import SysArgumentHandler

if __name__ == '__main__':
    try:
        handler = SysArgumentHandler(debug=False)
        handler.handle_arguments(sys.argv)
    except Exception as error:
        raise error
