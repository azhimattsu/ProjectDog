
import uuid


class FactoryId:

    @staticmethod
    def create_id() -> str:
        return str(uuid.uuid4())
