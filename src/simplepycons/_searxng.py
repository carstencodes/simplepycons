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


class SearxngIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "searxng"

    @property
    def original_file_name(self) -> "str":
        return "searxng.svg"

    @property
    def title(self) -> "str":
        return "SearXNG"

    @property
    def primary_color(self) -> "str":
        return "#3050FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SearXNG</title>
     <path d="m13.716 17.261 6.873 6.582L24 20.282l-6.824-6.536a9.11
 9.11 0 0 0 1.143-4.43c0-5.055-4.105-9.159-9.16-9.159S0 4.261 0
 9.316c0 5.055 4.104 9.159 9.159 9.159a9.11 9.11 0 0 0
 4.557-1.214ZM9.159 2.773a6.546 6.546 0 0 1 6.543 6.543 6.545 6.545 0
 0 1-6.543 6.542 6.545 6.545 0 0 1-6.542-6.542 6.545 6.545 0 0 1
 6.542-6.543ZM7.26 5.713a4.065 4.065 0 0 1 4.744.747 4.064 4.064 0 0 1
 .707 4.749l1.157.611a5.376 5.376 0 0 0-.935-6.282 5.377 5.377 0 0
 0-6.274-.987l.601 1.162Z" />
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
