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


class GeniusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "genius"

    @property
    def original_file_name(self) -> "str":
        return "genius.svg"

    @property
    def title(self) -> "str":
        return "Genius"

    @property
    def primary_color(self) -> "str":
        return "#FFFF64"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Genius</title>
     <path d="M0 6.827c0 2.164.79 4.133 2.167 5.51.393.393.786.59
 1.18.983h.195c.197 0
 .196-.196.196-.196-.393-.787-.588-1.77-.588-2.754 0-2.164.982-4.329
 2.36-5.706V1.518c0-.197-.197-.196-.197-.196h-2.95C.789 2.896 0 4.664
 0 6.827zm2.559 12.59c2.36 2.164 5.31 3.343 8.851 3.343 7.082 0
 12.59-5.702 12.59-12.586
 0-3.344-1.378-6.492-3.542-8.656h-.196c0-.197-.196 0-.196 0 .59
 1.574.983 3.147.983 4.918 0 7.278-5.902 13.373-13.377 13.373-1.77
 0-3.344-.393-4.917-.983-.197 0-.196.199-.196.395zm5.9-11.998c0
 .59.395 1.178.788 1.571h.392c3.54 1.18 4.722-.193
 4.722-1.767V5.056c0-.196.196-.196.196-.196h.787c.197 0
 .196-.196.196-.196-.196-1.18-.784-2.358-1.571-3.342h-2.363c0-.197-.196
 0-.196.196v2.95c0 1.574-1.18 2.754-2.754 2.951 0-.197-.196 0-.196 0z"
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
