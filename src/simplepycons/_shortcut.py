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


class ShortcutIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shortcut"

    @property
    def original_file_name(self) -> "str":
        return "shortcut.svg"

    @property
    def title(self) -> "str":
        return "Shortcut"

    @property
    def primary_color(self) -> "str":
        return "#494BCB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shortcut</title>
     <path d="M7.665.545H24L16.604 8.44l7.254 7.036-7.473 7.978L0
 23.451l7.427-7.929L.202 8.514Zm1.095 16.27-4.476 4.78 9.406.002Zm7.19
 4.387 5.304-5.663-5.92-5.742-5.304 5.663ZM14 8.503 8.11 2.788 2.805
 8.452l5.892 5.714Zm1.27-1.356 4.445-4.745h-9.336Z" />
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
