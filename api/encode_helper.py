import base64


def enkode(s):
    return base64.b64encode(s.encode()).decode()


def dekode(s):
    return base64.b64decode(s).decode()

if __name__ == "__main__":
    pass