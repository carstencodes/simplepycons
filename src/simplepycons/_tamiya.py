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


class TamiyaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tamiya"

    @property
    def original_file_name(self) -> "str":
        return "tamiya.svg"

    @property
    def title(self) -> "str":
        return "Tamiya"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tamiya</title>
     <path d="M0 6.408v4.27h4.496l1.36-4.27Zm5.856 0 1.398
 4.27h4.496v-4.27Zm5.894 4.27-3.627 2.644 1.398 4.27h2.23Zm-2.23
 6.914-3.664-2.645-3.627 2.645Zm-7.291 0 1.398-4.27L0
 10.678v6.914zM12.25 6.408v4.27h4.496l1.36-4.27zm5.856 0 1.398
 4.27H24v-4.27ZM24 10.678l-3.627 2.644 1.398 4.27H24Zm-2.23
 6.914-3.664-2.645-3.627 2.645zm-7.29 0 1.397-4.27-3.627-2.644v6.914z"
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
        return '''https://commons.wikimedia.org/wiki/File:TAMIY'''

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
