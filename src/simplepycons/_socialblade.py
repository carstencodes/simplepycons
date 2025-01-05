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


class SocialBladeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "socialblade"

    @property
    def original_file_name(self) -> "str":
        return "socialblade.svg"

    @property
    def title(self) -> "str":
        return "Social Blade"

    @property
    def primary_color(self) -> "str":
        return "#B3382C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Social Blade</title>
     <path d="M2.323 16.688H0v1.893h2.323v-1.893ZM5.935
 13.591H3.613v4.99h2.322v-4.99ZM9.548
 14.796H7.226v3.785h2.322v-3.785ZM13.161
 13.935H10.84v4.646h2.322v-4.646ZM16.774
 12.043h-2.322v6.538h2.322v-6.538ZM20.387
 10.065h-2.323v8.516h2.323v-8.516ZM24 5.42h-2.323v13.16H24V5.42Z" />
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
