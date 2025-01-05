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


class MilanoteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "milanote"

    @property
    def original_file_name(self) -> "str":
        return "milanote.svg"

    @property
    def title(self) -> "str":
        return "Milanote"

    @property
    def primary_color(self) -> "str":
        return "#31303A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Milanote</title>
     <path d="M12 0c6.627 0 12 5.373 12 12s-5.373 12-12 12S0 18.627 0
 12 5.373 0 12 0Zm0 12.943L15.057 16H8.943Zm4-4v6.114L12.943 12Zm-8
 6.114V8.943L11.057 12Zm8.917 2.227a.665.665 0 0 0
 .367-.367l-.003.009a.665.665 0 0 0 .052-.26V7.334a.667.667 0 0
 0-1.138-.471L12 11.057 7.805 6.862a.667.667 0 0
 0-1.138.471v9.334a.667.667 0 0 0 .666.666h9.334c.092 0
 .18-.018.26-.052l-.01.004z" />
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
