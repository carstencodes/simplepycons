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


class IftttIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ifttt"

    @property
    def original_file_name(self) -> "str":
        return "ifttt.svg"

    @property
    def title(self) -> "str":
        return "IFTTT"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IFTTT</title>
     <path d="M0 8.82h2.024v6.36H0zm11.566
 0h-3.47v2.024h1.446v4.337h2.024v-4.337h1.446V8.82zm5.494
 0h-3.47v2.024h1.446v4.337h2.024v-4.337h1.446V8.82zm5.494
 0h-3.47v2.024h1.446v4.337h2.024v-4.337H24V8.82zM7.518
 10.843V8.82H2.892v6.36h2.024v-1.734H6.65v-2.024H4.916v-.578z" />
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
