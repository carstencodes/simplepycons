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


class XstateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xstate"

    @property
    def original_file_name(self) -> "str":
        return "xstate.svg"

    @property
    def title(self) -> "str":
        return "XState"

    @property
    def primary_color(self) -> "str":
        return "#2C3E50"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>XState</title>
     <path d="M15.891 0h6.023l-6.085
 10.563c-1.853-3.305-1.822-7.32.062-10.563zm6.055
 23.999L8.078.001H2.055l6.919 12.015L2.055 24h6.023L12 17.236 15.892
 24z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/davidkpiano/xstate/blob/54'''

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
