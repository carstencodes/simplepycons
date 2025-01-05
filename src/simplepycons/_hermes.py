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


class HermesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hermes"

    @property
    def original_file_name(self) -> "str":
        return "hermes.svg"

    @property
    def title(self) -> "str":
        return "Hermes"

    @property
    def primary_color(self) -> "str":
        return "#0091CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hermes</title>
     <path d="m21.818 4.516-1.05 4.148h2.175L24 4.516M19.41
 14.04h2.17l1.04-4.08h-2.178m-2.41
 9.523h2.154l1.056-4.147h-2.16m.193-5.377H5.55v.92l3.341
 3.161h9.349m2.41-9.525H0v1.116l3.206 3.032H19.6m-8.372 7.58 3.43
 3.24h2.205l1.05-4.147h-6.685" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.myhermes.de/assets/touchicons/fav'''

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
