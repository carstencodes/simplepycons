#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class WebAwesomeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webawesome"

    @property
    def original_file_name(self) -> "str":
        return "webawesome.svg"

    @property
    def title(self) -> "str":
        return "Web Awesome"

    @property
    def primary_color(self) -> "str":
        return "#F36944"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Web Awesome</title>
     <path d="M13.958 4.95c0 .783-.465 1.462-1.132 1.77L16.8
 10.2l3.914-.784A1.8 1.8 0 0 1 20.4 8.4a1.8 1.8 0 1 1 1.86 1.8l-4.221
 9.385A2.4 2.4 0 0 1 15.849 21H8.153c-.945
 0-1.8-.555-2.19-1.414l-4.221-9.384a1.8 1.8 0 1 1 1.545-.784L7.2
 10.2l3.98-3.484a1.95 1.95 0 0 1-1.125-1.766 1.95 1.95 0 0 1 3.9 0z"
 />
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
