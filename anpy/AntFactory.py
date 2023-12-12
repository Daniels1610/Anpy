from anpy.Ant import Ant

class AntFactory():
    @staticmethod
    def create(id:int) -> Ant:
        return Ant(id)