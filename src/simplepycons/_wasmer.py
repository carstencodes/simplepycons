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


class WasmerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wasmer"

    @property
    def original_file_name(self) -> "str":
        return "wasmer.svg"

    @property
    def title(self) -> "str":
        return "Wasmer"

    @property
    def primary_color(self) -> "str":
        return "#4946DD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wasmer</title>
     <path d="M18.111 3.537c-.011.822-.5
 1.208-1.111.86-.611-.353-1.106-1.307-1.111-2.146L12 0v4.651l5.561
 3.222.55.32v7.763L22 18.206V5.794l-3.889-2.256Zm-5 3.034c-.011.822-.5
 1.208-1.111.86-.611-.352-1.106-1.307-1.111-2.145l-3.89-2.252V7.41l5.562
 3.222.55.32v8.038L17 21.241V8.828L13.11 6.57Zm-5 2.759c-.011.822-.5
 1.208-1.111.86-.611-.353-1.106-1.307-1.111-2.146L2 5.794v12.413L12
 24V11.586L8.111 9.33Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/wasmerio/wasmer.io/blob/0d'''

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
