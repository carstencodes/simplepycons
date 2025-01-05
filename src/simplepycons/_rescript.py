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


class RescriptIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rescript"

    @property
    def original_file_name(self) -> "str":
        return "rescript.svg"

    @property
    def title(self) -> "str":
        return "ReScript"

    @property
    def primary_color(self) -> "str":
        return "#E6484F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ReScript</title>
     <path d="M23.29
 1.8c-.3-.4-.6-.7-.9-.9-1.3-.9-2.899-.9-6.098-.9H7.696C4.498 0 2.9 0
 1.8.8c-.4.3-.7.6-1 1C0 2.9 0 4.5 0 7.7v8.6c0 3.2 0 4.8.8
 5.9.3.4.6.7.9.9 1.199.9 2.798.9 5.996.9h8.596c3.199 0 4.798 0
 5.898-.8.4-.3.7-.6.9-.9.799-1.1.799-2.7.799-5.9V7.7c.2-3.2.2-4.8-.6-5.9ZM11.194
 16.5c0 .2 0 .5-.1.8 0
 .2-.1.3-.1.5-.1.1-.2.3-.4.5s-.4.3-.6.4c-.3.1-.7.1-1.399.1-.8 0-1.1
 0-1.4-.1-.4-.2-.699-.5-.899-.9-.1-.3-.1-.7-.1-1.4v-8c0-.9
 0-1.4.2-1.7.2-.3.4-.5.8-.7.3-.2.8-.2 1.699-.2h2.299zm5.097-4.9c-1.599
 0-2.798-1.3-2.798-2.8 0-1.6 1.3-2.8 2.798-2.8 1.5 0 2.8 1.3 2.8 2.8 0
 1.5-1.3 2.8-2.8 2.8z" />
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
