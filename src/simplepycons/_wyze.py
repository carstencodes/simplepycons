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


class WyzeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wyze"

    @property
    def original_file_name(self) -> "str":
        return "wyze.svg"

    @property
    def title(self) -> "str":
        return "Wyze"

    @property
    def primary_color(self) -> "str":
        return "#1DF0BB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wyze</title>
     <path d="M5.475 13.171 7.3 9.469h.974L5.779
 14.53h-.608l-1.034-2.082-1.034 2.082h-.609L0 9.469h.973l1.826
 3.673.851-1.706-.973-1.967h.973l1.825 3.702Zm8.457-3.702-2.251
 3.442v1.591h-.882v-1.591L8.517 9.469h1.034l1.673 2.545
 1.673-2.545h1.035Zm5.444
 4.194H24v.867h-4.624v-.867Zm0-4.194H24v.868h-4.624v-.868Zm0
 2.083H24v.867h-4.624v-.867Zm-.273-2.083-3.438
 4.223h3.133v.838H13.84l3.407-4.222h-3.042v-.839h4.898Z" />
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
