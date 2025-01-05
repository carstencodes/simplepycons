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


class GoogleDataprocIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googledataproc"

    @property
    def original_file_name(self) -> "str":
        return "googledataproc.svg"

    @property
    def title(self) -> "str":
        return "Google Dataproc"

    @property
    def primary_color(self) -> "str":
        return "#AECBFA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Dataproc</title>
     <path d="M23.373 20.364a4.682 4.682 0 0 1-8.1 0 4.694 4.694 0 0 1
 0-4.669c.326-.564.778-.995 1.272-1.358.472.198 3.394 1.421 3.917
 1.717a2.291 2.291 0 0 0-3.109.842 2.304 2.304 0 0 0 0 2.267 2.267
 2.267 0 0 0 2.564 1.053 2.254 2.254 0 0 0 1.375-1.053 2.328 2.328 0 0
 0 0-2.279 2.478 2.478 0 0 0-.83-.83l-3.53-2.045-5.727-3.317a5.022
 5.022 0 0 0 4.139-.36l6.32 3.641a4.682 4.682 0 0 1 1.709
 6.391zm-14-2.01v.004l-3.558 2a2.27 2.27 0 0 1-3.102-.823 2.267 2.267
 0 0 1 2.551-3.332c.591.161 1.089.56 1.375 1.102v-.05a2.27 2.27 0 0
 1-.824 3.103c.559-.303 3.352-2.62
 3.465-2.714-.304-1.744-1.573-3.24-3.396-3.72a4.608 4.608 0 0
 0-3.558.479 4.67 4.67 0 0 0-1.694 6.383 4.682 4.682 0 0 0 2.865 2.192
 4.657 4.657 0 0 0 3.66-.56l6.877-3.973c-.019-1.303.512-2.604
 1.375-3.58l-6.036 3.49zm-2.4-4.703v-8.1h.012c.002-1.617.821-3.189
 2.321-4.055a4.682 4.682 0 1 1 2.337 8.737 4.678 4.678 0 0
 1-1.55-.28c-.016-.085-.733-3.796-.733-4.188L9.29 9.59v6.761a4.075
 4.075 0 0 0-2.317-2.7zm2.403-8.1a2.279 2.279 0 1 0 4.546 0 2.23 2.23
 0 0 0-.297-1.127 2.279 2.279 0 0 0-1.97-1.14 2.267 2.267 0 0 0-2.279
 2.254v.013z" />
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
