from __future__ import annotations

import os
from pathlib import Path

import pooch
from platformdirs import user_cache_dir

DEFAULT_ENDPOINT = 'https://huggingface.co'
ENDPOINT = os.environ.get('HF_ENDPOINT', DEFAULT_ENDPOINT).rstrip('/')
BASE_CACHE = Path(user_cache_dir('wulu-geetest-bypass', appauthor=False))


def get_fetcher():
    return pooch.create(
        path=BASE_CACHE / 'icon',
        base_url=f'{ENDPOINT}/wulu007/gt/resolve/main/',
        registry={'icon_t1_261010': None},
    )


def get_model_path() -> Path:
    local_file = get_fetcher().fetch('icon_t1_261010', progressbar=True)
    return Path(local_file)


if __name__ == '__main__':
    print(get_model_path())
