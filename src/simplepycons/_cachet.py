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


class CachetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cachet"

    @property
    def original_file_name(self) -> "str":
        return "cachet.svg"

    @property
    def title(self) -> "str":
        return "Cachet"

    @property
    def primary_color(self) -> "str":
        return "#7ED321"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cachet</title>
     <path d="M11.746.254C5.265.254 0 5.519 0 12c0 6.481 5.265 11.746
 11.746 11.746 6.482 0 11.746-5.265 11.746-11.746
 0-1.44-.26-2.82-.734-4.097l-.264-.709-1.118 1.118.1.288c.373
 1.064.575 2.207.575 3.4a10.297 10.297 0 01-10.305 10.305A10.297
 10.297 0 011.441 12 10.297 10.297 0 0111.746 1.695c1.817 0 3.52.47
 5.002 1.293l.32.178 1.054-1.053-.553-.316A11.699 11.699 0
 0011.746.254zM22.97.841l-13.92 13.92-3.722-3.721-1.031 1.03 4.752
 4.753L24 1.872z" />
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
