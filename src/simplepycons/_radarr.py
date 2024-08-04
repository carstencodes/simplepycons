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


class RadarrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "radarr"

    @property
    def original_file_name(self) -> "str":
        return "radarr.svg"

    @property
    def title(self) -> "str":
        return "radarr"

    @property
    def primary_color(self) -> "str":
        return "#FFCB3D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>radarr</title>
     <path d="M5.274 0C3.189.039 1.19 1.547 1.19 4.705l.184 14.518c0
 1.47 1.103 2.205 2.573 2.021L3.764 3.786c0-1.654.919-1.838
 2.022-1.103l14.7 8.27c1.103.734 1.655 1.47 1.838
 2.756.92-1.654.552-4.043-1.286-5.33L7.991.846A4.559 4.559 0 0 0
 5.274.001zm1.982 6.91-.184 10.107 9.004-5.146Zm13.598 6.064-15.068
 8.82c-.92.552-2.022.736-3.124.368.918 1.47 3.307 2.389 5.145
 1.47l12.68-7.35c1.102-.736 1.286-2.022.367-3.308z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Radarr/Radarr/blob/5f624a1'''

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