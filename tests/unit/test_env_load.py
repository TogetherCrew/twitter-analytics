import os

from dotenv import load_dotenv


def test_neo4j_env_variables():
    """
    test if the environment variables are loaded correctly
    """
    load_dotenv()

    protocol = os.getenv("NEO4J_PROTOCOL")
    host = os.getenv("NEO4J_HOST")
    port = os.getenv("NEO4J_PORT")
    db_name = os.getenv("NEO4J_DB")

    user = os.getenv("NEO4J_USER")
    password = os.getenv("NEO4J_PASSWORD")

    assert protocol is not None
    assert host is not None
    assert port is not None
    assert db_name is not None
    assert protocol is not None
    assert user is not None
    assert password is not None
