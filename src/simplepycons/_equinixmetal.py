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


class EquinixMetalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "equinixmetal"

    @property
    def original_file_name(self) -> "str":
        return "equinixmetal.svg"

    @property
    def title(self) -> "str":
        return "Equinix Metal"

    @property
    def primary_color(self) -> "str":
        return "#ED2224"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Equinix Metal</title>
     <path d="M22.399 7.789v7.005l-1.599.56V7.231L16
 5.557v11.472l-1.601.557V4.996L12
 4.16l-2.4.836v12.59l-1.599-.557V5.557L3.2
 7.232v8.121l-1.599-.56V7.79L0 8.349v7.582l4.801
 1.676v-9.24l1.6-.558v10.356L11.2
 19.84V6.133l.8-.28.8.28v13.708l4.801-1.676V7.809l1.599.558v9.24L24
 15.93V8.349z" />
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
