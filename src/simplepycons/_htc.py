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


class HtcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "htc"

    @property
    def original_file_name(self) -> "str":
        return "htc.svg"

    @property
    def title(self) -> "str":
        return "HTC"

    @property
    def primary_color(self) -> "str":
        return "#A5CF4C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HTC</title>
     <path d="M22
 14.75h-2.8c-.7-.05-1.15-.5-1.2-1.15v-1.15c.05-.65.6-1.25
 1.2-1.25H24V9.95h-4.85c-.65.05-1.25.25-1.7.7-.4.4-.65 1.1-.7 1.75 0
 .35-.05.85 0 1.15.05.75.3 1.3.7 1.7.4.45 1.05.7 1.7.7H24V14.7c0
 .05-1.3.05-2 .05M8.5 10v1.25h2.95v4.7h1.25v-4.7h2.95V10Zm-1.3
 2.35c0-.65-.25-1.25-.7-1.7-.5-.5-1.2-.7-1.7-.7H2.35c-.55
 0-.95.2-1.15.35V8H0v8h1.25v-3.6c.05-.65.55-1.15 1.15-1.2.5-.05
 1.95-.05 2.4 0 .65.05 1.1.55 1.15 1.2V16H7.2z" />
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
