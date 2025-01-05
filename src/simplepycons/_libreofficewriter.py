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


class LibreofficeWriterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libreofficewriter"

    @property
    def original_file_name(self) -> "str":
        return "libreofficewriter.svg"

    @property
    def title(self) -> "str":
        return "LibreOffice Writer"

    @property
    def primary_color(self) -> "str":
        return "#083FA6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreOffice Writer</title>
     <path d="M22 0v7l-7-7h7zm0 9v12c0 1.662-1.338 3-3 3H5c-1.662
 0-3-1.338-3-3V3c0-1.662 1.338-3 3-3h8l9 9zM6 10h5V9H6v1zm0
 2h5v-1H6v1zm0 2h5v-1H6v1zm5
 3H6v1h5v-1zm7-2H6v1h12v-1zm0-6h-6v5h6V9zm-1.5 2a.5.5 0 1 0 0-1 .5.5 0
 0 0 0 1zM14 11l-1 2h3l-2-2z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wiki.documentfoundation.org/Design/Br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/LibreOffice/help/blob/02fa
eab6e7b014ca97a8c452e829af4522dadfc8/source/media/navigation/libo-writ'''

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
