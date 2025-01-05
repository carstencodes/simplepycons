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


class CommaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "comma"

    @property
    def original_file_name(self) -> "str":
        return "comma.svg"

    @property
    def title(self) -> "str":
        return "comma"

    @property
    def primary_color(self) -> "str":
        return "#51FF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>comma</title>
     <path d="M6.72682
 24c0-.55531-.0434-1.02051.02045-1.46891.0272-.1912.25037-.39595.43237-.51143.88731-.56315
 1.85122-1.01275 2.67734-1.65857 2.67584-2.09206 4.26201-4.84612
 4.3487-8.42366.02452-1.01583-.34891-1.2696-1.20211-.87389-2.4628
 1.1424-5.11119.47263-6.5246-1.65034-1.54137-2.3155-1.32431-5.3984.52253-7.4211
 2.359-2.58344 6.24053-2.66074 8.91722-.19346 1.60337 1.47794 2.3652
 3.38627 2.5552 5.5569.63691 7.27188-3.01046 13.2657-9.64881
 15.89874-.657.26045-1.3307.4744-2.09828.74571" />
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
