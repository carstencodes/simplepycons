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


class TheFinalsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thefinals"

    @property
    def original_file_name(self) -> "str":
        return "thefinals.svg"

    @property
    def title(self) -> "str":
        return "THE FINALS"

    @property
    def primary_color(self) -> "str":
        return "#D31F3C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>THE FINALS</title>
     <path d="M18.523 19.319H24L14.965
 6.295c-.626-.904-1.51-1.614-2.847-1.614-1.38 0-2.264.775-2.889
 1.614L0 19.319h5.261l3.372-4.759 3.256
 4.759h5.478l-5.934-8.712.599-.846 6.491 9.558Zm0 0" />
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
