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


class TeradataIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "teradata"

    @property
    def original_file_name(self) -> "str":
        return "teradata.svg"

    @property
    def title(self) -> "str":
        return "Teradata"

    @property
    def primary_color(self) -> "str":
        return "#F37440"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Teradata</title>
     <path d="M12 0C5 0 0 5.65 0 12.08C0 18.83 5 24 12 24S24 18.83 24
 12.08C24 5.65 19 0 12 0M8.47
 3.44H11.97V6.7H15.55V9.56H11.97V14.78C11.97 16.36 12.74 17.05 13.9
 17.05C14.32 17.05 14.88 16.93 15.41 16.73C15.79 17.73 16.46 18.63
 17.18 19.35A7 7 0 0 1 13.66 20.32C10.54 20.32 8.47 18.67 8.47
 15.04V3.45Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Teradata/teradata.github.i
o/blob/0fb3886aaeefea7bea4951c300f49ac8f9c2476f/src/assets/icons/terad'''

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
