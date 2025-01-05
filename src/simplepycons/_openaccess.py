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


class OpenAccessIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openaccess"

    @property
    def original_file_name(self) -> "str":
        return "openaccess.svg"

    @property
    def title(self) -> "str":
        return "Open Access"

    @property
    def primary_color(self) -> "str":
        return "#F68212"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Access</title>
     <path d="M18.971 13.486a7.56 7.56 0 00-.54-1.043V6.415a6.375
 6.375 0 00-1.88-4.535A6.374 6.374 0 0012.017 0h-.002a6.374 6.374 0
 00-4.536 1.878 6.375 6.375 0 00-1.88
 4.537v.877h2.57v-.877c0-1.026.4-1.992 1.127-2.72a3.822 3.822 0
 012.72-1.125 3.852 3.852 0 013.847 3.845v3.508A7.52 7.52 0 0012
 8.865a7.54 7.54 0 00-5.35 2.216 7.54 7.54 0 00-2.216 5.35 7.54 7.54 0
 002.215 5.35A7.54 7.54 0 0012 24a7.54 7.54 0 005.35-2.216 7.54 7.54 0
 002.216-5.35c0-1.021-.2-2.012-.595-2.946zM12 21.428a5.003 5.003 0
 01-4.997-4.996A5.003 5.003 0 0112 11.435a5.002 5.002 0 014.997
 4.997A5.002 5.002 0 0112 21.428zm2.145-4.973a2.12 2.12 0 11-4.24 0
 2.12 2.12 0 014.24 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Open_'''

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
