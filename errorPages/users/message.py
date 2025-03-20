class message:
    def __init__(self, type: str, message: str, code: int, img: str = None):
        self.type = type
        self.message = message
        self.code = code
        self.img = img
    def __str__(self):
        return f"[{self.type.upper()}] Código {self.code}: {self.message} (Imagen: {self.img})"
    
    def to_dict(self):
        return {
        "type": self.type,
        "message": self.message,
        "code": self.code,
        "img": self.img
        }