#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class FlydotioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flydotio"

    @property
    def original_file_name(self) -> "str":
        return "flydotio.svg"

    @property
    def title(self) -> "str":
        return "Fly.io"

    @property
    def primary_color(self) -> "str":
        return "#24175B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fly.io</title>
     <path d="M11.987 0c-2.45-.01-5.002.925-6.541 2.897-1.17
 1.502-1.664 3.474-1.49 5.356.29 2.112 1.476 3.96 2.676 5.672a41.5
 41.5 0 0 0 4.216 4.831c-1.063.832-1.943 2.286-1.357 3.644.821 2.32
 4.665 2.05 5.122-.372.39-1.288-.694-2.533-1.428-3.309 2.388-2.431
 4.706-5.036
 6.17-8.145.595-1.32.902-2.802.614-4.24-.28-2.341-1.823-4.473-3.967-5.46C14.76.266
 13.364.016 11.987 0m-.236 1.577v15.534C9.881 13.483 7.724 9.266 8.73
 5.069c.35-1.539 1.253-3.309 3.02-3.492m1.996.04c1.534.357 3.031 1.096
 3.906 2.48 1.3 1.93 1.318 4.55.1 6.521-1.268 2.395-3.06 4.463-4.916
 6.415 1.472-2.974 3.074-6.106
 3.182-9.5-.043-2.08-.438-4.612-2.272-5.916M11.97 20.103c.848.342
 1.597 1.983.153
 2.173-.664.15-1.367-.599-.995-1.222.213-.355.488-.73.842-.95" />
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
