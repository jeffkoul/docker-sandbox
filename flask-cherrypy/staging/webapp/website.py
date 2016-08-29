from flask import Flask
staticContent = Flask(__name__)

@staticContent.route("/")
def root():
    return "Hello from app root!\n"

@staticContent.route("/subPath")
def subPath():
    return "You made it to a subpath: whee....\n"

if __name__ == "__main__":
    staticContent.run()

