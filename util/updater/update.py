#!/usr/bin/env python3
#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#

from pathlib import Path
from contextlib import chdir
from subprocess import run
from json import dump
from time import sleep

current_dir = Path(__file__).parent.absolute().resolve()
project_dir = current_dir.parent.parent.absolute().resolve()

icons_module_dir = project_dir / "vendor" / "simple-icons"

with chdir(icons_module_dir):
    p = run(["git", "fetch", "origin", "--tags"], check=True, capture_output=True)
    if p.stdout is not None:

        new_tags = p.stdout.splitlines()
        new_tags = [t for t in new_tags if t.lstrip().startswith(b'*')]

        if len(new_tags) == 0:
            print("No changes detected")
            raise SystemExit(0)
    else:
        print("No output to analyze")
        new_tags = []

with chdir(project_dir):
    current_version = run(["pdm", "show", "--version"], check=True, capture_output=True).stdout
    epoch, _ = current_version.split(b'!', 2)
    epoch = int(epoch)

for tag in new_tags:
    with chdir(icons_module_dir):
        run(["git", "checkout", f"tags/{tag}"], check=True)

    with chdir(project_dir):
        run(["pdm", "generate"], check=True)
        run(["pdm", "bump", "to", f"{epoch}!{tag}"], check=True)
        with (project_dir / "simple-icons.json").open("w") as f:
            dump({"simple-icons": { "version": tag }}, f)

        run(["git", "add", "simple-icons.json", "pyproject.toml", "src/", str(icons_module_dir)], check=True)
        run(["git", "commit", "-m", f"chore(deps): Updated simple icons to '{tag}'"], check=True)
        run(["pdm", "build", "--no-sdist"], check=True)
        whl = project_dir / "dist" / f"simplepycons-{epoch}!{tag}-py3-none-any.whl"
        while not whl.exists():
            print(f"Waiting for {whl} to become available")
            sleep(1)
        run(["twine", "upload", str(whl)], check=True)
        run(["pdm", "bump", "tag"], check=True)

run(["git", "push"], check=True)
run(["git", "push", "--tags"], check=True)
