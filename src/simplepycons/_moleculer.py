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


class MoleculerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "moleculer"

    @property
    def original_file_name(self) -> "str":
        return "moleculer.svg"

    @property
    def title(self) -> "str":
        return "Moleculer"

    @property
    def primary_color(self) -> "str":
        return "#3CAFCE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Moleculer</title>
     <path d="M15.442.718a2.58 2.58 0 0 0-2.579 2.579 2.58 2.58 0 0 0
 1.368 2.275L12.809 8.27a3.505 3.505 0 0 0-1.077-.172 3.505 3.505 0 0
 0-3.505 3.505 3.505 3.505 0 0 0 .085.745l-2.83 1.036a2.97 2.97 0 0
 0-2.513-1.39A2.97 2.97 0 0 0 0 14.962a2.97 2.97 0 0 0 2.97 2.97 2.97
 2.97 0 0 0 2.969-2.97 2.97 2.97 0 0 0-.072-.634l2.716-1.193a3.505
 3.505 0 0 0 3.15 1.972 3.505 3.505 0 0 0 2.129-.724l2.276 2.167a4.305
 4.305 0 0 0-.749 2.426 4.305 4.305 0 0 0 4.306 4.305A4.305 4.305 0 0
 0 24 18.977a4.305 4.305 0 0 0-4.305-4.305 4.305 4.305 0 0
 0-2.718.969l-2.424-1.964a3.505 3.505 0 0 0 .684-2.074 3.505 3.505 0 0
 0-1.521-2.89l1.204-2.891a2.58 2.58 0 0 0 .522.054 2.58 2.58 0 0 0
 2.58-2.58 2.58 2.58 0 0 0-2.58-2.578Z" />
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
