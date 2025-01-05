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


class NumpyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "numpy"

    @property
    def original_file_name(self) -> "str":
        return "numpy.svg"

    @property
    def title(self) -> "str":
        return "NumPy"

    @property
    def primary_color(self) -> "str":
        return "#013243"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NumPy</title>
     <path d="M10.315 4.876L6.3048 2.8517l-4.401 2.1965 4.1186
 2.0683zm1.8381.9277l4.2045 2.1223-4.3622
 2.1906-4.125-2.0718zm5.6153-2.9213l4.3193 2.1658-3.863
 1.9402-4.2131-2.1252zm-1.859-.9329L12.021 0 8.1742 1.9193l4.0068
 2.0208zm-3.0401
 16.7443V24l4.7107-2.3507-.0053-5.3085zm4.7037-4.2057l-.0052-5.2528-4.6985
 2.3356v5.2546zm5.6553-.9845v5.327l-4.0178
 2.0052-.0029-5.3028zm0-1.8626V6.4214l-4.0253 2.001.0034
 5.2633zM11.2062 11.571L8.0333
 9.9756v6.895s-3.8804-8.2564-4.2399-8.998c-.0463-.0957-.2371-.2007-.2858-.2262C2.8118
 7.2812.773 6.2485.773 6.2485V18.43l2.8204 1.5076v-6.3674s3.8392
 7.3775 3.878 7.458c.0389.0807.4245.8582.8362 1.1314.5485.363 2.8992
 1.7766 2.8992 1.7766z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/numpy/numpy/blob/main/bran'''
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
