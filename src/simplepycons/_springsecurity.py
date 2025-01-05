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


class SpringSecurityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "springsecurity"

    @property
    def original_file_name(self) -> "str":
        return "springsecurity.svg"

    @property
    def title(self) -> "str":
        return "Spring Security"

    @property
    def primary_color(self) -> "str":
        return "#6DB33F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spring Security</title>
     <path d="M20.59 2.066 11.993 0 3.41 2.066v6.612h4.557a3.804 3.804
 0 0 0 0 .954H3.41v3.106C3.41 19.867 11.994 24 11.994 24s8.582-4.133
 8.582-11.258V9.635h-4.545a3.616 3.616 0 0 0 0-.954h4.558zM12
 12.262h-.006a3.109 3.109 0 1 1 .006 0zm-.006-4.579a.804.804 0 0 0-.37
 1.52v.208l.238.237v.159l.159.159v.159l-.14.14.15.246v.159l-.16.189.223.222.246-.246V9.218a.804.804
 0 0 0-.346-1.535zm0 .836a.299.299 0 1 1 .298-.299.299.299 0 0
 1-.298.3z" />
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
