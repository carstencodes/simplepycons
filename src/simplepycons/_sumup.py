#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class SumupIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sumup"

    @property
    def original_file_name(self) -> "str":
        return "sumup.svg"

    @property
    def title(self) -> "str":
        return "SumUp"

    @property
    def primary_color(self) -> "str":
        return "#1E1C1C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SumUp</title>
     <path d="M19.488 0A4.51 4.51 0 0 1 24 4.512v14.976A4.51 4.51 0 0
 1 19.488 24H4.512A4.51 4.51 0 0 1 0 19.488V4.512A4.51 4.51 0 0 1
 4.512 0zM7.308 17.855a5.4 5.4 0 0 0 7.649 0 5.424 5.424 0 0 0
 0-7.662zm9.385-11.71a5.4 5.4 0 0 0-7.649 0 5.424 5.424 0 0 0 0
 7.662z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/sumup-oss/circuit-ui/tree/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://circuit.sumup.com/?path=/docs/brand-s'''

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
