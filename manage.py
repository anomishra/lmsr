from flask_script import Manager, Server
import os

from app import app

manager = Manager(app)

# use_reloader is active!
server = Server(host="0.0.0.0", port=8080, use_reloader=True)
manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()
