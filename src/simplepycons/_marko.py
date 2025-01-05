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


class MarkoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "marko"

    @property
    def original_file_name(self) -> "str":
        return "marko.svg"

    @property
    def title(self) -> "str":
        return "Marko"

    @property
    def primary_color(self) -> "str":
        return "#2596BE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Marko</title>
     <path d="M15.4 5.46h-3.39l-2.3 3.77L7.4 5.46H4l-4 6.55 4
 6.53h3.39l-4-6.54L5.7 8.23 8.01 12h3.39l2.31-3.78L16.03 12l-4.01
 6.54h3.39l4-6.54zm4.6 0h-3.39l4 6.54-4.01 6.54h3.39L24 12z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/marko-js/website/blob/c03b'''

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
