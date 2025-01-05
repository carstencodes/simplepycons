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


class MockServiceWorkerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mockserviceworker"

    @property
    def original_file_name(self) -> "str":
        return "mockserviceworker.svg"

    @property
    def title(self) -> "str":
        return "Mock Service Worker"

    @property
    def primary_color(self) -> "str":
        return "#FF6A33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mock Service Worker</title>
     <path d="M4.5 0A4.49 4.49 0 0 0 0 4.5v15A4.49 4.49 0 0 0 4.5
 24h15a4.49 4.49 0 0 0 4.5-4.5v-15A4.49 4.49 0 0 0 19.5 0Zm1.633 4.43
 11.715.013c.623.001 1.208.26 1.62.674.414.414.671 1 .67
 1.623v.086l-1.224 11.799a2.31 2.31 0 0 1-.836 1.545 2.293 2.293 0 0
 1-3.15-.246L4.426 8.262a2.31 2.31 0 0 1-.586-1.657A2.295 2.295 0 0 1
 6.133 4.43Zm2.363 3.35 7.334 8.146.844-8.137zm1.123.501 3.244.004
 2.92 3.244-.336 3.227zM4.678 9.287l3.017 3.354-.369 3.57 3.588.004
 3.018 3.351-7.78-.01c-.623
 0-1.208-.26-1.62-.673-.414-.414-.671-1-.67-1.623v-.086z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mswjs/msw/blob/9c53bd23040'''

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
