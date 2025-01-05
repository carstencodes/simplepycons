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


class BitdefenderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitdefender"

    @property
    def original_file_name(self) -> "str":
        return "bitdefender.svg"

    @property
    def title(self) -> "str":
        return "Bitdefender"

    @property
    def primary_color(self) -> "str":
        return "#ED1C24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitdefender</title>
     <path d="M1.685 0v.357l1.232 1.046c1.477 1.204 1.67 1.439 1.67
 2.526V24h8.646c4.537 0 9.083-1.629 9.083-6.849
 0-3.082-2.174-5.458-5.186-5.797v-.067c2.475-.745 4.169-2.54
 4.169-5.253 0-4.372-3.73-6.032-7.349-6.032L1.686 0zm7.176
 3.664h3.524c2.383 0 3.121.327 3.844 1.013.548.521.799 1.237.801 2.07
 0 .775-.267 1.466-.831 2.004-.705.676-1.674 1.011-3.443
 1.011H8.862V3.664zm0 9.758h4.099c3.456 0 5.085.881 5.085 3.39 0
 3.153-3.055 3.526-5.256 3.526H8.86v-6.916z" />
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
