#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TencentHyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tencenthy"

    @property
    def original_file_name(self) -> "str":
        return "tencenthy.svg"

    @property
    def title(self) -> "str":
        return "Tencent Hy"

    @property
    def primary_color(self) -> "str":
        return "#0052D9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tencent Hy</title>
     <path d="M12 0a1 1 0 0 1 0 24 1 1 0 0 1 0-24m1.65 1.12c.533.097
 1.023.233 1.41.404 6.086 2.686 7.398 9.217 1.603 14.341a3.782 3.782 0
 0 1-6.126-1.75 3.66 3.66 0 0 1-.095-1.622c-1.934.6-3.295 2.305-3.524
 4.45-.204 1.912.324 4.044 2.056 5.634A11 11 0 1 0 13.65 1.12M2.748
 6.21A11 11 0 0 0 8.9 22.55c-5.377-4.022-6.06-8.4-2.43-13.87a2.234
 2.234 0 1 0-3.722-2.47m10.157-5.172c4.408 1.33 3.61 5.41 2.447
 6.924-.86 1.117-2.922 1.46-3.708 2.238a4.18 4.18 0 0 0-1.212
 2.292A5.3 5.3 0 0 1 12 12.258a5.672 5.672 0 0 0 1.404-11.169 11 11 0
 0 0-.5-.052" />
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
