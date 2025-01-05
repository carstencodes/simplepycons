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


class NtfyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ntfy"

    @property
    def original_file_name(self) -> "str":
        return "ntfy.svg"

    @property
    def title(self) -> "str":
        return "ntfy"

    @property
    def primary_color(self) -> "str":
        return "#317F6F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ntfy</title>
     <path d="M12.597 13.693v2.156h6.205v-2.156ZM5.183
 6.549v2.363l3.591 1.901.023.01-.023.009-3.591 1.901v2.35l.386-.211
 5.456-2.969V9.729ZM3.659 2.037C1.915 2.037.42 3.41.42 5.154v.002L.438
 18.73 0 21.963l5.956-1.583h14.806c1.744 0 3.238-1.374
 3.238-3.118V5.154c0-1.744-1.493-3.116-3.237-3.117h-.001zm0
 2.2h17.104c.613.001 1.037.447 1.037.917v12.108c0
 .47-.424.916-1.038.916H5.633l-3.026.915.031-.179-.017-13.76c0-.47.424-.917
 1.038-.917z" />
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
