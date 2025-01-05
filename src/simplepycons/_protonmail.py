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


class ProtonMailIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protonmail"

    @property
    def original_file_name(self) -> "str":
        return "protonmail.svg"

    @property
    def title(self) -> "str":
        return "Proton Mail"

    @property
    def primary_color(self) -> "str":
        return "#6D4AFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proton Mail</title>
     <path d="m15.24 8.998 3.656-3.073v15.81H2.482C1.11 21.735 0
 20.609 0 19.223V6.944l7.58 6.38a2.186 2.186 0 0 0
 2.871-.042l4.792-4.284h-.003zm-5.456 3.538 1.809-1.616a2.438 2.438 0
 0 1-1.178-.533L.905 2.395A.552.552 0 0 0 0 2.826v2.811l8.226
 6.923a1.186 1.186 0 0 0 1.558-.024zM23.871 2.463a.551.551 0 0
 0-.776-.068l-3.199 2.688v16.653h1.623c1.371 0 2.481-1.127
 2.481-2.513V2.824a.551.551 0 0 0-.129-.36z" />
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
