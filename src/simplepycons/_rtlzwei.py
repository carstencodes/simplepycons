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


class RtlzweiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rtlzwei"

    @property
    def original_file_name(self) -> "str":
        return "rtlzwei.svg"

    @property
    def title(self) -> "str":
        return "RTLZWEI"

    @property
    def primary_color(self) -> "str":
        return "#00BCF6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RTLZWEI</title>
     <path d="M0 0v24h7.38v-3.69H3.692L3.69 3.69h9.229V0H0zm16.61
 0v3.69h3.7v16.62h-9.238V24H24V0h-7.39zm-.003
 6.49l-3.689.717v9.227l3.69-.715V6.49zm-5.535
 1.076l-3.69.715v9.229l3.69-.717V7.566z" />
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
