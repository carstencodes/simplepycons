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


class JetbrainsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jetbrains"

    @property
    def original_file_name(self) -> "str":
        return "jetbrains.svg"

    @property
    def title(self) -> "str":
        return "JetBrains"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JetBrains</title>
     <path d="M2.345 23.997A2.347 2.347 0 0 1 0 21.652V10.988C0
 9.665.535 8.37 1.473 7.433l5.965-5.961A5.01 5.01 0 0 1 10.989
 0h10.666A2.347 2.347 0 0 1 24 2.345v10.664a5.056 5.056 0 0 1-1.473
 3.554l-5.965 5.965A5.017 5.017 0 0 1 13.007
 24v-.003H2.345Zm8.969-6.854H5.486v1.371h5.828v-1.371ZM3.963
 6.514h13.523v13.519l4.257-4.257a3.936 3.936 0 0 0
 1.146-2.767V2.345c0-.678-.552-1.234-1.234-1.234H10.989a3.897 3.897 0
 0 0-2.767 1.145L3.963 6.514Zm-.192.192L2.256 8.22a3.944 3.944 0 0
 0-1.145 2.768v10.664c0 .678.552 1.234 1.234 1.234h10.666a3.9 3.9 0 0
 0 2.767-1.146l1.512-1.511H3.771V6.706Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.jetbrains.com/company/brand/logos'''

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
