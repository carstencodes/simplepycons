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


class CoderwallIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coderwall"

    @property
    def original_file_name(self) -> "str":
        return "coderwall.svg"

    @property
    def title(self) -> "str":
        return "Coderwall"

    @property
    def primary_color(self) -> "str":
        return "#3E8DCC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coderwall</title>
     <path d="M21.354 18.708c1.46 0 2.646 1.185 2.646 2.646C24 22.814
 22.814 24 21.354 24s-2.646-1.186-2.646-2.646c0-1.458 1.185-2.646
 2.646-2.646zM12 9.354c1.46 0 2.646 1.186 2.646 2.646S13.46 14.646 12
 14.646 9.354 13.46 9.354 12 10.54 9.354 12 9.354zm9.354 0C22.814
 9.354 24 10.54 24 12s-1.186 2.646-2.646 2.646S18.708 13.46 18.708
 12s1.185-2.646 2.646-2.646zM12 0c1.46 0 2.646 1.185 2.646 2.646 0
 1.46-1.186 2.646-2.646 2.646S9.354 4.106 9.354 2.646 10.54 0 12
 0zM2.646 0c1.46 0 2.646 1.185 2.646 2.646 0 1.46-1.186 2.646-2.646
 2.646S0 4.106 0 2.646 1.186 0 2.646 0zm18.708 0C22.814 0 24 1.185 24
 2.646c0 1.46-1.186 2.646-2.646 2.646s-2.646-1.186-2.646-2.646S19.893
 0 21.354 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/twolfson/coderwall-svg/tre'''

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
