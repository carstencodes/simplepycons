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


class MidiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "midi"

    @property
    def original_file_name(self) -> "str":
        return "midi.svg"

    @property
    def title(self) -> "str":
        return "MIDI"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MIDI</title>
     <path d="M21.775 7.517H24v8.966h-2.225zm-8.562 0h6.506c.66 0
 1.045.57 1.045 1.247v6.607c0 .84-.35 1.112-1.112
 1.112h-6.439v-5.696h2.225v3.505h3.135V9.54h-5.36zm-3.235
 0h2.19v8.966h-2.19zM0 7.517h7.854c.66 0 1.045.57 1.045
 1.247v7.72H6.708V9.774H5.427v6.708H3.438V9.775H2.191v6.708H0Z" />
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
