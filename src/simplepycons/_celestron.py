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


class CelestronIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "celestron"

    @property
    def original_file_name(self) -> "str":
        return "celestron.svg"

    @property
    def title(self) -> "str":
        return "Celestron"

    @property
    def primary_color(self) -> "str":
        return "#F47216"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Celestron</title>
     <path d="M12 .002c-6.6266 0-12 5.3712-12 12 0 6.6275 5.3734
 11.996 12 11.996 1.7452 0 3.4033-.3698 4.8984-1.041C10.7585 21.2392
 2.2788 17.3246 3.25 9.5312c.6406-5.1338 7.2145-8.46
 13.8047-8.414C15.518.4012 13.8062.002 12 .002zm5.4297
 1.8437c-5.0918-.049-9.3055 2.0411-9.6875 5.5566-.6046 5.5956 7.1547
 8.8084 11.8437 10.1407.9056.2592 1.8969.4197 2.7676.5234C23.399
 16.286 24 14.2111 24
 12.002c0-4.2502-2.21-7.9827-5.541-10.1172a18.6755 18.6755 0 0
 0-1.0293-.0391z" />
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
