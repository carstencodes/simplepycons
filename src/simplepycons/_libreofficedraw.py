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


class LibreofficeDrawIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libreofficedraw"

    @property
    def original_file_name(self) -> "str":
        return "libreofficedraw.svg"

    @property
    def title(self) -> "str":
        return "LibreOffice Draw"

    @property
    def primary_color(self) -> "str":
        return "#CB6D30"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreOffice Draw</title>
     <path d="M5 0C3.338 0 2 1.338 2 3v18c0 1.662 1.338 3 3 3h14c1.662
 0 3-1.338 3-3V9l-9-9H5zm1 12a3 3 0 0 1 3-3c1.6 0 2.897 1.257 2.984
 2.837L11.5 11l-2.298 3.98c-.068.004-.133.02-.203.02a3 3 0 0
 1-3-3zm3.191 5 2.31-4 2.31 4H9.19zM18 16h-3.613L13
 13.597V11h5v5zm4-16v7l-7-7h7zm-5 15h-3v-3h3v3z" />
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
eab6e7b014ca97a8c452e829af4522dadfc8/source/media/navigation/libo-draw'''

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
