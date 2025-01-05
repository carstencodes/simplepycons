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


class ModxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "modx"

    @property
    def original_file_name(self) -> "str":
        return "modx.svg"

    @property
    def title(self) -> "str":
        return "MODX"

    @property
    def primary_color(self) -> "str":
        return "#102C53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MODX</title>
     <path d="M19.145 9.49l4.47-7.19H12.118l-1.24 2.023zM2.92
 0v11.497l2.48 1.55 13.435-3.1zm18.16 24V12.503l-1.984-1.263-5.168
 8.267zM5.165 14.053l-4.78 7.648h11.497L18.6 10.953Z" />
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
