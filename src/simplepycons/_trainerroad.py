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


class TrainerroadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trainerroad"

    @property
    def original_file_name(self) -> "str":
        return "trainerroad.svg"

    @property
    def title(self) -> "str":
        return "TrainerRoad"

    @property
    def primary_color(self) -> "str":
        return "#DA291C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TrainerRoad</title>
     <path d="M20.289 14.039c.157-.064.44-.199.51-.234 1.105-.56
 1.92-1.222 2.42-1.966.527-.756.8-1.658.78-2.579
 0-1.253-.456-2.193-1.398-2.874-.922-.668-2.225-.971-3.874-1.012H1.357L0
 8.421h5.528c.014 0 .028.005.038.016a.02.02 0 01.004.019L2.785
 16.85h3.668c.063 0 .12-.041.14-.102l2.759-8.303a.043.043 0
 01.042-.024l2.823.001c.014 0 .028.005.038.015a.02.02 0
 01.004.019L9.473 16.85h3.669c.064 0
 .12-.042.14-.103l.742-2.26a.043.043 0 01.042-.024s2.452.005
 2.452.003c.864 1.363 1.807 2.878 2.616 4.16l3.844-.002c.118 0
 .19-.13.125-.229l-2.832-4.321c-.01-.022.013-.025.018-.035zm-.45-3.355c-.437.412-1.185.612-2.163.612h-2.583l.952-2.874
 2.353.001c1.14.017 1.826.514 1.838 1.337.007.35-.138.688-.397.924z"
 />
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
