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


class ShadcnuiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shadcnui"

    @property
    def original_file_name(self) -> "str":
        return "shadcnui.svg"

    @property
    def title(self) -> "str":
        return "shadcn/ui"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>shadcn/ui</title>
     <path d="M22.219 11.784 11.784 22.219c-.407.407-.407 1.068 0
 1.476.407.407 1.068.407 1.476 0L23.695 13.26c.407-.408.407-1.069
 0-1.476-.408-.407-1.069-.407-1.476 0ZM20.132.305.305
 20.132c-.407.407-.407 1.068 0 1.476.408.407 1.069.407 1.476 0L21.608
 1.781c.407-.407.407-1.068 0-1.476-.408-.407-1.069-.407-1.476 0Z" />
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
