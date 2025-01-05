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


class KahootIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kahoot"

    @property
    def original_file_name(self) -> "str":
        return "kahoot.svg"

    @property
    def title(self) -> "str":
        return "Kahoot!"

    @property
    def primary_color(self) -> "str":
        return "#46178F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kahoot!</title>
     <path d="M20.557 18.87l2.747-17.513L16.174 0zM.696
 2.348v19.078l4.035.14-.035-6.679 2.487-2.4 2.626 9.078h3.565L10.087
 9.722l4.957-5.444-3.496-1.339L4.73 9.443V1.322zm18.295 17.86l-.99
 2.331L20.12 24l2.088-1.235-.887-2.556Z" />
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
