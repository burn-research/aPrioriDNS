# tests/conftest.py
import os
import matplotlib
import pytest


@pytest.fixture(scope="session", autouse=True)
def _mpl_headless():
    matplotlib.use("Agg")


@pytest.fixture(scope="session")
def apriori_test_cache_dir(tmp_path_factory):
    """
    Persistent cache for test datasets.

    Priority:
      1) APRIORI_TEST_DATA env var (if set)
      2) <repo_root>/.pytest_apriori_cache  (created automatically)
      3) pytest temp dir fallback (should rarely happen)
    """
    # 1) user override
    env = os.environ.get("APRIORI_TEST_DATA")
    if env:
        os.makedirs(env, exist_ok=True)
        return env

    # 2) repo-local persistent cache
    # pytest always runs with a working directory; typically repo root
    repo_cache = os.path.abspath(os.path.join(os.getcwd(), ".pytest_apriori_cache"))
    os.makedirs(repo_cache, exist_ok=True)
    return repo_cache