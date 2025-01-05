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


class TeleFiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tele5"

    @property
    def original_file_name(self) -> "str":
        return "tele5.svg"

    @property
    def title(self) -> "str":
        return "TELE 5"

    @property
    def primary_color(self) -> "str":
        return "#FF00FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TELE 5</title>
     <path d="M.006
 0v5.027H3.83V0h-.685v4.18H2.23V.074h-.677V4.18h-.87V0H.007zm5.623.004v14.154h8.658V7.254h8.791V.004H5.628zM3.145
 6.076v3.9H.005v.85H3.83v-4.75h-.685zM23 9.926 5.389 18.502c2.371
 4.857 8.236 6.874 13.1 4.506v.002C23.352 20.64 25.372 14.783 23
 9.926zM.006
 12.129v5.027H3.83V12.13h-.685v4.18H2.23v-4.106h-.677v4.106h-.87v-4.18H.007zm0
 6.07v5.791h.687v-2.47H3.83v-.848H.693v-2.473H.006z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Tele_'''

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
