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


class ScreencastifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "screencastify"

    @property
    def original_file_name(self) -> "str":
        return "screencastify.svg"

    @property
    def title(self) -> "str":
        return "Screencastify"

    @property
    def primary_color(self) -> "str":
        return "#FF8282"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Screencastify</title>
     <path d="M7.898 2.347c-.472.008-.914.38-.914.891v4.278H1.1c-.541
 0-1.1.437-1.1.978v7.02c0 .54.559.907 1.1.907h5.884V7.533h6.408c.542 0
 .926.437.926.979v1.623l3.667-2.095v7.927l-3.667-2.095v1.676c0
 .541-.384.908-.926.908H6.984v4.313c0 .68.786 1.1 1.38.768l9.638-5.535
 5.553-3.195c.593-.402.593-1.257 0-1.59l-5.553-3.194L8.364
 2.47a.886.886 0 00-.466-.123z" />
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
