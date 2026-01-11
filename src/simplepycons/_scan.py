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


class ScanIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scan"

    @property
    def original_file_name(self) -> "str":
        return "scan.svg"

    @property
    def title(self) -> "str":
        return "Scan"

    @property
    def primary_color(self) -> "str":
        return "#004C97"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scan</title>
     <path d="M23.363 9.13a5.8 5.8 0 0 1 0 5.285l-3.376 5.948a6.11
 6.11 0 0 1-4.603 2.853h-6.76a6.09 6.09 0 0
 1-4.605-2.83l-3.384-6.03a5.8 5.8 0 0 1 0-5.276l3.384-5.806A5.73 5.73
 0 0 1 8.623.784h6.76a5.74 5.74 0 0 1 4.605 2.49zm-14.47 5.94a2.22
 2.22 0 0 0-1.542.73 5.41 5.41 0 0 0 4.43 2.44 4.305 4.305 0 0 0
 4.886-3.716c.124-3.02-2.04-3.834-4.264-4.248-1.12-.232-2.207-.382-2.207-1.427
 0-.888.946-1.26 1.95-1.26a2.49 2.49 0 0 1 2.132 1.21l2.182-1.46a4.98
 4.98 0 0 0-4.314-2.256c-2.298 0-4.513 1.27-4.662 3.683 0 2.821 2.04
 3.759 4.048 4.066 1.319.183 2.489.43 2.489 1.535 0 1.302-1.012
 1.6-2.15 1.6-1.658 0-1.658-.88-2.92-.88" />
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
