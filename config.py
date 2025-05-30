import os

BASE_URLS = {
    "production": "alldev.click",
}

SITE_ENV = os.environ.get("SITE_ENV", "production")
BASE_URL = BASE_URLS[SITE_ENV]
ROOT_DIR = "pages"
LAYOUTS_BASE_DIR = "_layouts"
SITE_DIR = "_site"
HOOKS = {}
SITE_STATE = {}
