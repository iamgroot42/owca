from werkzeug.security import generate_password_hash
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    print("Password for %s: %s" % (name, generate_password_hash(name)))
