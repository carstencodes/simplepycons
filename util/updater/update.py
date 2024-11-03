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
from sys import argv

current_dir = Path(__file__).parent.absolute().resolve()
project_dir = current_dir.parent.parent.absolute().resolve()

icons_module_dir = project_dir / "vendor" / "simple-icons"

_, *args = argv

if len(args) == 0:
    with chdir(icons_module_dir):
        p = run(["git", "fetch", "--tags", "origin"], check=True, capture_output=True)
        if p.stdout is not None:

            print(p.stdout)

            new_tags = p.stdout.splitlines()
            new_tags = [t for t in new_tags if t.lstrip().startswith(b'*')]

            if len(new_tags) == 0:
                print("No changes detected")
                raise SystemExit(0)

            new_tags = [t.split("->")[1].strip() for t in new_tags]

        else:
            print("No output to analyze")
            new_tags = []
else:
    print(f"Using versions: {args}")
    new_tags = args

with chdir(project_dir):
    print("Getting current version/epoch")
    current_version = run(["pdm", "show", "--version"], check=True, capture_output=True).stdout
    epoch, _ = current_version.split(b'!', 2)
    epoch = int(epoch)

for tag in new_tags:
    print(f"Processing {tag}")
    with chdir(icons_module_dir):
        print ("Checkout ...")
        run(["git", "checkout", f"tags/{tag}"], check=True)

    with chdir(project_dir):
        print ("Generation ...")
        run(["pdm", "generate"], check=True)
        print ("Version bump ...")
        run(["pdm", "bump", "to", f"{epoch}!{tag}"], check=True)
        with (project_dir / "simple-icons.json").open("w") as f:
            dump({"simple-icons": { "version": tag }}, f)

        print ("Check-in / Commit ...")
        run(["git", "add", "simple-icons.json", "pyproject.toml", "src/", str(icons_module_dir)], check=True)
        run(["git", "commit", "-m", f"chore(deps): Updated simple icons to '{tag}'"], check=True)
        print ("Build ...")
        run(["pdm", "build", "--no-sdist"], check=True)
        whl = project_dir / "dist" / f"simplepycons-{epoch}!{tag}-py3-none-any.whl"
        while not whl.exists():
            print(f"Waiting for {whl} to become available")
            sleep(1)
        print ("Upload ...")
        run(["twine", "upload", str(whl)], check=True)
        print ("Tagging ...")
        run(["pdm", "bump", "tag"], check=True)
        print ("Next ...")

print ("Pushing ...")
run(["git", "push"], check=True)
run(["git", "push", "--tags"], check=True)
print ("... done!")

