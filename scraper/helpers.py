import datetime
import os
from mimetypes import guess_extension
from urllib.parse import urlparse


def download_assets(
    requests,
    asset_dir="temp",
    default_fname="unnamed",
    keep_domains=["ris.reshapebiotech.com"],
    exts=[".png", ".jpeg", ".jpg", ".svg"],
    append_ext=False,
):
    asset_list = {}
    for req_idx, request in enumerate(requests):
        if (
            not request
            or not request.response
            or not request.response.headers
            or "Content-Type" not in request.response.headers
        ):
            continue

        content_type = request.response.headers["Content-Type"].split(";")[0].strip()
        ext = guess_extension(content_type)
        if not ext or ext not in exts:
            continue

        parsed_url = urlparse(request.url)
        if parsed_url.netloc not in keep_domains:
            continue

        frelpath = parsed_url.path.strip()
        if not frelpath:
            timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
            frelpath = f"{default_fname}_{req_idx}_{timestamp}{ext}"
        elif frelpath.endswith(("/", "\\")):
            timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
            frelpath += f"{default_fname}_{req_idx}_{timestamp}{ext}"
        elif append_ext and not frelpath.endswith(ext):
            frelpath += f"_{default_fname}{ext}"
        if frelpath.startswith(("/", "\\")):
            frelpath = frelpath[1:]

        fpath = os.path.join(asset_dir, parsed_url.netloc, frelpath)
        if os.path.isfile(fpath):
            continue
        os.makedirs(os.path.dirname(fpath), exist_ok=True)

        print(f"Downloading {request.url} to {fpath}")
        asset_list[fpath] = request.url
        try:
            with open(fpath, "wb") as file:
                file.write(request.response.body)
        except:
            print(f"Cannot download {request.url} to {fpath}")
    return asset_list
