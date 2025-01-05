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


class TampermonkeyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tampermonkey"

    @property
    def original_file_name(self) -> "str":
        return "tampermonkey.svg"

    @property
    def title(self) -> "str":
        return "Tampermonkey"

    @property
    def primary_color(self) -> "str":
        return "#00485B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tampermonkey</title>
     <path d="M5.955.002C3-.071.275 2.386.043 5.335c-.069 3.32-.011
 6.646-.03 9.969.06 1.87-.276 3.873.715 5.573 1.083 2.076 3.456 3.288
 5.77 3.105 4.003-.011 8.008.022 12.011-.017 2.953-.156 5.478-2.815
 5.482-5.772-.007-4.235.023-8.473-.015-12.708C23.82 2.533 21.16.007
 18.205.003c-4.083-.005-8.167 0-12.25-.002zm.447 12.683c2.333-.046
 4.506 1.805 4.83 4.116.412 2.287-1.056 4.716-3.274
 5.411-2.187.783-4.825-.268-5.874-2.341-1.137-2.039-.52-4.827
 1.37-6.197a4.896 4.896 0 012.948-.99zm11.245 0c2.333-.046 4.505 1.805
 4.829 4.116.413 2.287-1.056 4.716-3.273
 5.411-2.188.783-4.825-.268-5.875-2.341-1.136-2.039-.52-4.827
 1.37-6.197a4.896 4.896 0 012.949-.99z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Tampe'''

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
