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


class NomadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nomad"

    @property
    def original_file_name(self) -> "str":
        return "nomad.svg"

    @property
    def title(self) -> "str":
        return "Nomad"

    @property
    def primary_color(self) -> "str":
        return "#00CA8E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nomad</title>
     <path d="m12.004 0-10.4 6v12l10.392 6 10.4-6V6L12.004 0zm4.639
 13.204-2.77 1.6-3.347-1.832v3.826l-3.144 1.995V10.8L9.88 9.272l3.462
 1.823V7.191l3.301-1.984v7.997z" />
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
