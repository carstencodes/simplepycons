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


class OpenThreeDIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "open3d"

    @property
    def original_file_name(self) -> "str":
        return "open3d.svg"

    @property
    def title(self) -> "str":
        return "Open3D"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open3D</title>
     <path d="M5.998 1.606 0 12l5.998
 10.394h2.094l1.954-3.383H7.952L4.06 12.268h8.149l3.56 6.157L19.483
 12l-3.715-6.444-3.56 6.18H4.055l3.893-6.747h2.098L8.088 1.606Zm2.71 0
 1.954 3.383h5.386L20.096 12l-4.044 7.011h-5.394l-1.954
 3.383h9.294l.488-.847L24 12 18.002 1.606Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/isl-org/Open3D/blob/2ae042'''

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
