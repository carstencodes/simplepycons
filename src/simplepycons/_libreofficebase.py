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


class LibreofficeBaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libreofficebase"

    @property
    def original_file_name(self) -> "str":
        return "libreofficebase.svg"

    @property
    def title(self) -> "str":
        return "LibreOffice Base"

    @property
    def primary_color(self) -> "str":
        return "#7324A9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreOffice Base</title>
     <path d="M17 13h-1v-1h1v1zm0 1h-1v1h1v-1zm0
 2h-1v1h1v-1zm-.6-16H15l7 7V0h-5.6zM13 0l9 9v12c0 1.662-1.338 3-3
 3H5c-1.662 0-3-1.338-3-3V3c0-1.662 1.338-3 3-3h8zM6 11c0 .552 1.343 1
 3 1s3-.448 3-1v-1c0-.552-1.343-1-3-1s-3 .448-3 1v1zm0 2c0 .552 1.343
 1 3 1s3-.448 3-1v-1c0 .552-1.343 1-3 1s-3-.448-3-1v1zm0 2c0 .552
 1.343 1 3 1s3-.448 3-1v-1c0 .552-1.343 1-3 1s-3-.448-3-1v1zm0 2c0
 .552 1.343 1 3 1s3-.448 3-1v-1c0 .552-1.343 1-3
 1s-3-.448-3-1v1zm12-6h-5v7h5v-7zm-3 1h-1v1h1v-1zm0
 4h-1v1h1v-1zm0-2h-1v1h1v-1z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wiki.documentfoundation.org/Design/Br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/LibreOffice/help/blob/e3b1
cce7dde7e964c7670dd24a167e750654685a/source/media/navigation/libo-base'''

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
