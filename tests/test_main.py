from hackathon_26.main import main


def test_main() -> None:
    assert main("foo") == "foo"
