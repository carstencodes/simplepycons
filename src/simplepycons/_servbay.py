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


class ServbayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "servbay"

    @property
    def original_file_name(self) -> "str":
        return "servbay.svg"

    @property
    def title(self) -> "str":
        return "ServBay"

    @property
    def primary_color(self) -> "str":
        return "#00103C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ServBay</title>
     <path d="M14.201.028a.505.505 0 0 1
 .643.313c.04.11.043.23.006.341l-2.258 6.356a.512.512 0 0 1-.319.302L1
 11.168l2.665-7.33a.513.513 0 0 1 .319-.302L14.2.028h.001ZM1
 11.757l2.776 4.05a.55.55 0 0 0 .622.227l5.12-1.892a.483.483 0 0 0
 .29-.653l-.03-.063L7.412 9.62 1 11.756Zm8.799 12.215a.505.505 0 0
 1-.643-.312.517.517 0 0 1-.006-.342l2.235-6.365a.513.513 0 0 1
 .319-.3L23 12.832l-2.665 7.33a.51.51 0 0 1-.318.3l-10.218
 3.51v-.001ZM20.437 8.079a.55.55 0 0 0-.622-.226l-5.12 1.893a.483.483
 0 0 0-.29.65l.03.064 2.336 3.85 6.215-2.12-2.55-4.11h.001Z" />
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
