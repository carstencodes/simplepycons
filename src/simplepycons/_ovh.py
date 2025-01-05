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


class OvhIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ovh"

    @property
    def original_file_name(self) -> "str":
        return "ovh.svg"

    @property
    def title(self) -> "str":
        return "OVH"

    @property
    def primary_color(self) -> "str":
        return "#123F6D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OVH</title>
     <path d="M19.881 10.095l2.563-4.45C23.434 7.389 24 9.404 24
 11.555c0 2.88-1.017 5.523-2.71
 7.594h-6.62l2.04-3.541h-2.696l3.176-5.513h2.691zm-2.32-5.243L9.333
 19.14l.003.009H2.709C1.014 17.077 0 14.435 0 11.555c0-2.152.57-4.17
 1.561-5.918L5.855 13.1 10.6 4.852h6.961z" />
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
