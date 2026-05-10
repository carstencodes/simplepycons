#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class HeliumBrowserIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "heliumbrowser"

    @property
    def original_file_name(self) -> "str":
        return "heliumbrowser.svg"

    @property
    def title(self) -> "str":
        return "Helium Browser"

    @property
    def primary_color(self) -> "str":
        return "#3450D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Helium Browser</title>
     <path d="M14.3081 22.2984 12 24l-2.3081-1.7016
 1.0489-8.1189-6.5174 4.9661L1.5938 18l.321-2.8467L9.4808
 12l-7.566-3.1533L1.5938 6l2.6296-1.1456 6.5174 4.9661-1.049-8.119L12
 0l2.3081 1.7016-1.0488 8.1189 6.5173-4.9661L22.4062 6l-.321
 2.8467L14.5192 12l7.566 3.1533.321 2.8467-2.6296
 1.1456-6.5173-4.9661z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/imputnet/helium-macos/blob
/0567a6078847e7dd11ce3c4f2eedcf49aa327dfe/resources/assets/AppIcon.ico'''

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
