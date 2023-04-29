from RailsTranslatorException import NotARailsProject
import pytest
import main


def test_root():
    main.input = lambda _: "C:\\Not\\A\\Rails\\Project"
    with pytest.raises(NotARailsProject):
        main.main()


def teardown_method():
    main.input = input
