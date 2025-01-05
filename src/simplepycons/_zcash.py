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


class ZcashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zcash"

    @property
    def original_file_name(self) -> "str":
        return "zcash.svg"

    @property
    def title(self) -> "str":
        return "Zcash"

    @property
    def primary_color(self) -> "str":
        return "#F3B724"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zcash</title>
     <path d="M12 0A12 12 0 0 0 0 12a12.013 12.013 0 0 0 12 12 12 12 0
 1 0 0-24zm-1.008 4.418h2.014v2.014l3.275-.002v1.826l-5.08
 6.889h5.08v2.423h-3.275v2.006h-2.012v-2.006H7.72v-1.826l5.074-6.888H7.719V6.432h3.273V4.418z"
 />
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
        yield from [
            "ZEC",
        ]
