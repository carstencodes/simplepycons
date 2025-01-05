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


class KanikoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kaniko"

    @property
    def original_file_name(self) -> "str":
        return "kaniko.svg"

    @property
    def title(self) -> "str":
        return "Kaniko"

    @property
    def primary_color(self) -> "str":
        return "#FFA600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kaniko</title>
     <path d="M2.783 0h18.434c1.352 0 2.478.963 2.73 2.24a17.127
 17.127 0 0 1-3.2 4.42 16.918 16.918 0 0 1-8.399
 4.605V3.304h-.696V11.4c-.976.169-1.965.253-2.956.252v.696c1.011 0
 1.998.086 2.956.252v8.096h.696v-7.961a16.918 16.918 0 0 1 8.399 4.605
 17.127 17.127 0 0 1 3.2 4.42 2.783 2.783 0 0 1-2.73 2.24H2.783A2.783
 2.783 0 0 1 0 21.217V2.783A2.783 2.783 0 0 1 2.783 0Zm18.456
 7.152A17.712 17.712 0 0 0 24 3.572v16.856a17.712 17.712 0 0
 0-2.761-3.58 17.802 17.802 0 0 0-8.891-4.815v-.066a17.802 17.802 0 0
 0 8.891-4.815Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/GoogleContainerTools/kanik
o/blob/cf5ca26aa4e2f7bf0de56efdf3b4e86b0ff74ed0/logo/Kaniko-Logo-Monoc'''

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
