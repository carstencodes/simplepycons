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


class AppleTvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appletv"

    @property
    def original_file_name(self) -> "str":
        return "appletv.svg"

    @property
    def title(self) -> "str":
        return "Apple TV"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apple TV</title>
     <path d="M20.57 17.735h-1.815l-3.34-9.203h1.633l2.02
 5.987c.075.231.273.9.586 2.012l.297-.997.33-1.006
 2.094-6.004H24zm-5.344-.066a5.76 5.76 0 0 1-1.55.207c-1.23
 0-1.84-.693-1.84-2.087V9.646h-1.063V8.532h1.121V7.081l1.476-.602v2.062h1.707v1.113H13.38v5.805c0
 .446.074.75.214.932.14.182.396.264.75.264.207 0
 .495-.041.883-.115zm-7.29-5.343c.017 1.764 1.55 2.358 1.567
 2.366-.017.042-.248.842-.808 1.658-.487.71-.99 1.418-1.79
 1.435-.783.016-1.03-.462-1.93-.462-.89
 0-1.17.445-1.913.478-.758.025-1.344-.775-1.838-1.484-.998-1.451-1.765-4.098-.734-5.88.51-.89
 1.426-1.451 2.416-1.46.75-.016 1.468.512 1.93.512.461 0 1.327-.627
 2.234-.536.38.016 1.452.157 2.136 1.154-.058.033-1.278.743-1.27
 2.219M6.468
 7.988c.404-.495.685-1.18.61-1.864-.585.025-1.294.388-1.723.883-.38.437-.71
 1.138-.619 1.806.652.05 1.328-.338 1.732-.825Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Apple_TV_('''

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
