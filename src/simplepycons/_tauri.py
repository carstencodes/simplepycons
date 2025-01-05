#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class TauriIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tauri"

    @property
    def original_file_name(self) -> "str":
        return "tauri.svg"

    @property
    def title(self) -> "str":
        return "Tauri"

    @property
    def primary_color(self) -> "str":
        return "#24C8D8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tauri</title>
     <path d="M13.912 0a8.72 8.72 0 0 0-8.308 6.139c1.05-.515
 2.18-.845 3.342-.976 2.415-3.363 7.4-3.412 9.88-.097 2.48 3.315 1.025
 8.084-2.883 9.45a6.131 6.131 0 0 1-.3 2.762 8.72 8.72 0 0 0
 3.01-1.225A8.72 8.72 0 0 0 13.913 0zm.082 6.451a2.284 2.284 0 1 0-.15
 4.566 2.284 2.284 0 0 0 .15-4.566zm-5.629.27a8.72 8.72 0 0 0-3.031
 1.235 8.72 8.72 0 1 0 13.06 9.9131 10.173 10.174 0 0 1-3.343.965
 6.125 6.125 0 1 1-7.028-9.343 6.114 6.115 0 0 1 .342-2.772zm1.713
 6.27a2.284 2.284 0 0 0-2.284 2.283 2.284 2.284 0 0 0 2.284 2.284
 2.284 2.284 0 0 0 2.284-2.284 2.284 2.284 0 0 0-2.284-2.284z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/tauri-apps/tauri-docs/blob
/b1cdfa9d7c6d0b17dae60a90266ddced40a7b384/static/img/Brand_Guidelines.'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tauri-apps/tauri-docs/blob'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
