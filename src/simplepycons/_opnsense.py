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


class OpnsenseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opnsense"

    @property
    def original_file_name(self) -> "str":
        return "opnsense.svg"

    @property
    def title(self) -> "str":
        return "OPNSense"

    @property
    def primary_color(self) -> "str":
        return "#D94F00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OPNSense</title>
     <path d="M18.419
 11.08h5.259v1.847h-5.254l1.66.885v1.847l-5.111-2.732h-.005V11.08l5.111-2.737v1.847l-1.66.89zm.005
 5.54l5.255 2.808v1.841c.01 1.453-1.176 2.744-2.655
 2.731H.322v-4.573l5.252-2.808H2.119v-1.847h1.297v1.719l3.216-1.719h2.395v1.846l-3.453
 1.847h12.85l-3.455-1.847v-1.846h2.4l3.216
 1.719v-1.719h1.297v1.847h-3.458zM3.949
 20.307v-.972l-1.83.979v1.84h18.905c.481-.004.848-.393.857-.879v-.96l-1.764-.943v.936H3.949zm-.033-6.496v1.847l5.111-2.732V11.08L3.916
 8.343v1.847l1.665.89H.322v1.847h5.254l-1.66.884zM23.679 0v4.572L18.42
 7.386h3.462v1.847h-1.303V7.508l-3.222
 1.725h-2.39V7.386l3.451-1.847H5.578l3.449 1.847v1.847H6.638L3.416
 7.508v1.725H2.119V7.386h3.459L.322 4.572V2.731C.3 1.291 1.495-.012
 2.976 0h20.703zm-1.798
 1.846H2.976c-.488.009-.847.394-.857.88v.962l1.797.962v-.957h16.168v.956l1.797-.962V1.846z"
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
