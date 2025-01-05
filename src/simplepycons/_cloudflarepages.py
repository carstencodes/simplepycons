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


class CloudflarePagesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudflarepages"

    @property
    def original_file_name(self) -> "str":
        return "cloudflarepages.svg"

    @property
    def title(self) -> "str":
        return "Cloudflare Pages"

    @property
    def primary_color(self) -> "str":
        return "#F38020"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudflare Pages</title>
     <path d="M10.715 14.32H5.442l-.64-1.203L13.673 0l1.397.579-1.752
 9.112h5.24l.648 1.192L10.719 24l-1.412-.54ZM4.091 5.448a.5787.5787 0
 1 1 0-1.1574.5787.5787 0 0 1 0 1.1574zm1.543 0a.5787.5787 0 1 1
 0-1.1574.5787.5787 0 0 1 0 1.1574zm1.544 0a.5787.5787 0 1 1
 0-1.1574.5787.5787 0 0 1 0
 1.1574zm8.657-2.7h5.424l.772.771v16.975l-.772.772h-7.392l.374-.579h6.779l.432-.432V3.758l-.432-.432h-4.676l-.552
 2.85h-.59l.529-2.877.108-.552ZM2.74
 21.265l-.772-.772V3.518l.772-.771h7.677l-.386.579H2.98l-.432.432v16.496l.432.432h5.586l-.092.579zm1.157-1.93h3.28l-.116.58h-3.55l-.192-.193v-3.473l.578
 1.158zm13.117 0 .579.58H14.7l.385-.58z" />
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
