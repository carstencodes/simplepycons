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


class BitlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitly"

    @property
    def original_file_name(self) -> "str":
        return "bitly.svg"

    @property
    def title(self) -> "str":
        return "Bitly"

    @property
    def primary_color(self) -> "str":
        return "#EE6123"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitly</title>
     <path d="M13.055
 21.26c-1.345.022-2.325-.41-2.386-1.585-.025-.44-.018-.91.002-1.192.137-1.716
 1.333-2.95 2.53-3.19 1.482-.294 2.455.38 2.455 2.31 0 1.303-.36
 3.618-2.59 3.657h-.016zM11.923 0C5.32 0 0 5.297 0 12.224c0 3.594 1.92
 7.062 4.623 9.147.52.4 1.138.367
 1.497.02.297-.285.272-.984-.285-1.475-2.16-1.886-3.652-4.76-3.652-7.635
 0-5.15 4.58-9.49 9.74-9.49 6.28 0 9.636 5.102 9.636 9.43 0 2.65-1.29
 5.84-3.626 7.874.015 0 .493-.942.493-2.784
 0-3.13-1.976-4.836-4.28-4.836-1.663 0-2.667.598-3.34 1.152
 0-1.272.045-3.652.045-3.652
 0-1.572-.54-2.83-2.47-2.86-1.11-.015-1.932.493-2.44
 1.647-.18.436-.12.916.254 1.125.3.18.81.046
 1.046-.284.165-.21.254-.254.404-.24.24.03.257.405.257.66.014.193.193
 2.903.088 9.865C7.98 21.798 9.493 24 13.1 24c1.56 0 2.756-.435
 4.493-1.422C20.243 21.08 24 17.758 24 12.128 23.953 5.045 18.265 0
 11.933 0" />
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
