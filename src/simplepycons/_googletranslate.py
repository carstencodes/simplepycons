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


class GoogleTranslateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googletranslate"

    @property
    def original_file_name(self) -> "str":
        return "googletranslate.svg"

    @property
    def title(self) -> "str":
        return "Google Translate"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Translate</title>
     <path d="M22.401 4.818h-9.927L10.927 0H1.599C.72 0 .002.719.002
 1.599v16.275c0 .878.72 1.597 1.597 1.597h10L13.072 24H22.4c.878 0
 1.597-.707 1.597-1.572V6.39c0-.865-.72-1.572-1.597-1.572zm-15.66
 8.68c-2.07 0-3.75-1.68-3.75-3.75 0-2.07 1.68-3.75 3.75-3.75 1.012 0
 1.86.375 2.512.976l-.99.952a2.194 2.194 0 0 0-1.522-.584c-1.305
 0-2.363 1.08-2.363 2.409S5.436 12.16 6.74 12.16c1.507 0 2.13-1.08
 2.19-1.808l-2.188-.002V9.066h3.51c.05.23.09.457.09.764 0 2.147-1.434
 3.669-3.602 3.669zm16.757 8.93c0 .59-.492 1.072-1.097
 1.072h-8.875l3.649-4.03h.005l-.74-2.302.006-.005s.568-.488
 1.277-1.24c.712.771 1.63 1.699 2.818
 2.805l.771-.772c-1.272-1.154-2.204-2.07-2.89-2.805.919-1.087
 1.852-2.455
 2.049-3.707h2.034v.002h.002v-.94h-4.532v-1.52h-1.471v1.52H14.3l-1.672-5.21.006.022h9.767c.605
 0 1.097.48 1.097
 1.072v16.038zm-6.484-7.311c-.536.548-.943.873-.943.873l-.008.004-1.46-4.548h4.764c-.307
 1.084-.988 2.108-1.651
 2.904-1.176-1.392-1.18-1.844-1.18-1.844h-1.222s.05.678 1.7 2.61z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Googl'''

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
