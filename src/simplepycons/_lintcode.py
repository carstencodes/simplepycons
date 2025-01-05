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


class LintcodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lintcode"

    @property
    def original_file_name(self) -> "str":
        return "lintcode.svg"

    @property
    def title(self) -> "str":
        return "LintCode"

    @property
    def primary_color(self) -> "str":
        return "#13B4FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LintCode</title>
     <path d="M11.11 0 5.064 10.467l4.797 6.142
 1.322-2.289-3.149-4.032 4.722-8.184A902.354 902.354 0 0 0 11.11
 0Zm3.029 7.391L12.817 9.68l3.148 4.032-4.721 8.184c.546.703 1.095
 1.404 1.646 2.104l6.045-10.469-4.796-6.14Z" />
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
