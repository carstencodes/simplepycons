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


class DenonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "denon"

    @property
    def original_file_name(self) -> "str":
        return "denon.svg"

    @property
    def title(self) -> "str":
        return "Denon"

    @property
    def primary_color(self) -> "str":
        return "#0B131A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Denon</title>
     <path d="m9.365 11.237 3.394 3.361v-5.07h-.778v3.16L8.58
 9.406v5.077h.779V11.27l.006-.033m-4.497
 3.245V9.528h2.79v.773H5.646v1.164h1.558v.772H5.646v1.472h1.999v.773H4.868M20.58
 11.23 24
 14.58V9.528h-.779v3.2l-.005-.015-3.422-3.311v5.08h.79v-3.234l-.003-.019M.78
 13.747v-3.503h.688s1.755-.032 1.755 1.77c0 1.647-1.593 1.733-1.593
 1.733H.78zM0 9.527v4.955h1.655s2.336-.193
 2.336-2.496c0-2.374-2.343-2.458-2.343-2.458H0zm14.416 2.452c0
 .552.187 1.006.56 1.361.713.724 1.931.702
 2.618-.01.724-.689.724-1.991.007-2.676-.675-.726-1.966-.724-2.645
 0-.36.357-.54.8-.54
 1.325zm-.764-.01c0-.702.26-1.306.777-1.81.981-1.004 2.724-1.016
 3.702.006 1.026.965 1.032 2.706-.003 3.66-.961.964-2.596
 1.015-3.624.084-.568-.493-.852-1.14-.852-1.94z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.denon.com/en-us/support/termsofus'''
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
