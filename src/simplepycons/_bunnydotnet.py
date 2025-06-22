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


class BunnydotnetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bunnydotnet"

    @property
    def original_file_name(self) -> "str":
        return "bunnydotnet.svg"

    @property
    def title(self) -> "str":
        return "bunny.net"

    @property
    def primary_color(self) -> "str":
        return "#FFAA49"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>bunny.net</title>
     <path d="m12.978 3.828 5.642 3.104L13.436 0c-.86 1.126-1.033
 2.59-.459 3.828ZM10.398 15.03c.688 0 1.262.563 1.262 1.294 0
 .676-.574 1.239-1.32 1.239-.688
 0-1.261-.563-1.261-1.239.057-.675.63-1.294 1.32-1.294ZM6.497
 1.033l15.832 8.444c.402.169.516.62.344 1.013a.512.512 0 0 1-.344.338
 10.919 10.919 0 0 1-3.9 1.463l-3.328 6.643s-1.032 2.308-3.9
 1.407c1.204-1.182 2.638-2.252 2.638-4.053
 0-1.914-1.549-3.434-3.499-3.434-1.95 0-3.5 1.52-3.5 3.434 0 2.364
 2.41 3.378 3.73 5.01.573.844.516 1.97-.173
 2.702-1.606-1.576-4.76-4.278-6.08-6.023a5.55 5.55 0 0
 1-1.147-3.096c.114-2.477 1.835-4.616 4.244-5.348.746-.225 1.492-.281
 2.238-.281 1.032.056 2.065.394 2.983.9 1.434.789 2.065.62
 3.04-.225.573-.45 1.204-1.97.23-2.308a6.096 6.096 0 0
 0-.976-.225C13.152 7.056 9.994 6.72 8.847 6.1 7.01 5.087 5.749 3.003
 6.497 1.034ZM2.46 8.656c.631 0 1.21.516 1.21 1.187v1.186H2.46c-.631
 0-1.21-.516-1.21-1.186 0-.62.526-1.187 1.21-1.187Z" />
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
