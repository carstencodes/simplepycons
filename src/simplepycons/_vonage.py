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


class VonageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vonage"

    @property
    def original_file_name(self) -> "str":
        return "vonage.svg"

    @property
    def title(self) -> "str":
        return "Vonage"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vonage</title>
     <path d="M9.279 11.617l-4.54-10.07H0l6.797 15.296a.084.084 0 0 0
 .153 0zm9.898-10.07s-6.148 13.868-6.917 15.565c-1.838 4.056-3.2
 5.07-4.588 5.289a.026.026 0 0 0 .004.052h4.34c1.911 0 3.219-1.285
 5.06-5.341C17.72 15.694 24 1.547 24 1.547z" />
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
