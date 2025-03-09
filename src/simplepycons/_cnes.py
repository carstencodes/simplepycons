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


class CnesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cnes"

    @property
    def original_file_name(self) -> "str":
        return "cnes.svg"

    @property
    def title(self) -> "str":
        return "CNES"

    @property
    def primary_color(self) -> "str":
        return "#204F8C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CNES</title>
     <path d="M10.173 0h.9531V13.7978c0 2.8809 3.6823 8.7293 9.7256
 4.8304l.1227-.0684C19.6214 21.7444 16.2555 24 12.3174 24 7.1854 24
 3.025 20.1694 3.025 15.444c0-4.0457 3.0498-7.4356
 7.148-8.327V0Zm10.3989
 11.5108c-1.5249-2.7076-4.5751-4.5697-8.1029-4.6216-.0643 1.1076.8245
 7.1347 4.9603 7.4718 1.0779.0879 3.84-.5495 3.1426-2.8502Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://fr.m.wikipedia.org/wiki/Fichier:Logo_'''

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
