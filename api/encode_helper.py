import base64


def custom_encode(s):
    return base64.b64encode(s.encode()).decode()


def custom_decode(s):
    return base64.b64decode(s).decode()

if __name__ == "__main__":
    pass