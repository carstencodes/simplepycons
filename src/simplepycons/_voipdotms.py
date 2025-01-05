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


class VoipdotmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "voipdotms"

    @property
    def original_file_name(self) -> "str":
        return "voipdotms.svg"

    @property
    def title(self) -> "str":
        return "VoIP.ms"

    @property
    def primary_color(self) -> "str":
        return "#E1382D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VoIP.ms</title>
     <path d="M17.51 2.372c-.946 0-1.877.24-2.71.696a5.721 5.721 0 0
 0-2.055 1.92l-5.177 8.047c-.928 1.446-3.076 1.656-3.92.943l4.051
 6.343c.258.402.611.731 1.027.96a2.808 2.808 0 0 0 2.706 0 2.85 2.85 0
 0 0 1.025-.96L24 2.371ZM0 8.309l2.228 3.521s.89 1.302 2.402
 1.302c1.513 0 2.378-1.302 2.378-1.302l2.23-3.52Z" />
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
