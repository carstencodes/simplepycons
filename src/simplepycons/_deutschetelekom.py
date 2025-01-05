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


class DeutscheTelekomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deutschetelekom"

    @property
    def original_file_name(self) -> "str":
        return "deutschetelekom.svg"

    @property
    def title(self) -> "str":
        return "Deutsche Telekom"

    @property
    def primary_color(self) -> "str":
        return "#E20074"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deutsche Telekom</title>
     <path d="M6.722 15.84h-4.8v-4.8h4.791v4.8zM1.922
 0v8.16H3.36v-.236c0-3.844 2.159-6.24 6.239-6.24h.237v17.279c0
 2.396-.957 3.36-3.36 3.36h-.72V24h12.478v-1.676h-.72c-2.395
 0-3.36-.957-3.36-3.361V1.676h.237c4.08 0 6.239 2.396 6.239
 6.24v.236h1.439V0Zm15.356 15.84h4.8v-4.8h-4.791v4.8z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://tmap.t-mobile.com/portals/pro74u7a/EX'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://tmap.t-mobile.com/portals/pro74u7a/EX'''

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
        yield from [
            "T-Mobile",
        ]
