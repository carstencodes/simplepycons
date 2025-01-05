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


class GnomeTerminalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gnometerminal"

    @property
    def original_file_name(self) -> "str":
        return "gnometerminal.svg"

    @property
    def title(self) -> "str":
        return "GNOME Terminal"

    @property
    def primary_color(self) -> "str":
        return "#241F31"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GNOME Terminal</title>
     <path d="M1.846 0A1.841 1.841 0 000 1.846v18.463c0 1.022.823
 1.845 1.846 1.845h20.308A1.841 1.841 0 0024 20.31V1.846A1.841 1.841 0
 0022.154 0H1.846zm0 .924h20.308c.512 0 .922.41.922.922v18.463c0
 .511-.41.921-.922.921H1.846a.919.919 0
 01-.922-.921V1.846c0-.512.41-.922.922-.922zm0
 .922v18.463h20.308V1.846H1.846zm1.845 2.14l3.235 1.758v.836L3.69
 8.477V7.385l2.243-1.207v-.033L3.69 5.076v-1.09zM7.846
 9.23h3.693v.924H7.846V9.23zM0 21.736v.418C0 23.177.823 24 1.846
 24h20.308A1.841 1.841 0 0024 22.154v-.418a2.334 2.334 0
 01-1.846.918H1.846A2.334 2.334 0 010 21.736Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://gitlab.gnome.org/Teams/Design/brand/-'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.gnome.org/GNOME/gnome-terminal
/-/blob/9c32e039bfb7902c136dc7aed3308e027325776c/data/icons/hicolor_ap'''

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
