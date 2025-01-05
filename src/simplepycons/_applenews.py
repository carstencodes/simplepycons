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


class AppleNewsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "applenews"

    @property
    def original_file_name(self) -> "str":
        return "applenews.svg"

    @property
    def title(self) -> "str":
        return "Apple News"

    @property
    def primary_color(self) -> "str":
        return "#FD415E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apple News</title>
     <path d="M0 12.9401c2.726 4.6726 6.3944 8.385 11.039
 11.0582H1.4164C.634 23.9983 0 23.3639 0 22.5819v-9.6418ZM0 1.4138C0
 .6337.632.0018 1.4116.0018h4.8082L24 17.7583v4.773c0
 .3891-.1544.762-.4295 1.0373a1.4674 1.4674 0 0 1-1.037.4296h-4.774L0
 6.2416M12.9634.0017h9.6182A1.4187 1.4187 0 0 1 24
 1.4205v9.6256C21.2648 6.4935 17.6157 2.7745 12.9634.0017Z" />
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
