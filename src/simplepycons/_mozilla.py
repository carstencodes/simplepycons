#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class MozillaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mozilla"

    @property
    def original_file_name(self) -> "str":
        return "mozilla.svg"

    @property
    def title(self) -> "str":
        return "Mozilla"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mozilla</title>
     <path d="M0 0v24h24V0zm10.13 6.706c1.481 0 2.858.706 3.352
 2.224.565-1.377 1.73-2.224 3.353-2.224 1.87 0 3.565 1.13 3.565
 3.564v4.765h1.412v2.26h-4.341v-5.86c0-1.8-.6-2.47-1.765-2.47-1.412
 0-1.976 1.024-1.976
 2.435V15h1.376v2.259h-4.341v-5.824c0-1.8-.6-2.47-1.765-2.47-1.412
 0-1.976 1.024-1.976
 2.435V15H9v2.259H2.647V15h1.377V9.176H2.647V6.918H6.99V8.47c.635-1.095
 1.693-1.765 3.14-1.765z" />
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
