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


class NextraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nextra"

    @property
    def original_file_name(self) -> "str":
        return "nextra.svg"

    @property
    def title(self) -> "str":
        return "Nextra"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nextra</title>
     <path d="M22.68 21.031c-4.98-4.98-4.98-13.083
 0-18.063l.978-.978c.22-.22.342-.513.342-.825
 0-.311-.122-.604-.342-.824-.44-.441-1.207-.44-1.648 0l-.979.978c-4.98
 4.98-13.084 4.98-18.063 0L1.99.34a1.17 1.17 0 0 0-1.649 0 1.168 1.168
 0 0 0 0 1.649l.978.978c4.98 4.98 4.98 13.083 0
 18.063l-.977.978c-.221.22-.342.513-.342.825 0
 .31.121.604.341.824.442.443 1.21.441 1.65 0l.977-.977c4.98-4.983
 13.083-4.98 18.064 0l.978.977c.22.22.513.342.824.342.312 0
 .605-.122.824-.342.22-.22.342-.512.342-.824
 0-.313-.122-.605-.342-.825l-.977-.978z" />
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
