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


class HtmxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "htmx"

    @property
    def original_file_name(self) -> "str":
        return "htmx.svg"

    @property
    def title(self) -> "str":
        return "htmx"

    @property
    def primary_color(self) -> "str":
        return "#3366CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>htmx</title>
     <path d="M0 13.01v-2l7.09-2.98.58 1.94-5.1 2.05 5.16 2.05-.63
 1.9Zm16.37 1.03 5.18-2-5.16-2.09.65-1.88L24 10.95v2.12L17
 16zm-2.85-9.98H16l-5.47 15.88H8.05Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/bigskysoftware/htmx/blob/f'''

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
