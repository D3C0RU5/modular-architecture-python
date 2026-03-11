from .module_engine import ModuleEngine


def create_session(database_url: str):
    engine = ModuleEngine(database_url)
    return engine.get_session()
