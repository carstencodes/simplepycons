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


class KeystoneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keystone"

    @property
    def original_file_name(self) -> "str":
        return "keystone.svg"

    @property
    def title(self) -> "str":
        return "Keystone"

    @property
    def primary_color(self) -> "str":
        return "#166BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Keystone</title>
     <path d="M4.5 0A4.5 4.5 0 000 4.5v15A4.5 4.5 0 004.5 24h15a4.5
 4.5 0 004.5-4.5v-15A4.5 4.5 0 0019.5 0zm5.47
 14.789v3.586H6.744V5.692H9.97v5.45h.167l4.218-5.45h3.463l-4.385 5.599
 4.64 7.084h-3.788l-3.2-5.001z" />
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
