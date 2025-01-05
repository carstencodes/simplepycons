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


class IssuuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "issuu"

    @property
    def original_file_name(self) -> "str":
        return "issuu.svg"

    @property
    def title(self) -> "str":
        return "Issuu"

    @property
    def primary_color(self) -> "str":
        return "#F36D5D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Issuu</title>
     <path d="M.996 0A.998.998 0 0 0 0 .996V12c0 6.628 5.372 12 12
 12s12-5.372 12-12S18.628 0 12 0H.996zm11.17 3.582a8.333 8.333 0 0 1
 8.254 8.41 8.333 8.333 0 0 1-8.41
 8.252c-4.597-.045-8.296-3.81-8.254-8.41.045-4.6 3.81-8.296
 8.41-8.252zm-.031 2.27a6.107 6.107 0 0 0-6.155 6.046 6.109 6.109 0 0
 0 6.05 6.163 6.099 6.099 0 0 0 6.154-6.047 6.107 6.107 0 0
 0-6.041-6.162h-.008zm-.02 3.013a3.098 3.098 0 0 1 3.063 3.123 3.088
 3.088 0 0 1-3.121 3.06l.002-.001a3.091 3.091 0 0 1 .056-6.182z" />
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
