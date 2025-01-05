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


class OxygenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oxygen"

    @property
    def original_file_name(self) -> "str":
        return "oxygen.svg"

    @property
    def title(self) -> "str":
        return "Oxygen"

    @property
    def primary_color(self) -> "str":
        return "#3A209E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Oxygen</title>
     <path d="M23.89 12c0-6.627-5.324-12-11.89-12S.109 5.373.109 12
 5.433 24 12 24c2.014 0 3.91-.508 5.573-1.4.62.354 1.338.558 2.105.558
 2.326 0 4.212-1.865 4.212-4.165
 0-.946-.319-1.818-.857-2.517.552-1.383.857-2.894.857-4.476zm-21.402.005c0-5.448
 4.269-9.864 9.535-9.864s9.535 4.416 9.535 9.864c0 1.07-.166
 2.099-.471 3.063a4.23 4.23 0 0 0-1.408-.239c-2.326 0-4.212
 1.865-4.212 4.165 0 .72.185 1.397.51 1.988a9.21 9.21 0 0
 1-3.953.888c-5.267-.001-9.536-4.418-9.536-9.865zm17.191
 9.864c-1.514.021-2.84-1.267-2.819-2.788 0-1.54 1.262-2.788
 2.819-2.788 1.507-.025 2.843 1.27 2.819 2.788 0 1.54-1.263
 2.788-2.819 2.788z" />
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
