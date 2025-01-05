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


class BemIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bem"

    @property
    def original_file_name(self) -> "str":
        return "bem.svg"

    @property
    def title(self) -> "str":
        return "BEM"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BEM</title>
     <path d="M0 5.163h5.61v1.65H0Zm0-3.065h5.61v1.65H0Zm10.067
 6.106H0v1.65h9.69c1.06 0 3.536.024 4.455
 1.51v-.92c-.448-1.462-1.768-2.24-4.078-2.24Zm.023
 3.065H0v1.65h9.69c2.357 0 3.842.095
 4.455.425v-.731c-.471-1.155-2.451-1.344-4.055-1.344Zm-.023
 7.78H0V17.4h9.69c1.06 0 3.536-.024 4.455-1.509v.92c-.448 1.461-1.768
 2.24-4.078 2.24zm.023-3.065H0v-1.65h9.69c2.357 0 3.842-.094
 4.455-.424v.73c-.471 1.156-2.451 1.344-4.055 1.344zm6.507
 5.918H24v-1.014h-7.19c-.637 0-2.146-.023-2.688-.896v.566c.26.872 1.06
 1.344 2.475 1.344zm-.023-1.863h7.403v-1.013H16.81c-1.439
 0-2.334-.047-2.688-.26v.448c.283.708 1.485.825 2.452.825z" />
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
