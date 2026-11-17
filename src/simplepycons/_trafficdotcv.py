#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TrafficdotcvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trafficdotcv"

    @property
    def original_file_name(self) -> "str":
        return "trafficdotcv.svg"

    @property
    def title(self) -> "str":
        return "Traffic.cv"

    @property
    def primary_color(self) -> "str":
        return "#635BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Traffic.cv</title>
     <path d="M3.136 0A3.115 3.115 0 0 0 0 3.136v17.728A3.114 3.114 0
 0 0 3.136 24h17.728A3.115 3.115 0 0 0 24 20.864V3.136A3.115 3.115 0 0
 0 20.864 0Zm11.947 7.147 3.861.213a1.067 1.067 0 0 1 1.045 1.024l.214
 3.861a1.067 1.067 0 0 1-1.067 1.152 1.067 1.067 0 0
 1-1.11-1.024l-.106-1.322-3.67 3.882a1.067 1.067 0 0
 1-1.493.107l-2.346-1.963-3.52 3.67v.042a1.557 1.557 0 0 1-1.579 1.579
 1.557 1.557 0 0 1-1.557-1.579 1.557 1.557 0 0 1
 1.578-1.557l4.203-4.416a1.067 1.067 0 0 1 1.493-.085l2.347 1.962
 3.05-3.306-1.471-.043a1.067 1.067 0 0 1-1.003-1.152 1.067 1.067 0 0 1
 1.13-1.045" />
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
