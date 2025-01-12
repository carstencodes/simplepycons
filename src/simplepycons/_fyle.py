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


class FyleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fyle"

    @property
    def original_file_name(self) -> "str":
        return "fyle.svg"

    @property
    def title(self) -> "str":
        return "Fyle"

    @property
    def primary_color(self) -> "str":
        return "#FF2E63"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fyle</title>
     <path d="M10.024 0H1.241C.56 0 0 .56 0 1.243v21.514C0 23.44.56 24
 1.241 24h21.518A1.24 1.24 0 0 0 24 22.757V1.243C24 .56 23.44 0 22.759
 0H11.675v15.592c-.04.775-.29 1.397-.761 1.865-.92.927-2.521
 1.049-3.921 1.049-1.891
 0-4.432-.244-4.862-2.273l-.06-.508c-.02-.101-.02-.387-.02-1.131V3.965c0-.488.16-.907.51-1.254A1.7
 1.7 0 0 1 3.812 2.2l4.611.02.161.041v1.562H3.962c-.12
 0-.18.061-.18.142v3.484h3.491v1.599H3.782v6.566c.04 1.15 1.74 1.375
 3.181 1.375.64-.021 1.991-.021 2.601-.632.16-.165.32-.471.46-.928V0Z"
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
