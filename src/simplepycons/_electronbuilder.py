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


class ElectronbuilderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "electronbuilder"

    @property
    def original_file_name(self) -> "str":
        return "electronbuilder.svg"

    @property
    def title(self) -> "str":
        return "electron-builder"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>electron-builder</title>
     <path d="M12 7.01a3.506 3.506 0 003.506-3.505A3.506 3.506 0 0012
 0a3.506 3.506 0 00-3.506 3.506A3.506 3.506 0 0012 7.01m0 4.137C9.243
 8.588 5.574 7.01 1.484 7.01v12.852C5.574 19.863 9.243 21.44 12
 24c2.757-2.56 6.426-4.137 10.516-4.137V7.01c-4.09 0-7.759
 1.578-10.516 4.137z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
