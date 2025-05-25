class OpcaoErroException(Exception):
    def __init__(self):
        super().__init__("Parece que voce escreveu um valor errado")
