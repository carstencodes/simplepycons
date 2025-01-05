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


class KtmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ktm"

    @property
    def original_file_name(self) -> "str":
        return "ktm.svg"

    @property
    def title(self) -> "str":
        return "KTM"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KTM</title>
     <path d="M0 15.735h3.354l.843-2.06 1.55
 2.06h7.225l2.234-2.081-.372 2.081h2.83L20 13.675l-.32 2.06h3.052L24
 9.99h-3.068l-2.486 2.191.48-2.19h-2.942l-3.209 3.216
 1.342-3.938h4.907l.225-1.003H6.381l-.378 1.003h4.732l-1.994
 5.054-1.572-2.066L9.886 9.99H7.612l-2.787 2.23.938-2.23H2.44L0
 15.735Z" />
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
