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


class VaporIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vapor"

    @property
    def original_file_name(self) -> "str":
        return "vapor.svg"

    @property
    def title(self) -> "str":
        return "Vapor"

    @property
    def primary_color(self) -> "str":
        return "#0D0D0D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vapor</title>
     <path d="M22.75 13.908v1.56L12 24 1.25 15.468v-1.56L12
 22.44l10.75-8.532zM12 17.267L1.25 8.824 12 0l10.75 8.824L12
 17.267zm.356-4.635a3.193 3.193 0 0 0 3.193-3.193 3.185 3.185 0 0
 0-3.029-3.176l.001-.016-4.514-.427 1.205 4.102a3.184 3.184 0 0 0
 3.144 2.71zM12 20.269L1.25 11.737v1.533L12
 21.802l10.75-8.532v-1.533L12 20.269zm0-2.366L1.25 9.46v1.64L12
 19.63l10.75-8.532V9.46L12 17.903z" />
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
