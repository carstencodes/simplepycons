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


class CheckmkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "checkmk"

    @property
    def original_file_name(self) -> "str":
        return "checkmk.svg"

    @property
    def title(self) -> "str":
        return "Checkmk"

    @property
    def primary_color(self) -> "str":
        return "#15D1A0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Checkmk</title>
     <path d="M5.187 8.738v3.985l4.883-3.157v8.217l1.925 1.111
 1.926-1.111V9.57l4.882 3.158V8.742l-6.808-4.269-6.808 4.265zM12
 0l10.375 5.999V18L12 24 1.625 18.006V6.003L12 0z" />
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
