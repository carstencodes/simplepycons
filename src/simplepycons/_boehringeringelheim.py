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


class BoehringerIngelheimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "boehringeringelheim"

    @property
    def original_file_name(self) -> "str":
        return "boehringeringelheim.svg"

    @property
    def title(self) -> "str":
        return "Boehringer Ingelheim"

    @property
    def primary_color(self) -> "str":
        return "#00E47C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Boehringer Ingelheim</title>
     <path d="M5.41 22.03c-1.72-1.24-2.63-2.15-3.49-3.46A12.185 12.185
 0 0 1 0 12.03C0 5.38 5.36 0 12 0s12 5.38 12 12c0 2.73-.93 5.46-2.58
 7.48-.68.86-1.26 1.36-2.83 2.55v-7.02h1.19v4.8c.88-1.04 1.31-1.67
 1.74-2.43.88-1.57 1.36-3.51 1.36-5.38
 0-6.06-4.88-10.99-10.89-10.99S1.11 5.94 1.11 12.08c0 2.8.99 5.28 3.08
 7.73v-4.8H5.4v7.02Zm2.37
 1.21c-.23-.05-.76-.3-1.19-.53V15h1.19v8.24Zm7.23-16.92L12 4 8.99
 6.32l-.66-.86 3.66-2.86 3.66 2.86-.66.86Zm-4.83
 17.56c-.43-.08-.45-.08-.61-.13-.13-.02-.18-.02-.58-.13V7.2h1.19v16.67Zm2.4.1c-.18.02-.23.02-.48.02-.38
 0-.51
 0-.71-.02V7.2h1.19v16.78Zm2.4-.38c-.38.13-.71.2-1.19.3V7.2h1.19v16.4Zm2.43-.88c-.38.18-.61.28-1.21.56v-8.27h1.21v7.71Z"
 />
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
