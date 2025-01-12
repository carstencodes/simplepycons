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


class VZeroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "v0"

    @property
    def original_file_name(self) -> "str":
        return "v0.svg"

    @property
    def title(self) -> "str":
        return "v0"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>v0</title>
     <path d="M14.066 6.028v2.22h5.729q.075-.001.148.005l-5.853
 5.752a2 2 0 0 1-.024-.309V8.247h-2.353v5.45c0 2.322 1.935 4.222 4.258
 4.222h5.675v-2.22h-5.675q-.03
 0-.059-.003l5.729-5.629q.006.082.006.166v5.465H24v-5.465a4.204 4.204
 0 0 0-4.205-4.205zM0 8.245l8.28 9.266c.839.94 2.396.346
 2.396-.914V8.245H8.19v5.44l-4.86-5.44Z" />
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
