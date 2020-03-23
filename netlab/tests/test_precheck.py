import os


class TestLinks:
    def test_no_temp(self):
        """Folder "temp" should not existed outside of check mode"""
        assert "temp" not in os.listdir()

    def test_cases_content(self):
        """
        Any link starts with letters "cf" should not exist
        inside folder "cases"
        """
        for roots, dirs, files in os.walk("cases", topdown=False):
            for file in files:
                assert not file.startswith("cf")
