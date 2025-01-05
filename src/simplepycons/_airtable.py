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


class AirtableIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airtable"

    @property
    def original_file_name(self) -> "str":
        return "airtable.svg"

    @property
    def title(self) -> "str":
        return "Airtable"

    @property
    def primary_color(self) -> "str":
        return "#18BFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Airtable</title>
     <path d="M11.992 1.966c-.434 0-.87.086-1.28.257L1.779
 5.917c-.503.208-.49.908.012 1.116l8.982 3.558a3.266 3.266 0 0 0 2.454
 0l8.982-3.558c.503-.196.503-.908.012-1.116l-8.957-3.694a3.255 3.255 0
 0 0-1.272-.257zM23.4 8.056a.589.589 0 0 0-.222.045l-10.012
 3.877a.612.612 0 0 0-.38.564v8.896a.6.6 0 0 0 .821.552L23.62
 18.1a.583.583 0 0 0 .38-.551V8.653a.6.6 0 0 0-.6-.596zM.676
 8.095a.644.644 0 0 0-.48.19C.086 8.396 0 8.53 0 8.69v8.355c0
 .442.515.737.908.54l6.27-3.006.307-.147
 2.969-1.436c.466-.22.43-.908-.061-1.092L.883 8.138a.57.57 0 0
 0-.207-.044z" />
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
