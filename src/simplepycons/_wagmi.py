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


class WagmiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wagmi"

    @property
    def original_file_name(self) -> "str":
        return "wagmi.svg"

    @property
    def title(self) -> "str":
        return "Wagmi"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wagmi</title>
     <path d="M2.7391 13.2065c0 .7564.6132 1.3696 1.3696
 1.3696h2.7391c.7564 0 1.3696-.6132
 1.3696-1.3696V7.7283c0-.7564.6132-1.3696 1.3696-1.3696s1.3695.6132
 1.3695 1.3696v5.4782c0 .7564.6132 1.3696 1.3696 1.3696h2.7391c.7564 0
 1.3696-.6132 1.3696-1.3696V7.7283c0-.7564.6131-1.3696
 1.3695-1.3696s1.3696.6132 1.3696 1.3696v8.2174c0 .7564-.6132
 1.3695-1.3696 1.3695H1.3696C.6132 17.3152 0 16.7021 0
 15.9457V7.7283c0-.7564.6132-1.3696 1.3696-1.3696s1.3695.6132 1.3695
 1.3696zm19.4348 4.4348c1.0085 0 1.8261-.8176 1.8261-1.826
 0-1.0086-.8176-1.8262-1.826-1.8262-1.0086 0-1.8262.8176-1.8262 1.8261
 0 1.0085.8176 1.826 1.8261 1.826z" />
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
