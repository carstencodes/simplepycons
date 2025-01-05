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
        return "#87E64B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Envato</title>
     <path d="M16.156 0a2.7 2.7 0 0 0-1.886.8L4
 11.253c-.382.42-.558.978-.453 1.57.176.945 1.116 1.571 2.06
 1.399l5.54-1.13c.12-.025.183.136.082.204L5.088 17.23c-.769.487-1.119
 1.36-.875 2.234.244 1.151 1.398 1.814 2.516 1.537l9.183-2.26a.11.11 0
 0 1 .113.176l-1.433 1.77c-.383.487.244
 1.15.77.767l4.716-3.877c.84-.697.281-2.062-.803-1.957l-.011-.004-6.047.65a.111.111
 0 0
 1-.08-.199l5.918-4.609c.382-.315.628-.801.523-1.326-.105-.803-.767-1.328-1.607-1.223l-6.43.942c-.112.015-.174-.128-.084-.2l6.375-4.867c1.256-.978
 1.36-2.898.209-4.015A2.6 2.6 0 0 0 16.156 0M13.1 21.855a1.07 1.07 0 0
 0-1.073 1.073A1.07 1.07 0 0 0 13.1 24a1.07 1.07 0 0 0 1.072-1.072
 1.07 1.07 0 0 0-1.072-1.073" />
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
