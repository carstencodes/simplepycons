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


class PagseguroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pagseguro"

    @property
    def original_file_name(self) -> "str":
        return "pagseguro.svg"

    @property
    def title(self) -> "str":
        return "PagSeguro"

    @property
    def primary_color(self) -> "str":
        return "#FFC801"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PagSeguro</title>
     <path d="M17.482 9.712c1.64 0 3.108.69 4.1
 1.813.044-.388.087-.777.087-1.208C21.67 5.007 17.353.69 12 .69c-5.353
 0-9.67 4.316-9.67 9.626 0 .345 0 .69.044 1.036a8.688 8.688 0
 017.943-5.137c2.848 0 5.352 1.381 6.95 3.496h.215zm-7.122-2.72c-4.36
 0-7.9 3.54-7.9 7.9s3.54 7.9 7.9 7.9c2.158 0 4.1-.864 5.525-2.245a5.53
 5.53 0 01-3.928-5.31c0-2.676 1.9-4.92
 4.446-5.438-1.468-1.684-3.626-2.806-6.043-2.806zM4.79 21.583A11.958
 11.958 0 010 12C0 5.353 5.396 0 12 0s12 5.396 12 12-5.396 12-12
 12c-1.554
 0-3.022-.302-4.36-.82-1.079-.389-2.028-.907-2.849-1.597zm12.777-1.51a4.827
 4.827 0 004.835-4.835 4.827 4.827 0 00-4.835-4.834 4.827 4.827 0
 00-4.834 4.834 4.827 4.827 0 004.834 4.835Z" />
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
