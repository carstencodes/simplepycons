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


class FlathubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flathub"

    @property
    def original_file_name(self) -> "str":
        return "flathub.svg"

    @property
    def title(self) -> "str":
        return "Flathub"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flathub</title>
     <path d="M6.068 0a6 6 0 0 0-6 6 6 6 0 0 0 6 6 6 6 0 0 0 5.998-6 6
 6 0 0 0-5.998-6Zm9.15.08a1.656 1.656 0 0 0-1.654 1.656v8.15a1.656
 1.656 0 0 0 2.483 1.434l7.058-4.074a1.656 1.656 0 0 0
 0-2.869l-1.044-.604-6.014-3.47a1.656 1.656 0 0 0-.828-.223Zm3.575
 13.135a.815.815 0 0 0-.816.818v2.453h-2.454a.817.817 0 1 0 0
 1.635h2.454v2.453a.817.817 0 1 0 1.635 0v-2.453h2.452a.817.817 0 1 0
 0-1.635h-2.453v-2.453a.817.817 0 0 0-.818-.818zM2.865 13.5a2.794
 2.794 0 0 0-2.799 2.8v4.9c0 1.55 1.248 2.8 2.8 2.8h4.9c1.55 0
 2.8-1.25 2.8-2.8v-4.9c0-1.55-1.25-2.8-2.8-2.8Z" />
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
