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


class BuzzfeedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "buzzfeed"

    @property
    def original_file_name(self) -> "str":
        return "buzzfeed.svg"

    @property
    def title(self) -> "str":
        return "BuzzFeed"

    @property
    def primary_color(self) -> "str":
        return "#EE3322"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BuzzFeed</title>
     <path d="M24 12c0 6.627-5.373 12-12 12S0 18.627 0 12 5.373 0 12
 0s12 5.373 12 12zm-4.148-.273l-.977-6.94-6.5 2.624 2.575 1.487-2.435
 4.215L8.3 10.68l-4.153 7.19 2.327 1.346 2.812-4.868L13.5
 16.78l3.777-6.54 2.575 1.487z" />
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
