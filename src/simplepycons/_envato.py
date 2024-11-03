#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class EnvatoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "envato"

    @property
    def original_file_name(self) -> "str":
        return "envato.svg"

    @property
    def title(self) -> "str":
        return "Envato"

    @property
    def primary_color(self) -> "str":
        return "#81B441"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Envato</title>
     <path d="M20.058 1.043C16.744-2.841 6.018 4.682 6.104
 14.38a.459.459 0 0 1-.45.451.459.459 0 0 1-.388-.221 10.387 10.387 0
 0 1-.412-7.634.42.42 0 0 0-.712-.412 10.284 10.284 0 0 0-2.784
 7.033A10.284 10.284 0 0 0 11.76 23.999c14.635-.332 11.257-19.491
 8.298-22.956z" />
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
