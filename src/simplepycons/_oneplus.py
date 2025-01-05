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


class OneplusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oneplus"

    @property
    def original_file_name(self) -> "str":
        return "oneplus.svg"

    @property
    def title(self) -> "str":
        return "OnePlus"

    @property
    def primary_color(self) -> "str":
        return "#F5010C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OnePlus</title>
     <path d="M0
 3.74V24h20.26V12.428h-2.256v9.317H2.254V5.995h9.318V3.742zM18.004
 0v3.74h-3.758v2.256h3.758v3.758h2.255V5.996H24V3.74h-3.758V0zm-6.45
 18.756V8.862H9.562c0 .682-.228 1.189-.577
 1.504-.367.297-.91.437-1.556.437h-.245v1.625h2.133v6.31h2.237z" />
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
