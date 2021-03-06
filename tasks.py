# -*- coding: utf-8 -*-

import os
import shutil
import sys
import datetime

from invoke import task
from invoke.util import cd
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

CONFIG = {
    # Local path configuration (can be absolute or relative to tasks.py)
    "deploy_path": "docs",
    # Github Pages configuration
    "github_pages_branch": "master",
    "commit_message": f"""'Publish site on {datetime.date.today().isoformat()}'""",
    # Port for `serve`
    "port": 8000,
}


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run("pelican -d")


@task
def serve(c):
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def up(c):
    """`build`, then `serve`"""
    rebuild(c)  # uses default for local pelicanconf.py
    serve(c)


@task
def make_prod(c):
    """Build production version of site"""
    c.run("pelican -s publishconf.py")


@task
def prod_deploy(c):
    """Publish to GitHub Pages"""
    clean(c)
    rebuild(c)
    make_prod(c)
    c.run("git add .")
    c.run(f"git commit -m \"{CONFIG.get('commit_message')}\"")
    c.run(f"git push origin {CONFIG.get('github_pages_branch')}")
