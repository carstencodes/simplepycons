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


class ShieldsdotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shieldsdotio"

    @property
    def original_file_name(self) -> "str":
        return "shieldsdotio.svg"

    @property
    def title(self) -> "str":
        return "Shields.io"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shields.io</title>
     <path d="M19 0a5 5 0 0 1 5 5v14a5 5 0 0 1-5 5H5l-.257-.007A5 5 0
 0 1 0 19V5a5 5 0 0 1 5-5zm-7 21h7a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2h-7z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/badges/shields/blob/2b4d17'''

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
