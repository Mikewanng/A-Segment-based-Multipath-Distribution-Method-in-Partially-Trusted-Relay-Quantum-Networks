class Link(object):#定义边
    def __init__(self,fr=None,to=None,capacity=0,Is_fr_trusted=False,Is_to_trusted=False,Is_connected=False):
        self.fr=fr
        self.to=to
        self.c=capacity
        self.Is_fr_trusted=Is_fr_trusted
        self.Is_to_trusted=Is_to_trusted
        self.Is_connected=Is_connected


    def dellink(self):
        self.fr=None
        self.to=None
        self.c=0
        self.Is_fr_trusted=False
        self.Is_to_trusted=False
        self.Is_connected=False





